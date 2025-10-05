"""
Canada Job Bank scraper implementation.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
from urllib.parse import urljoin, urlencode
import time
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from .base import BaseScraper

class JobBankScraper(BaseScraper):
    """Scraper for jobbank.gc.ca"""
    
    BASE_URL = "https://www.jobbank.gc.ca"
    SEARCH_URL = f"{BASE_URL}/jobsearch/jobsearch"
    
    # Rate limiting settings
    REQUEST_DELAY = 2  # Delay between requests in seconds
    MAX_RETRIES = 3    # Maximum number of retries for failed requests
    RETRY_DELAY = 5    # Delay between retries in seconds
    
    def __init__(self):
        """Initialize Job Bank scraper with retry mechanism"""
        super().__init__()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=self.MAX_RETRIES,
            backoff_factor=self.RETRY_DELAY,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        # Create session with retry mechanism
        self.session = requests.Session()
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Set headers
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept-Language": "en-CA,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "DNT": "1"
        })
    
    def search(self, query, location, radius=None):
        """
        Search jobbank.gc.ca for jobs
        
        Args:
            query (str): Search query
            location (str): Location to search in
            radius (int, optional): Search radius in km
            
        Returns:
            list: List of job dictionaries
        """
        jobs = []
        page = 1
        consecutive_empty_pages = 0
        
        while True:
            # Construct search URL with parameters
            params = {
                "searchstring": query,
                "location": location,
                "page": page,
                "sort": "M"  # Sort by match
            }
            
            if radius:
                params["distance"] = min(radius, 100)  # Cap at 100km
            
            try:
                # Respect rate limiting
                time.sleep(self.REQUEST_DELAY)
                
                # Get search results page
                self.logger.info(f"Fetching page {page} for query '{query}' in {location}")
                response = self.session.get(
                    self.SEARCH_URL,
                    params=params,
                    timeout=30
                )
                response.raise_for_status()
                
                # Parse jobs from page
                page_jobs = self._parse_search_page(response.text)
                
                if not page_jobs:
                    consecutive_empty_pages += 1
                    if consecutive_empty_pages >= 2:  # Stop if 2 empty pages in a row
                        self.logger.info("No more results found")
                        break
                else:
                    consecutive_empty_pages = 0
                    jobs.extend(page_jobs)
                
                # Log progress
                self.logger.info(f"Found {len(page_jobs)} jobs on page {page}")
                
                page += 1
                
                # Stop after 5 pages to avoid excessive requests
                if page > 5:
                    self.logger.info("Reached maximum page limit")
                    break
                    
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Network error on page {page}: {str(e)}")
                if "Too Many Requests" in str(e):
                    self.logger.warning("Rate limit hit, waiting longer...")
                    time.sleep(self.RETRY_DELAY * 2)
                    continue
                break
                
            except Exception as e:
                self.logger.error(f"Unexpected error on page {page}: {str(e)}")
                break
        
        self.logger.info(f"Total jobs found: {len(jobs)}")
        return jobs
    
    def _parse_search_page(self, html):
        """Parse jobs from a search results page"""
        soup = BeautifulSoup(html, "html.parser")
        jobs = []
        
        # Check for no results message
        no_results = soup.find("div", class_="no-results")
        if no_results:
            return jobs
        
        # Find all job result containers
        results = soup.find_all("article", class_="job-search-result")
        if not results:
            self.logger.warning("No job results found on page")
            return jobs
        
        for result in results:
            try:
                # Get basic job info
                title_elem = result.find("span", class_="noc-title")
                company_elem = result.find("li", class_="business")
                location_elem = result.find("li", class_="location")
                
                if not all([title_elem, company_elem, location_elem]):
                    continue
                
                # Build job URL
                job_path = result.find("a", class_="resultJobItem")
                if not job_path or not job_path.get("href"):
                    continue
                    
                job_url = urljoin(self.BASE_URL, job_path["href"])
                
                # Create job object
                job = {
                    "title": self._clean_text(title_elem.get_text()),
                    "company": self._clean_text(company_elem.get_text()),
                    "location": self._clean_text(location_elem.get_text()),
                    "url": job_url,
                    "type": "job",  # Job Bank listings are formal jobs
                    "source": "Job Bank"
                }
                
                # Get salary if available
                salary_elem = result.find("li", class_="salary")
                if salary_elem:
                    job["salary"] = self._clean_text(salary_elem.get_text())
                
                # Get posting date
                date_elem = result.find("li", class_="date")
                if date_elem:
                    parsed_date = self._parse_date(date_elem.get_text())
                    if parsed_date:
                        job["posted_date"] = parsed_date.strftime("%Y-%m-%d")
                
                # Get job description snippet
                desc_elem = result.find("p", class_="summary")
                if desc_elem:
                    job["description"] = self._clean_text(desc_elem.get_text())
                
                # Validate and add job
                if self._validate_job(job):
                    jobs.append(job)
                    
            except Exception as e:
                self.logger.error(f"Error parsing job result: {str(e)}")
                continue
                
        return jobs
    
    def _parse_date(self, date_str):
        """Parse Job Bank date strings"""
        try:
            date_str = date_str.lower().strip()
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            
            # Handle "Posted on DATE" format
            if "posted on" in date_str:
                date_str = date_str.replace("posted on", "").strip()
                try:
                    return datetime.strptime(date_str, "%B %d, %Y")
                except ValueError:
                    pass
            
            # Handle relative dates
            if "today" in date_str:
                return today
            
            if "yesterday" in date_str:
                return today - timedelta(days=1)
            
            # Handle "X days ago"
            if match := re.search(r"(\d+) days? ago", date_str):
                days = int(match.group(1))
                return today - timedelta(days=days)
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error parsing date '{date_str}': {e}")
            return None 