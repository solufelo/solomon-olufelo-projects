"""
Indeed.ca job search implementation using the official Indeed API.
"""

import os
from datetime import datetime, timedelta
import logging
from typing import List, Dict, Optional, Tuple, Union
import requests
from urllib.parse import urljoin

from .base import BaseScraper

class IndeedScraper(BaseScraper):
    """Scraper for Indeed.ca using official API"""
    
    BASE_URL = "https://ca.indeed.com"
    API_BASE_URL = os.getenv('INDEED_API_BASE_URL', 'https://apis.indeed.com/oauth/v2')
    SEARCH_API_URL = os.getenv('INDEED_SEARCH_API_URL', 'https://apis.indeed.com/ads/search/v1')
    
    def __init__(self, config=None):
        """Initialize Indeed API client"""
        super().__init__()
        
        # Get API credentials from environment or config
        self.client_id = os.getenv('INDEED_CLIENT_ID')
        self.client_secret = os.getenv('INDEED_CLIENT_SECRET')
        
        # If not in environment, try to get from config
        if not all([self.client_id, self.client_secret]) and config:
            api_config = config.get('api', {}).get('indeed', {})
            self.client_id = api_config.get('client_id')
            self.client_secret = api_config.get('client_secret')
        
        if not all([self.client_id, self.client_secret]):
            self.logger.error(
                "Indeed API credentials not found. "
                "Add credentials to config.yml under api.indeed section or set INDEED_CLIENT_ID and INDEED_CLIENT_SECRET environment variables."
            )
            # Don't raise error, just disable functionality
            self.client_id = None
            self.client_secret = None
        else:
            client_id_display = self.client_id[:8] + "..." if self.client_id else "None"
            self.logger.info(f"Indeed API initialized with Client ID: {client_id_display}")
            
        # Initialize session
        self.session = requests.Session()
        self.access_token = None
        self.token_expires_at = None
        
    def _get_access_token(self) -> str:
        """
        Get OAuth access token for Indeed API
        
        Returns:
            str: Access token
        """
        # Check if we have a valid token
        if self.access_token and self.token_expires_at:
            if datetime.now() < self.token_expires_at - timedelta(minutes=5):
                return self.access_token
                
        # Request new token
        try:
            # Ensure we have string values for auth
            client_id = str(self.client_id) if self.client_id else ""
            client_secret = str(self.client_secret) if self.client_secret else ""
            
            response = self.session.post(
                f"{self.API_BASE_URL}/tokens",
                auth=(client_id, client_secret),
                data={'grant_type': 'client_credentials'},
                timeout=30
            )
            response.raise_for_status()
            
            data = response.json()
            self.access_token = data['access_token']
            self.token_expires_at = datetime.now() + timedelta(seconds=data['expires_in'])
            
            return self.access_token
            
        except Exception as e:
            self.logger.error(f"Error getting access token: {str(e)}")
            raise
            
    def search(self, query: str, location: str, radius: Optional[int] = None) -> List[Dict]:
        """
        Search Indeed.ca for jobs using the official API
        
        Args:
            query (str): Search query
            location (str): Location to search in
            radius (int, optional): Search radius in km
            
        Returns:
            list: List of job dictionaries
        """
        jobs = []
        start = 0
        limit = 25  # Results per page
        
        try:
            # Get access token
            access_token = self._get_access_token()
            
            while True:
                # Prepare search parameters
                params = {
                    'q': query,
                    'l': location,
                    'start': start,
                    'limit': limit,
                    'fromage': 30,  # Last 30 days
                    'sort': 'date',
                    'co': 'ca',  # Country code for Canada
                }
                
                if radius:
                    params['radius'] = radius
                
                # Make API request
                response = self.session.get(
                    self.SEARCH_API_URL,
                    params=params,
                    headers={'Authorization': f'Bearer {access_token}'},
                    timeout=30
                )
                response.raise_for_status()
                
                # Parse response
                data = response.json()
                results = data.get('results', [])
                
                if not results:
                    break
                    
                # Process jobs
                for result in results:
                    try:
                        job = {
                            'title': result['jobtitle'],
                            'company': result['company'],
                            'location': result['formattedLocation'],
                            'url': result['url'],
                            'type': 'job',  # Indeed listings are typically jobs
                            'source': 'Indeed',
                            'description': result.get('snippet', ''),
                            'posted_date': self._parse_date(result['date'])
                        }
                        
                        # Add salary if available
                        if result.get('salary'):
                            job['salary'] = result['salary']
                            
                        # Validate and add job
                        if self._validate_job(job):
                            jobs.append(job)
                            
                    except Exception as e:
                        self.logger.error(f"Error parsing job result: {str(e)}")
                        continue
                
                # Check if we have more results
                if len(results) < limit:
                    break
                    
                start += limit
                
        except Exception as e:
            self.logger.error(f"Error during Indeed API search: {str(e)}")
            
        return jobs
        
    def _parse_date(self, timestamp: str) -> Optional[str]:
        """
        Parse Indeed API date format to YYYY-MM-DD
        
        Args:
            timestamp (str): ISO format timestamp
            
        Returns:
            str: Date in YYYY-MM-DD format, or None if parsing fails
        """
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d')
        except Exception as e:
            self.logger.error(f"Error parsing date '{timestamp}': {str(e)}")
            return None 