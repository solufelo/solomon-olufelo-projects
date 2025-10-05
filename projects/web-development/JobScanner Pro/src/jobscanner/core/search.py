"""
Core search functionality for JobScanner Pro.
Coordinates job searches across multiple platforms.
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from pathlib import Path

# Import scrapers
from jobscanner.scrapers.indeed import IndeedScraper
from jobscanner.scrapers.jobbank import JobBankScraper
from jobscanner.scrapers.craigslist import CraigslistScraper
from jobscanner.scrapers.kijiji import KijijiScraper

# Import utilities
from .filters import deduplicate_jobs, filter_jobs

logger = logging.getLogger(__name__)

class JobSearch:
    """Manages job searches across multiple platforms"""
    
    def __init__(self, config):
        """Initialize with configuration"""
        self.config = config
        self.scrapers = self._initialize_scrapers()
        
    def _initialize_scrapers(self):
        """Initialize enabled scrapers from config"""
        scrapers = []
        platform_config = self.config["search"]["platforms"]
        
        if platform_config["indeed"]:
            scrapers.append(IndeedScraper(config=self.config))  # Pass config for API credentials
        if platform_config["jobbank"]:
            scrapers.append(JobBankScraper())
        if platform_config["craigslist"]:
            scrapers.append(CraigslistScraper())
        if platform_config["kijiji"]:
            scrapers.append(KijijiScraper())
            
        return scrapers
    
    def _add_source_info(self, jobs, source):
        """Add source information to job listings"""
        for job in jobs:
            job["source"] = source
            # Add source-specific prefix to job ID if not present
            if "id" in job and not job["id"].startswith(f"{source}_"):
                job["id"] = f"{source}_{job['id']}"
        return jobs
    
    def search(self, query, location, radius=None, gigs_only=False, new_only=False, 
               remote_only=False, on_site_only=False):
        """
        Search for jobs across all enabled platforms
        
        Args:
            query (str): Search query (e.g., "graphic designer")
            location (str): Location to search in
            radius (int, optional): Search radius in km
            gigs_only (bool): Only return gig postings
            new_only (bool): Only return new postings
            remote_only (bool): Only return remote jobs
            on_site_only (bool): Only return on-site jobs
            
        Returns:
            list: List of job dictionaries
        """
        logger.info(f"Searching for '{query}' in {location}")
        
        # Search all platforms in parallel
        with ThreadPoolExecutor() as executor:
            future_to_scraper = {
                executor.submit(
                    scraper.search,
                    query=query,
                    location=location,
                    radius=radius
                ): scraper for scraper in self.scrapers
            }
            
            # Collect all results
            all_jobs = []
            for future in future_to_scraper:
                try:
                    scraper = future_to_scraper[future]
                    jobs = future.result()
                    
                    # Add source information
                    source = scraper.__class__.__name__.replace("Scraper", "").lower()
                    jobs_with_source = self._add_source_info(jobs, source)
                    
                    all_jobs.extend(jobs_with_source)
                    logger.info(f"Found {len(jobs)} jobs from {source}")
                except Exception as e:
                    scraper = future_to_scraper[future]
                    logger.error(f"Error with {scraper.__class__.__name__}: {e}")
        
        # Apply filters
        filtered_jobs = filter_jobs(
            all_jobs,
            gigs_only=gigs_only,
            new_only=new_only,
            remote_only=remote_only,
            on_site_only=on_site_only,
            location=location
        )
        
        # Remove duplicates
        unique_jobs = deduplicate_jobs(filtered_jobs)
        
        # Log source breakdown
        source_counts = {}
        for job in unique_jobs:
            source = job.get("source", "unknown")
            source_counts[source] = source_counts.get(source, 0) + 1
            
        for source, count in source_counts.items():
            logger.info(f"Found {count} unique jobs from {source}")
        
        logger.info(f"Found {len(unique_jobs)} total unique jobs")
        return unique_jobs
    
    def export_results(self, jobs, output_file, format="csv"):
        """Export job results to file"""
        # Convert to DataFrame for easy export
        df = pd.DataFrame(jobs)
        
        # Create output directory if it doesn't exist
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        
        # Export based on format
        if format == "csv":
            df.to_csv(output_file, index=False)
        elif format == "json":
            df.to_json(output_file, orient="records", indent=2)
            
        logger.info(f"Exported {len(jobs)} jobs to {output_file}")
    
    def display_results(self, jobs):
        """Display job results in the console"""
        if not jobs:
            print("\nNo jobs found matching your criteria.")
            return
            
        print(f"\nFound {len(jobs)} jobs:")
        print("-" * 80)
        
        for i, job in enumerate(jobs, 1):
            print(f"{i}. {job['title']}")
            print(f"   Company: {job['company']}")
            print(f"   Location: {job['location']}")
            print(f"   Type: {job['type']}")  # 'job' or 'gig'
            print(f"   Source: {job.get('source', 'Unknown')}")
            print(f"   URL: {job['url']}")
            if job.get('salary'):
                print(f"   Salary: {job['salary']}")
            print("-" * 80) 