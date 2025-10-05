import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import csv
import webbrowser
import threading
import subprocess
import platform
import os
import logging
from pathlib import Path
from typing import Dict, List, Optional
import re

# Handle imports for both development and PyInstaller executable
try:
    from ..core.search import JobSearch
    from ..core.filters import filter_jobs, deduplicate_jobs
except ImportError:
    # Fallback for PyInstaller executable
    import sys
    from pathlib import Path
    
    # Add the jobscanner package to the path
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller executable
        app_path = Path(sys.executable).parent
    else:
        # Running in development
        app_path = Path(__file__).parent.parent
    
    sys.path.insert(0, str(app_path))
    
    from jobscanner.core.search import JobSearch
    from jobscanner.core.filters import filter_jobs, deduplicate_jobs

logger = logging.getLogger(__name__)

def safe_import(module_path_relative, module_path_absolute):
    """Safely import modules for both development and PyInstaller"""
    try:
        # Try relative import first
        parts = module_path_relative.split('.')
        if parts[0] == '':
            parts = parts[1:]  # Remove empty first element for relative imports
        
        module = __import__(module_path_relative, fromlist=[parts[-1]])
        return getattr(module, parts[-1]) if len(parts) > 1 else module
    except ImportError:
        # Fall back to absolute import
        parts = module_path_absolute.split('.')
        module = __import__(module_path_absolute, fromlist=[parts[-1]])
        return getattr(module, parts[-1]) if len(parts) > 1 else module

class JobScannerGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("JobScanner Pro - Advanced Job Search")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Search parameters
        self.job_title_var = tk.StringVar()
        self.company_var = tk.StringVar()
        self.location_var = tk.StringVar(value="Brampton, ON")
        self.radius_var = tk.IntVar(value=25)
        self.keywords_var = tk.StringVar()
        
        # Salary filter
        self.min_salary_var = tk.StringVar()
        self.max_salary_var = tk.StringVar()
        self.salary_type_var = tk.StringVar(value="hourly")
        
        # Job preferences
        self.job_type_var = tk.StringVar(value="any")
        self.experience_var = tk.StringVar(value="any")
        self.remote_pref_var = tk.StringVar(value="any")
        
        # Time filters
        self.date_posted_var = tk.StringVar(value="anytime")
        
        # Advanced options
        self.gigs_only_var = tk.BooleanVar()
        self.new_only_var = tk.BooleanVar()
        self.use_resume_keywords_var = tk.BooleanVar(value=True)
        
        # Source selection
        self.sources = {
            "indeed": tk.BooleanVar(value=False), # Disabled - API issues
            "jobbank": tk.BooleanVar(value=True),
            "craigslist": tk.BooleanVar(value=True),
            "kijiji": tk.BooleanVar(value=True)
        }
        
        # Resume/Cover letter paths
        self.resume_path_var = tk.StringVar()
        self.cover_letter_path_var = tk.StringVar()
        
        # Search state
        self.is_searching = tk.BooleanVar(value=False)
        self.search_thread = None
        
        # Initialize search config
        self.config = {
            "search": {
                "platforms": {
                    "indeed": True,   # Re-enabled Indeed with web scraping
                    "jobbank": True,
                    "craigslist": True,
                    "kijiji": True
                }
            }
        }
        
        self.setup_gui()
        self.results: List[Dict] = []
        
    def setup_gui(self):
        """Set up the enhanced GUI with essential job search fields"""
        # Create main container with notebook for tabbed interface
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Search Tab
        self.search_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.search_frame, text="Job Search")
        
        # Results Tab  
        self.results_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.results_frame, text="Search Results")
        
        self.setup_search_tab()
        self.setup_results_tab()
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to search...")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def setup_search_tab(self):
        """Setup the main search interface"""
        # Create scrollable frame
        canvas = tk.Canvas(self.search_frame)
        scrollbar = ttk.Scrollbar(self.search_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Main search container
        main_container = ttk.Frame(scrollable_frame)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # === ESSENTIAL SEARCH FIELDS ===
        search_essentials = ttk.LabelFrame(main_container, text="Essential Search Criteria", padding=15)
        search_essentials.pack(fill=tk.X, pady=(0, 15))
        
        # Job Title (with suggestions)
        ttk.Label(search_essentials, text="Job Title / Role:", font=('TkDefaultFont', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=5)
        job_title_combo = ttk.Combobox(search_essentials, textvariable=self.job_title_var, width=40)
        job_title_combo['values'] = [
            "Graphic Designer", "Web Designer", "UI/UX Designer", "Digital Marketing Specialist",
            "Content Creator", "Video Editor", "Photographer", "Social Media Manager",
            "Marketing Coordinator", "Brand Designer", "Creative Director", "Art Director"
        ]
        job_title_combo.grid(row=0, column=1, columnspan=2, sticky=tk.EW, pady=5, padx=(10, 0))
        
        # Company (optional)
        ttk.Label(search_essentials, text="Company (optional):").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(search_essentials, textvariable=self.company_var, width=40).grid(row=1, column=1, columnspan=2, sticky=tk.EW, pady=5, padx=(10, 0))
        
        # Location with popular choices
        ttk.Label(search_essentials, text="Location:", font=('TkDefaultFont', 10, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=5)
        location_combo = ttk.Combobox(search_essentials, textvariable=self.location_var, width=25)
        location_combo['values'] = [
            "Brampton, ON", "Mississauga, ON", "Toronto, ON", "Vaughan, ON", 
            "Markham, ON", "Richmond Hill, ON", "Oakville, ON", "Remote", "Canada"
        ]
        location_combo.grid(row=2, column=1, sticky=tk.EW, pady=5, padx=(10, 0))
        
        # Radius
        ttk.Label(search_essentials, text="Radius (km):").grid(row=2, column=2, sticky=tk.W, pady=5, padx=(20, 5))
        ttk.Spinbox(search_essentials, from_=5, to=100, textvariable=self.radius_var, width=8).grid(row=2, column=3, pady=5)
        
        # Additional Keywords
        ttk.Label(search_essentials, text="Additional Keywords:").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Entry(search_essentials, textvariable=self.keywords_var, width=40).grid(row=3, column=1, columnspan=2, sticky=tk.EW, pady=5, padx=(10, 0))
        
        # Configure grid weights
        search_essentials.grid_columnconfigure(1, weight=1)
        
        # === JOB PREFERENCES ===
        preferences_frame = ttk.LabelFrame(main_container, text="Job Preferences", padding=15)
        preferences_frame.pack(fill=tk.X, pady=(0, 15))
        
        # First row: Job Type, Experience, Remote Preference
        ttk.Label(preferences_frame, text="Job Type:").grid(row=0, column=0, sticky=tk.W, pady=5)
        job_type_combo = ttk.Combobox(preferences_frame, textvariable=self.job_type_var, width=15, state="readonly")
        job_type_combo['values'] = ["any", "full-time", "part-time", "contract", "freelance", "internship"]
        job_type_combo.grid(row=0, column=1, sticky=tk.W, pady=5, padx=(5, 15))
        
        ttk.Label(preferences_frame, text="Experience:").grid(row=0, column=2, sticky=tk.W, pady=5)
        exp_combo = ttk.Combobox(preferences_frame, textvariable=self.experience_var, width=15, state="readonly")
        exp_combo['values'] = ["any", "entry-level", "1-3 years", "3-5 years", "5-10 years", "10+ years"]
        exp_combo.grid(row=0, column=3, sticky=tk.W, pady=5, padx=(5, 15))
        
        ttk.Label(preferences_frame, text="Work Style:").grid(row=0, column=4, sticky=tk.W, pady=5)
        remote_combo = ttk.Combobox(preferences_frame, textvariable=self.remote_pref_var, width=15, state="readonly")
        remote_combo['values'] = ["any", "remote", "on-site", "hybrid"]
        remote_combo.grid(row=0, column=5, sticky=tk.W, pady=5, padx=(5, 0))
        
        # === SALARY FILTER ===
        salary_frame = ttk.LabelFrame(main_container, text="Salary Range (Optional)", padding=15)
        salary_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(salary_frame, text="Min:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(salary_frame, textvariable=self.min_salary_var, width=12).grid(row=0, column=1, pady=5, padx=(5, 10))
        
        ttk.Label(salary_frame, text="Max:").grid(row=0, column=2, sticky=tk.W, pady=5)
        ttk.Entry(salary_frame, textvariable=self.max_salary_var, width=12).grid(row=0, column=3, pady=5, padx=(5, 10))
        
        ttk.Label(salary_frame, text="Type:").grid(row=0, column=4, sticky=tk.W, pady=5)
        salary_type_combo = ttk.Combobox(salary_frame, textvariable=self.salary_type_var, width=10, state="readonly")
        salary_type_combo['values'] = ["hourly", "annual", "monthly"]
        salary_type_combo.grid(row=0, column=5, pady=5, padx=(5, 0))
        
        # === RESUME/CV INTEGRATION ===
        resume_frame = ttk.LabelFrame(main_container, text="Resume/CV Integration", padding=15)
        resume_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Resume upload
        ttk.Label(resume_frame, text="Resume/CV:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(resume_frame, textvariable=self.resume_path_var, width=50).grid(row=0, column=1, sticky=tk.EW, pady=5, padx=(5, 5))
        ttk.Button(resume_frame, text="Browse", command=self.browse_resume, width=10).grid(row=0, column=2, pady=5)
        
        # Cover letter upload
        ttk.Label(resume_frame, text="Cover Letter:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(resume_frame, textvariable=self.cover_letter_path_var, width=50).grid(row=1, column=1, sticky=tk.EW, pady=5, padx=(5, 5))
        ttk.Button(resume_frame, text="Browse", command=self.browse_cover_letter, width=10).grid(row=1, column=2, pady=5)
        
        # Use resume keywords option
        ttk.Checkbutton(resume_frame, text="Use resume keywords to find related jobs", 
                       variable=self.use_resume_keywords_var).grid(row=2, column=0, columnspan=3, sticky=tk.W, pady=10)
        
        resume_frame.grid_columnconfigure(1, weight=1)
        
        # === FILTERS & SOURCES ===
        filters_sources_frame = ttk.Frame(main_container)
        filters_sources_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Filters
        filters_frame = ttk.LabelFrame(filters_sources_frame, text="Additional Filters", padding=15)
        filters_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        ttk.Label(filters_frame, text="Date Posted:").grid(row=0, column=0, sticky=tk.W, pady=5)
        date_combo = ttk.Combobox(filters_frame, textvariable=self.date_posted_var, width=15, state="readonly")
        date_combo['values'] = ["anytime", "last 24 hours", "last 3 days", "last week", "last month"]
        date_combo.grid(row=0, column=1, sticky=tk.W, pady=5, padx=(5, 0))
        
        ttk.Checkbutton(filters_frame, text="Gigs only", variable=self.gigs_only_var).grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Checkbutton(filters_frame, text="New postings only", variable=self.new_only_var).grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Sources
        sources_frame = ttk.LabelFrame(filters_sources_frame, text="Job Sources", padding=15)
        sources_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        for i, (source, var) in enumerate(self.sources.items()):
            ttk.Checkbutton(sources_frame, text=source.title(), variable=var).grid(row=i, column=0, sticky=tk.W, pady=2)
        
        # === SEARCH CONTROLS ===
        search_controls = ttk.Frame(main_container)
        search_controls.pack(fill=tk.X, pady=20)
        
        # Search button with loading indicator
        self.search_btn = ttk.Button(search_controls, text="🔍 Search Jobs", command=self.start_search, 
                                   style='Accent.TButton')
        self.search_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Progress bar (initially hidden)
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(search_controls, variable=self.progress_var, mode='indeterminate')
        
        # Export and file management buttons
        ttk.Button(search_controls, text="📄 Export Results", command=self.export_results).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(search_controls, text="📁 Open Exports Folder", command=self.open_exports_folder).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(search_controls, text="🗑️ Clear Results", command=self.clear_results).pack(side=tk.LEFT)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def setup_results_tab(self):
        """Setup the results display tab"""
        # Results summary frame
        summary_frame = ttk.Frame(self.results_frame)
        summary_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.results_summary_var = tk.StringVar(value="No search performed yet")
        ttk.Label(summary_frame, textvariable=self.results_summary_var, font=('TkDefaultFont', 11, 'bold')).pack(side=tk.LEFT)
        
        # Results table with enhanced columns
        table_frame = ttk.Frame(self.results_frame)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        columns = ("Title", "Company", "Location", "Type", "Salary", "Posted", "Source", "Match %")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=20)
        
        # Configure columns with better widths
        column_widths = {"Title": 200, "Company": 150, "Location": 120, "Type": 80, 
                        "Salary": 100, "Posted": 80, "Source": 80, "Match %": 70}
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100))
        
        # Scrollbars for results table
        y_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        x_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        
        # Pack table and scrollbars
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind double-click to open job
        self.tree.bind("<Double-1>", self.open_job_link)
        
    def browse_resume(self):
        """Browse for resume file"""
        filename = filedialog.askopenfilename(
            title="Select Resume/CV",
            filetypes=[("PDF files", "*.pdf"), ("Word documents", "*.docx"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.resume_path_var.set(filename)
    
    def browse_cover_letter(self):
        """Browse for cover letter file"""
        filename = filedialog.askopenfilename(
            title="Select Cover Letter",
            filetypes=[("PDF files", "*.pdf"), ("Word documents", "*.docx"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.cover_letter_path_var.set(filename)
    
    def extract_resume_keywords(self):
        """Extract keywords from resume for enhanced search matching using NLP"""
        resume_path = self.resume_path_var.get()
        if not resume_path or not os.path.exists(resume_path):
            return []
        
        try:
            # Use the advanced resume parser - safe import for PyInstaller
            try:
                from ..utils.resume_parser import resume_parser
            except ImportError:
                from jobscanner.utils.resume_parser import resume_parser
            
            self.status_var.set("Analyzing resume with NLP...")
            self.root.update()
            
            # Parse the resume
            resume_data = resume_parser.parse_resume(resume_path)
            
            if not resume_data:
                self.status_var.set("Could not extract data from resume")
                return []
            
            # Store parsed data for later use
            self.parsed_resume_data = resume_data
            
            # Get top keywords for search enhancement
            keywords = resume_data.get('top_keywords', [])
            
            # Add some skills from different categories
            skills_by_cat = resume_data.get('skills_by_category', {})
            for category in ['design_skills', 'design_software', 'web_technologies']:
                if category in skills_by_cat:
                    keywords.extend(skills_by_cat[category][:3])
            
            # Remove duplicates while preserving order
            seen = set()
            unique_keywords = []
            for keyword in keywords:
                if keyword.lower() not in seen:
                    seen.add(keyword.lower())
                    unique_keywords.append(keyword)
            
            self.status_var.set(f"Extracted {len(unique_keywords)} keywords from resume")
            return unique_keywords[:15]  # Limit to top 15 keywords
            
        except Exception as e:
            self.status_var.set(f"Error analyzing resume: {str(e)}")
            logger.error(f"Resume parsing error: {e}")
            return []
    
    def generate_smart_search_terms(self):
        """Generate enhanced search terms based on job title and resume"""
        base_terms = []
        
        # Main job title
        job_title = self.job_title_var.get().strip()
        if job_title:
            base_terms.append(job_title)
            
            # Add related terms based on job title
            related_terms = {
                "graphic designer": ["visual designer", "brand designer", "creative designer", "digital designer"],
                "web designer": ["ui designer", "frontend designer", "digital designer", "web developer"],
                "marketing": ["digital marketing", "social media", "content marketing", "brand marketing"],
                "photographer": ["photo editor", "visual content creator", "digital photographer"],
                "video editor": ["motion graphics", "videographer", "content creator", "multimedia"]
            }
            
            for key, synonyms in related_terms.items():
                if key.lower() in job_title.lower():
                    base_terms.extend(synonyms)
        
        # Add company if specified
        company = self.company_var.get().strip()
        if company:
            base_terms.append(company)
        
        # Add additional keywords
        keywords = self.keywords_var.get().strip()
        if keywords:
            base_terms.extend([k.strip() for k in keywords.split(',')])
        
        # Add resume keywords if enabled
        if self.use_resume_keywords_var.get():
            if hasattr(self, 'parsed_resume_data') and self.parsed_resume_data:
                # Use already parsed resume data - safe import for PyInstaller
                try:
                    from ..utils.resume_parser import resume_parser
                except ImportError:
                    from jobscanner.utils.resume_parser import resume_parser
                smart_terms = resume_parser.get_job_search_terms(self.parsed_resume_data, job_title)
                base_terms.extend(smart_terms)
            else:
                # Extract keywords if not already parsed
                resume_keywords = self.extract_resume_keywords()
                base_terms.extend(resume_keywords)
        
        return list(set(base_terms))  # Remove duplicates
    
    def start_search(self):
        """Start the job search in a separate thread"""
        if self.is_searching.get():
            return
        
        # Validation
        if not self.job_title_var.get().strip():
            messagebox.showwarning("Input Required", "Please enter a job title to search for.")
            return
        
        self.is_searching.set(True)
        self.search_btn.configure(text="🔄 Searching...", state="disabled")
        self.progress_bar.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)
        self.progress_bar.start(10)
        
        # Start search in separate thread
        self.search_thread = threading.Thread(target=self.perform_search, daemon=True)
        self.search_thread.start()
    
    def perform_search(self):
        """Perform the actual job search"""
        try:
            self.status_var.set("Preparing search...")
            
            # Generate smart search terms
            search_terms = self.generate_smart_search_terms()
            primary_search = search_terms[0] if search_terms else self.job_title_var.get()
            
            self.status_var.set(f"Searching with enhanced terms: {', '.join(search_terms[:3])}...")
            
            # Update config based on selected sources
            for source, var in self.sources.items():
                self.config["search"]["platforms"][source] = var.get()
            
            # Create search instance
            job_search = JobSearch(config=self.config)
            
            # Determine remote preference filters
            remote_only = self.remote_pref_var.get() == "remote"
            on_site_only = self.remote_pref_var.get() == "on-site"
            
            # Perform primary search
            self.results = job_search.search(
                query=primary_search,
                location=self.location_var.get(),
                radius=self.radius_var.get(),
                gigs_only=self.gigs_only_var.get(),
                new_only=self.new_only_var.get(),
                remote_only=remote_only,
                on_site_only=on_site_only
            )
            
            # Perform additional searches for related terms
            if len(search_terms) > 1:
                for term in search_terms[1:3]:  # Search top 2 additional terms
                    self.status_var.set(f"Searching related term: {term}...")
                    additional_results = job_search.search(
                        query=term,
                        location=self.location_var.get(),
                        radius=self.radius_var.get(),
                        gigs_only=self.gigs_only_var.get(),
                        new_only=self.new_only_var.get(),
                        remote_only=remote_only,
                        on_site_only=on_site_only
                    )
                    self.results.extend(additional_results)
            
            # Remove duplicates and apply salary filtering
            self.results = deduplicate_jobs(self.results)
            self.results = self._apply_salary_filter(self.results)
            self._calculate_match_scores(search_terms)
            
            # Sort by match score
            self.results.sort(key=lambda x: x.get('match_score', 0), reverse=True)
            
            # Update UI in main thread
            self.root.after(0, self.update_results_display)
            
        except Exception as e:
            error_msg = str(e)  # Capture the error message immediately
            self.root.after(0, lambda msg=error_msg: self.search_error(msg))
    
    def _calculate_match_scores(self, search_terms):
        """Calculate match scores for jobs based on search terms"""
        for job in self.results:
            score = 0
            job_text = f"{job.get('title', '')} {job.get('description', '')} {job.get('company', '')}".lower()
            
            for term in search_terms:
                if term.lower() in job_text:
                    score += 1
            
            # Bonus for exact title match
            if search_terms and search_terms[0].lower() in job.get('title', '').lower():
                score += 2
            
            job['match_score'] = min(100, int((score / len(search_terms)) * 100)) if search_terms else 50
    
    def _apply_salary_filter(self, results):
        """Apply salary filtering to search results"""
        try:
            min_salary = self.min_salary_var.get().strip()
            max_salary = self.max_salary_var.get().strip()
            salary_type = self.salary_type_var.get()
            
            if not min_salary and not max_salary:
                return results
            
            # Convert to float values
            min_val = float(min_salary) if min_salary else None
            max_val = float(max_salary) if max_salary else None
            
            # Import and use salary parser - safe import for PyInstaller
            try:
                from ..utils.salary_parser import salary_parser
            except ImportError:
                from jobscanner.utils.salary_parser import salary_parser
            
            filtered_results = salary_parser.filter_jobs_by_salary(
                results, min_val, max_val, salary_type
            )
            
            logger.info(f"Salary filtering: {len(results)} -> {len(filtered_results)} jobs")
            return filtered_results
            
        except ValueError:
            # Invalid salary values, return all results
            logger.warning("Invalid salary values provided, skipping salary filter")
            return results
        except Exception as e:
            logger.error(f"Error applying salary filter: {e}")
            return results
    
    def update_results_display(self):
        """Update the results display after search completion"""
        # Stop loading indicators
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.search_btn.configure(text="🔍 Search Jobs", state="normal")
        self.is_searching.set(False)
        
        # Clear existing results
        self.clear_results()
        
        # Update summary
        total_jobs = len(self.results)
        remote_jobs = len([j for j in self.results if 'remote' in j.get('location', '').lower()])
        avg_match = sum(j.get('match_score', 0) for j in self.results) / len(self.results) if self.results else 0
        
        summary = f"Found {total_jobs} jobs ({remote_jobs} remote) • Avg. Match: {avg_match:.0f}%"
        self.results_summary_var.set(summary)
        
        # Populate results table
        for job in self.results:
            # Format salary
            salary = job.get('salary', 'Not specified')
            if salary and len(salary) > 20:
                salary = salary[:17] + "..."
            
            # Format posting date
            posted = job.get('posted_date', 'N/A')
            
            # Add job type indicator
            job_type = job.get('type', '').capitalize()
            if 'remote' in job.get('location', '').lower():
                job_type += " (Remote)"
            
            self.tree.insert("", tk.END, values=(
                job.get("title", "")[:40] + ("..." if len(job.get("title", "")) > 40 else ""),
                job.get("company", "")[:25] + ("..." if len(job.get("company", "")) > 25 else ""),
                job.get("location", "")[:20] + ("..." if len(job.get("location", "")) > 20 else ""),
                job_type,
                salary,
                posted,
                job.get("source", "").capitalize(),
                f"{job.get('match_score', 0)}%"
            ))
        
        # Switch to results tab
        self.notebook.select(self.results_frame)
        self.status_var.set(f"Search completed - {total_jobs} jobs found")
    
    def search_error(self, error_msg):
        """Handle search errors"""
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.search_btn.configure(text="🔍 Search Jobs", state="normal")
        self.is_searching.set(False)
        
        messagebox.showerror("Search Error", f"Search failed: {error_msg}")
        self.status_var.set("Search failed")
    
    def open_job_link(self, event):
        """Open job link when double-clicking a result"""
        selected_item = self.tree.selection()
        if not selected_item:
            return
            
        item_index = self.tree.index(selected_item[0])
        if item_index < len(self.results):
            job_url = self.results[item_index].get("url")
            if job_url:
                webbrowser.open(job_url)
    
    def export_results(self):
        """Export search results with enhanced details"""
        if not self.results:
            messagebox.showinfo("Info", "No results to export")
            return
        
        try:
            # Create outputs directory
            output_dir = Path("outputs")
            output_dir.mkdir(exist_ok=True)
            
            # Generate timestamp
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Export to CSV with enhanced details
            csv_file = output_dir / f"job_search_results_{timestamp}.csv"
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'title', 'company', 'location', 'type', 'salary', 'posted_date', 
                    'source', 'url', 'match_score', 'description'
                ])
                writer.writeheader()
                
                for job in self.results:
                    # Clean up data for CSV
                    cleaned_job = {
                        'title': job.get('title', ''),
                        'company': job.get('company', ''),
                        'location': job.get('location', ''),
                        'type': job.get('type', ''),
                        'salary': job.get('salary', ''),
                        'posted_date': job.get('posted_date', ''),
                        'source': job.get('source', ''),
                        'url': job.get('url', ''),
                        'match_score': job.get('match_score', 0),
                        'description': job.get('description', '')[:500]  # Limit description length
                    }
                    writer.writerow(cleaned_job)
            
            # Also export search parameters for reference
            params_file = output_dir / f"search_parameters_{timestamp}.json"
            search_params = {
                'job_title': self.job_title_var.get(),
                'company': self.company_var.get(),
                'location': self.location_var.get(),
                'radius': self.radius_var.get(),
                'keywords': self.keywords_var.get(),
                'job_type': self.job_type_var.get(),
                'experience': self.experience_var.get(),
                'remote_preference': self.remote_pref_var.get(),
                'min_salary': self.min_salary_var.get(),
                'max_salary': self.max_salary_var.get(),
                'date_posted': self.date_posted_var.get(),
                'sources': {k: v.get() for k, v in self.sources.items()},
                'total_results': len(self.results),
                'search_timestamp': timestamp
            }
            
            with open(params_file, 'w') as f:
                json.dump(search_params, f, indent=2)
            
            messagebox.showinfo("Export Complete", 
                              f"Results exported to:\n• {csv_file.name}\n• {params_file.name}")
            self.status_var.set(f"Exported {len(self.results)} jobs to outputs folder")
            
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export results: {str(e)}")
    
    def open_exports_folder(self):
        """Open the exports folder in file manager"""
        try:
            output_dir = Path("outputs")
            output_dir.mkdir(exist_ok=True)
            
            # Open folder based on operating system
            if platform.system() == "Windows":
                os.startfile(output_dir)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", output_dir])
            else:  # Linux
                subprocess.run(["xdg-open", output_dir])
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open exports folder: {str(e)}")
    
    def clear_results(self):
        """Clear all search results"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.results = []
        self.results_summary_var.set("No results")

def main():
    """Main entry point for the GUI application"""
    root = tk.Tk()
    app = JobScannerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 