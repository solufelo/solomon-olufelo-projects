import tkinter as tk
from tkinter import ttk, messagebox
import json
import csv
import webbrowser
from pathlib import Path
from typing import Dict, List, Optional

from ..core.search import JobSearch
from ..utils.filters import filter_jobs, deduplicate_jobs

class JobScannerGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("JobScanner Pro")
        self.root.geometry("800x600")
        
        # Search parameters
        self.role_var = tk.StringVar()
        self.location_var = tk.StringVar(value="Brampton, ON")
        self.sources = {
            "jobbank": tk.BooleanVar(value=True),
            "craigslist": tk.BooleanVar(value=True),
            "kijiji": tk.BooleanVar(value=True)
        }
        
        # Initialize search config
        self.config = {
            "search": {
                "platforms": {
                    "indeed": False,  # Temporarily disabled
                    "jobbank": True,
                    "craigslist": True,
                    "kijiji": True
                }
            }
        }
        
        self.setup_gui()
        self.results: List[Dict] = []
        
    def setup_gui(self):
        """Set up the GUI components"""
        # Search Frame
        search_frame = ttk.LabelFrame(self.root, text="Search Parameters", padding=10)
        search_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Role input
        ttk.Label(search_frame, text="Role:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(search_frame, textvariable=self.role_var).grid(row=0, column=1, sticky=tk.EW)
        
        # Location input
        ttk.Label(search_frame, text="Location:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(search_frame, textvariable=self.location_var).grid(row=1, column=1, sticky=tk.EW)
        
        # Source checkboxes
        source_frame = ttk.LabelFrame(search_frame, text="Sources", padding=5)
        source_frame.grid(row=2, column=0, columnspan=2, sticky=tk.EW, pady=5)
        
        for i, (source, var) in enumerate(self.sources.items()):
            ttk.Checkbutton(source_frame, text=source.title(), variable=var).grid(row=0, column=i, padx=5)
        
        # Search button
        ttk.Button(search_frame, text="Search", command=self.search).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Results Frame
        results_frame = ttk.LabelFrame(self.root, text="Results", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Results Treeview
        self.tree = ttk.Treeview(results_frame, columns=("title", "company", "location", "source"), show="headings")
        
        # Configure columns
        self.tree.heading("title", text="Title")
        self.tree.heading("company", text="Company")
        self.tree.heading("location", text="Location")
        self.tree.heading("source", text="Source")
        
        # Add scrollbars
        y_scroll = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.tree.yview)
        x_scroll = ttk.Scrollbar(results_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        
        # Pack scrollbars and tree
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind double-click event
        self.tree.bind("<Double-1>", self.open_job_link)
        
        # Action buttons frame
        action_frame = ttk.Frame(self.root)
        action_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(action_frame, text="Export CSV", command=self.export_csv).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="Clear Results", command=self.clear_results).pack(side=tk.LEFT, padx=5)
        
    def search(self):
        """Perform job search with current parameters"""
        try:
            # Clear existing results
            self.clear_results()
            
            # Update config based on selected sources
            for source, var in self.sources.items():
                self.config["search"]["platforms"][source] = var.get()
            
            # Create search instance with config
            job_search = JobSearch(config=self.config)
            
            # Perform search
            self.results = job_search.search(
                query=self.role_var.get(),
                location=self.location_var.get()
            )
            
            # Update treeview
            for job in self.results:
                self.tree.insert("", tk.END, values=(
                    job.get("title", ""),
                    job.get("company", ""),
                    job.get("location", ""),
                    job.get("source", "")
                ))
                
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {str(e)}")
            
    def open_job_link(self, event):
        """Open job link in default browser when row is double-clicked"""
        selected_item = self.tree.selection()
        if not selected_item:
            return
            
        item_index = self.tree.index(selected_item[0])
        if item_index < len(self.results):
            job_url = self.results[item_index].get("url")
            if job_url:
                webbrowser.open(job_url)
                
    def export_csv(self):
        """Export current results to CSV file"""
        if not self.results:
            messagebox.showinfo("Info", "No results to export")
            return
            
        try:
            output_dir = Path("outputs")
            output_dir.mkdir(exist_ok=True)
            
            output_file = output_dir / "job_results.csv"
            with open(output_file, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["title", "company", "location", "source", "url"])
                writer.writeheader()
                writer.writerows(self.results)
                
            messagebox.showinfo("Success", f"Results exported to {output_file}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {str(e)}")
            
    def clear_results(self):
        """Clear all results from the treeview"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.results = []

def main():
    root = tk.Tk()
    app = JobScannerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 