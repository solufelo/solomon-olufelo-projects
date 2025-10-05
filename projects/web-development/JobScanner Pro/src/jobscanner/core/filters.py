"""
Job filtering and deduplication module.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import logging
import re

logger = logging.getLogger(__name__)

def filter_jobs(jobs: List[Dict], 
               new_only: bool = False,
               gigs_only: bool = False,
               jobs_only: bool = False,
               remote_only: bool = False,
               on_site_only: bool = False,
               source: Optional[str] = None,
               min_radius: Optional[int] = None,
               max_radius: Optional[int] = None,
               location: Optional[str] = None) -> List[Dict]:
    """
    Filter jobs based on various criteria
    
    Args:
        jobs (List[Dict]): List of job dictionaries
        new_only (bool): Only return jobs posted in last 24h
        gigs_only (bool): Only return gigs
        jobs_only (bool): Only return formal jobs
        remote_only (bool): Only return remote jobs
        on_site_only (bool): Only return on-site jobs
        source (str, optional): Filter by source (e.g., 'Job Bank', 'Kijiji')
        min_radius (int, optional): Minimum radius in km from location
        max_radius (int, optional): Maximum radius in km from location
        location (str, optional): Base location for radius filtering
        
    Returns:
        List[Dict]: Filtered list of jobs
    """
    filtered = jobs.copy()
    
    # Filter by job type
    if gigs_only:
        filtered = [job for job in filtered if job.get('type') == 'gig']
    elif jobs_only:
        filtered = [job for job in filtered if job.get('type') == 'job']
        
    # Filter by work arrangement (remote vs on-site)
    if remote_only:
        filtered = [job for job in filtered if _is_remote_job(job)]
        logger.info(f"Filtered to {len(filtered)} remote jobs")
    elif on_site_only:
        filtered = [job for job in filtered if not _is_remote_job(job)]
        logger.info(f"Filtered to {len(filtered)} on-site jobs")
        
    # Filter by source
    if source:
        filtered = [job for job in filtered if job.get('source', '').lower() == source.lower()]
        
    # Filter by posting date
    if new_only:
        cutoff = datetime.now() - timedelta(days=1)
        filtered = [
            job for job in filtered 
            if job.get('posted_date') and 
            datetime.strptime(job['posted_date'], '%Y-%m-%d') >= cutoff
        ]
    
    # Filter by location radius if both location and radius provided
    if location and (min_radius is not None or max_radius is not None):
        filtered = _filter_by_radius(filtered, location, min_radius, max_radius)
        
    logger.info(f"Filtered {len(jobs)} jobs to {len(filtered)} results")
    return filtered

def deduplicate_jobs(jobs: List[Dict]) -> List[Dict]:
    """
    Remove duplicate job listings based on URL and fuzzy title matching
    
    Args:
        jobs (List[Dict]): List of job dictionaries
        
    Returns:
        List[Dict]: Deduplicated list of jobs
    """
    seen_urls = set()
    unique_jobs = []
    
    for job in jobs:
        url = job.get('url')
        
        # Skip if no URL or already seen
        if not url or url in seen_urls:
            continue
            
        # Check for similar existing jobs
        duplicate = False
        for existing in unique_jobs:
            if _is_duplicate_job(job, existing):
                duplicate = True
                break
                
        if not duplicate:
            unique_jobs.append(job)
            seen_urls.add(url)
            
    logger.info(f"Deduplicated {len(jobs)} jobs to {len(unique_jobs)} unique listings")
    return unique_jobs

def _is_duplicate_job(job1: Dict, job2: Dict) -> bool:
    """
    Check if two jobs are likely duplicates based on:
    - Identical URLs
    - Very similar titles and companies
    - Same location and similar descriptions
    
    Args:
        job1 (Dict): First job dictionary
        job2 (Dict): Second job dictionary
        
    Returns:
        bool: True if jobs appear to be duplicates
    """
    # Same URL = definite duplicate
    if job1.get('url') == job2.get('url'):
        return True
        
    # Check title similarity
    title1 = job1.get('title', '').lower()
    title2 = job2.get('title', '').lower()
    
    if title1 and title2:
        # Exact match
        if title1 == title2:
            return True
            
        # Very similar titles (one contains the other)
        if title1 in title2 or title2 in title1:
            # If titles are similar, check company
            company1 = job1.get('company', '').lower()
            company2 = job2.get('company', '').lower()
            
            if company1 and company2 and (
                company1 == company2 or
                company1 in company2 or
                company2 in company1
            ):
                return True
                
    return False

def _is_remote_job(job: Dict) -> bool:
    """
    Detect if a job is remote based on title, location, and description
    
    Args:
        job (Dict): Job dictionary
        
    Returns:
        bool: True if job appears to be remote
    """
    # Remote keywords to look for
    remote_keywords = [
        'remote', 'work from home', 'wfh', 'telecommute', 'telework',
        'work remotely', 'home office', 'virtual', 'anywhere',
        'distributed', 'location independent'
    ]
    
    # Check title for remote keywords
    title = job.get('title', '').lower()
    if any(keyword in title for keyword in remote_keywords):
        return True
    
    # Check location for remote indicators
    location = job.get('location', '').lower()
    if any(keyword in location for keyword in remote_keywords):
        return True
    
    # Specific location patterns that indicate remote work
    remote_location_patterns = [
        r'\bremote\b',
        r'\banywhere\b',
        r'\bcanada\b$',  # Just "Canada" often means remote
        r'\bhome\b',
        r'\bvirtual\b'
    ]
    
    for pattern in remote_location_patterns:
        if re.search(pattern, location, re.IGNORECASE):
            return True
    
    # Check description for remote keywords
    description = job.get('description', '').lower()
    if description and any(keyword in description for keyword in remote_keywords):
        return True
    
    return False

def _filter_by_radius(jobs: List[Dict], 
                     base_location: str,
                     min_radius: Optional[int] = None,
                     max_radius: Optional[int] = None) -> List[Dict]:
    """
    Filter jobs by distance from base location
    Basic implementation - includes jobs in nearby cities within typical radius
    
    Args:
        jobs (List[Dict]): List of job dictionaries
        base_location (str): Base location to filter from
        min_radius (int, optional): Minimum radius in km
        max_radius (int, optional): Maximum radius in km
        
    Returns:
        List[Dict]: Filtered list of jobs
    """
    # Map of major cities to approximate distances (km) from common locations
    DISTANCE_MAP = {
        'brampton': {
            'mississauga': 15,
            'toronto': 30,
            'vaughan': 25,
            'woodbridge': 20,
            'etobicoke': 20,
            'markham': 35,
            'richmond hill': 35,
            'oakville': 35,
            'milton': 30
        },
        'mississauga': {
            'brampton': 15,
            'toronto': 25,
            'vaughan': 30,
            'woodbridge': 25,
            'etobicoke': 15,
            'oakville': 20,
            'milton': 25
        },
        'toronto': {
            'mississauga': 25,
            'brampton': 30,
            'vaughan': 25,
            'woodbridge': 25,
            'etobicoke': 15,
            'markham': 25,
            'richmond hill': 30
        }
    }
    
    # Normalize location names
    base_location = base_location.lower().split(',')[0].strip()
    
    # Get distance map for base location
    distances = DISTANCE_MAP.get(base_location, {})
    if not distances:
        logger.warning(f"No distance data for {base_location}, skipping radius filter")
        return jobs
        
    filtered = []
    for job in jobs:
        job_location = job.get('location', '').lower()
        
        # Extract city from job location
        for city in distances.keys():
            if city in job_location:
                distance = distances[city]
                
                # Check if within radius bounds
                if min_radius is not None and distance < min_radius:
                    continue
                if max_radius is not None and distance > max_radius:
                    continue
                    
                filtered.append(job)
                break
        else:
            # Include if no specific location (might be remote)
            if 'remote' in job_location or not any(city in job_location for city in distances):
                filtered.append(job)
                
    return filtered 