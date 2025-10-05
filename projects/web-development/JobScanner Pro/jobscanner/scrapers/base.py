"""
Base scraper class that defines the interface for all job scrapers.
"""

from abc import ABC, abstractmethod
import logging

class BaseScraper(ABC):
    """Abstract base class for job scrapers"""
    
    def __init__(self):
        """Initialize scraper with logging"""
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def search(self, query, location, radius=None):
        """
        Search for jobs
        
        Args:
            query (str): Search query
            location (str): Location to search in
            radius (int, optional): Search radius in km
            
        Returns:
            list: List of job dictionaries with the following keys:
                - title (str): Job title
                - company (str): Company name
                - location (str): Job location
                - description (str): Job description
                - url (str): Job posting URL
                - type (str): Either 'job' or 'gig'
                - salary (str, optional): Salary information
                - posted_date (datetime, optional): When the job was posted
        """
        pass
    
    def _clean_text(self, text):
        """Clean up text by removing extra whitespace"""
        if not text:
            return ""
        return " ".join(text.split())
    
    def _validate_job(self, job):
        """
        Validate that a job has all required fields
        
        Args:
            job (dict): Job dictionary
            
        Returns:
            bool: True if valid, False otherwise
        """
        required_fields = {"title", "company", "location", "url", "type"}
        return all(field in job for field in required_fields) 