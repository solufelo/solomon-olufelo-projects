"""
Kijiji scraper implementation.
Handles both services/gigs and job listings.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
from urllib.parse import urljoin, urlencode
import time
import json

from .base import BaseScraper

class KijijiScraper(BaseScraper):
    """Scraper for Kijiji.ca"""
    
    BASE_URL = "https://www.kijiji.ca"
    
    # Search endpoints
    JOBS_URL = f"{BASE_URL}/b-jobs"
    SERVICES_URL = f"{BASE_URL}/b-services"
    
    # Job categories of interest
    JOB_CATEGORIES = {
        "art-media-design": "c45",
        "graphic-design": "c46",
        "photography": "c47",
        "writing": "c48",
        "computer": "c54"
    }
    
    # Services/gigs categories
    SERVICE_CATEGORIES = {
        "artistic": "c72",
        "entertainment": "c73",
        "music-lessons": "c74",
        "photography": "c76",
        "web-design": "c78"
    }
    
    def __init__(self):
        """Initialize Kijiji scraper"""
        super().__init__()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept-Language": "en-CA,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        })
    
    def search(self, query, location, radius=None):
        """
        Search Kijiji for jobs and services/gigs
        
        Args:
            query (str): Search query
            location (str): Location to search in
            radius (int, optional): Search radius in km
            
        Returns:
            list: List of job dictionaries
        """
        jobs = []
        location_id = self._get_location_id(location)
        
        try:
            # Search jobs section
            jobs.extend(self._search_section(
                self.JOBS_URL,
                query,
                location_id,
                self.JOB_CATEGORIES,
                "job",
                radius
            ))
            
            # Slight delay to avoid rate limiting
            time.sleep(2)
            
            # Search services/gigs section
            jobs.extend(self._search_section(
                self.SERVICES_URL,
                query,
                location_id,
                self.SERVICE_CATEGORIES,
                "gig",
                radius
            ))
            
        except Exception as e:
            self.logger.error(f"Error during Kijiji search: {e}")
        
        return jobs
    
    def _get_location_id(self, location):
        """Get Kijiji location ID for a given location string"""
        # Common location IDs in the GTA
        location_map = {
            "brampton": "1700272",
            "mississauga": "1700277",
            "toronto": "1700273",
            "vaughan": "1700286",
            "woodbridge": "1700286",  # Part of Vaughan
            "etobicoke": "1700273"    # Part of Toronto
        }
        
        location_lower = location.lower().split(',')[0].strip()
        return location_map.get(location_lower, "1700272")  # Default to Brampton
    
    def _search_section(self, base_url, query, location_id, categories, job_type, radius=None):
        """Search a specific section (jobs or services) of Kijiji"""
        results = []
        
        # Search each relevant category
        for category_name, category_id in categories.items():
            try:
                # Construct search URL with parameters
                params = {
                    "keywords": query,
                    "locationId": location_id,
                    "dc": category_id,
                    "sort": "dateDesc"
                }
                
                if radius:
                    params["radius"] = min(radius, 100)  # Kijiji max radius is 100km
                
                # Get search results
                response = self.session.get(
                    base_url,
                    params=params,
                    timeout=30
                )
                response.raise_for_status()
                
                # Parse results
                page_results = self._parse_search_page(
                    response.text,
                    job_type,
                    category_name
                )
                results.extend(page_results)
                
                # Slight delay between categories
                time.sleep(1)
                
            except Exception as e:
                self.logger.error(
                    f"Error searching category {category_name}: {e}"
                )
                continue
        
        return results
    
    def _parse_search_page(self, html, job_type, category):
        """Parse jobs/gigs from a search results page"""
        soup = BeautifulSoup(html, "html.parser")
        results = []
        
        # Find all listing containers
        for listing in soup.find_all("div", class_="search-item"):
            try:
                # Get title and URL
                title_elem = listing.find("a", class_="title")
                if not title_elem:
                    continue
                
                # Build job object
                job = {
                    "title": self._clean_text(title_elem.get_text()),
                    "url": urljoin(self.BASE_URL, title_elem["href"]),
                    "type": job_type,
                    "category": category
                }
                
                # Get location
                location_elem = listing.find("div", class_="location")
                if location_elem:
                    job["location"] = self._clean_text(location_elem.get_text())
                else:
                    job["location"] = "Greater Toronto Area, ON"
                
                # Get date
                date_elem = listing.find("span", class_="date-posted")
                if date_elem:
                    job["posted_date"] = self._parse_date(date_elem.get_text())
                
                # Get price/compensation if available
                price_elem = listing.find("div", class_="price")
                if price_elem:
                    price_text = self._clean_text(price_elem.get_text())
                    if price_text and price_text.lower() != "free":
                        job["salary"] = price_text
                
                # Get description snippet
                desc_elem = listing.find("div", class_="description")
                if desc_elem:
                    job["description"] = self._clean_text(desc_elem.get_text())
                
                # Set company name based on context
                if job_type == "job":
                    company_elem = listing.find("div", class_="business")
                    job["company"] = self._clean_text(company_elem.get_text()) if company_elem else "See posting for details"
                else:
                    job["company"] = "Independent / Gig"
                
                # Validate and add job
                if self._validate_job(job):
                    results.append(job)
                
            except Exception as e:
                self.logger.error(f"Error parsing listing: {e}")
                continue
        
        return results
    
    def _parse_date(self, date_str):
        """Parse Kijiji date strings to YYYY-MM-DD format"""
        try:
            date_str = date_str.lower().strip()
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            
            # Handle "yesterday"
            if "yesterday" in date_str:
                return (today - timedelta(days=1)).strftime("%Y-%m-%d")
            
            # Handle "< X hours ago"
            if "hours ago" in date_str or "< 24 hours ago" in date_str:
                return today.strftime("%Y-%m-%d")
            
            # Handle "DD/MM/YYYY"
            if match := re.search(r"(\d{2})/(\d{2})/(\d{4})", date_str):
                try:
                    dt = datetime(
                        year=int(match.group(3)),
                        month=int(match.group(2)),
                        day=int(match.group(1))
                    )
                    return dt.strftime("%Y-%m-%d")
                except ValueError:
                    self.logger.error(f"Invalid date format: {date_str}")
                    return None
            
            # If no valid date format found, return None
            self.logger.error(f"Unrecognized date format: {date_str}")
            return None
            
        except Exception as e:
            self.logger.error(f"Error parsing date '{date_str}': {e}")
            return None 