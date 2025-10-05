"""
Craigslist Toronto scraper implementation.
Handles both jobs and gigs sections.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
from urllib.parse import urljoin, quote_plus
import time

from .base import BaseScraper

class CraigslistScraper(BaseScraper):
    """Scraper for Craigslist Toronto"""
    
    BASE_URL = "https://toronto.craigslist.org"
    
    # Search endpoints
    JOBS_URL = f"{BASE_URL}/search/jjj"  # Jobs
    GIGS_URL = f"{BASE_URL}/search/ggg"  # Gigs
    
    # Job categories to search in
    JOB_CATEGORIES = {
        "art": "art",
        "media": "med",
        "web": "web",
        "creative": "crg",
        "design": "des"
    }
    
    # Gig categories
    GIG_CATEGORIES = {
        "creative": "crg",
        "computer": "cpg",
        "art": "art"
    }
    
    def __init__(self):
        """Initialize Craigslist scraper"""
        super().__init__()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept-Language": "en-CA,en;q=0.9"
        })
    
    def search(self, query, location, radius=None):
        """
        Search Craigslist Toronto for jobs and gigs
        
        Args:
            query (str): Search query
            location (str): Location to search in (will focus on Toronto area)
            radius (int, optional): Search radius in km (used for location filtering)
            
        Returns:
            list: List of job dictionaries
        """
        jobs = []
        
        # Search both jobs and gigs sections
        try:
            # Get jobs
            jobs.extend(self._search_section(
                self.JOBS_URL,
                query,
                self.JOB_CATEGORIES,
                "job"
            ))
            
            # Slight delay to avoid rate limiting
            time.sleep(2)
            
            # Get gigs
            jobs.extend(self._search_section(
                self.GIGS_URL,
                query,
                self.GIG_CATEGORIES,
                "gig"
            ))
            
        except Exception as e:
            self.logger.error(f"Error during Craigslist search: {e}")
        
        # Filter by location if radius specified
        if radius and location.lower().startswith("brampton"):
            jobs = self._filter_by_distance(jobs, radius)
        
        return jobs
    
    def _search_section(self, base_url, query, categories, job_type):
        """Search a specific section (jobs or gigs) of Craigslist"""
        results = []
        
        # Search each relevant category
        for category in categories.values():
            try:
                params = {
                    "query": query,
                    "sort": "date",  # Sort by newest first
                }
                
                # Add category filter
                url = f"{base_url}/{category}" if category else base_url
                
                # Get search results
                response = self.session.get(
                    url,
                    params=params,
                    timeout=30
                )
                response.raise_for_status()
                
                # Parse results
                page_results = self._parse_search_page(
                    response.text,
                    job_type
                )
                results.extend(page_results)
                
                # Slight delay between categories
                time.sleep(1)
                
            except Exception as e:
                self.logger.error(
                    f"Error searching category {category}: {e}"
                )
                continue
        
        return results
    
    def _parse_search_page(self, html, job_type):
        """Parse jobs/gigs from a search results page"""
        soup = BeautifulSoup(html, "html.parser")
        results = []
        
        # Find all result rows
        for row in soup.find_all("li", class_="result-row"):
            try:
                # Get title and URL
                title_elem = row.find("a", class_="result-title")
                if not title_elem:
                    continue
                    
                # Get basic job info
                job = {
                    "title": self._clean_text(title_elem.get_text()),
                    "url": title_elem["href"],
                    "type": job_type
                }
                
                # Get location
                location_elem = row.find("span", class_="result-hood")
                job["location"] = self._clean_text(
                    location_elem.get_text().strip("()") if location_elem
                    else "Toronto, ON"
                )
                
                # Set company (Craigslist often doesn't show this)
                job["company"] = "See posting for details"
                
                # Get posting date
                date_elem = row.find("time", class_="result-date")
                if date_elem:
                    job["posted_date"] = self._parse_date(
                        date_elem["datetime"]
                    )
                
                # Get compensation if available
                price_elem = row.find("span", class_="result-price")
                if price_elem:
                    job["salary"] = self._clean_text(price_elem.get_text())
                
                # Validate and add job
                if self._validate_job(job):
                    results.append(job)
                    
            except Exception as e:
                self.logger.error(f"Error parsing result row: {e}")
                continue
        
        return results
    
    def _parse_date(self, date_str):
        """Parse Craigslist date string to YYYY-MM-DD format"""
        try:
            # Craigslist uses ISO format
            dt = datetime.fromisoformat(date_str)
            return dt.strftime("%Y-%m-%d")
        except Exception as e:
            self.logger.error(f"Error parsing date '{date_str}': {e}")
            return None
    
    def _filter_by_distance(self, jobs, radius_km):
        """
        Filter jobs by distance from Brampton
        Very basic filtering - only includes jobs with specific locations
        """
        brampton_locations = {
            "brampton",
            "mississauga",  # Include nearby cities within typical radius
            "etobicoke",
            "woodbridge",
            "vaughan"
        }
        
        filtered = []
        for job in jobs:
            location = job["location"].lower()
            
            # Include if in Brampton or nearby cities
            if any(city in location for city in brampton_locations):
                filtered.append(job)
                
            # Include if no specific location (might be remote)
            elif location == "toronto, on":
                filtered.append(job)
        
        return filtered 