"""
Utility functions for filtering and deduplicating job listings.
"""

import logging
from datetime import datetime, timedelta
from difflib import SequenceMatcher

logger = logging.getLogger(__name__)

def filter_jobs(jobs, gigs_only=False, new_only=False):
    """
    Filter job listings based on criteria
    
    Args:
        jobs (list): List of job dictionaries
        gigs_only (bool): Only return gig postings
        new_only (bool): Only return postings from last 24 hours
        
    Returns:
        list: Filtered list of jobs
    """
    filtered = jobs.copy()
    
    if gigs_only:
        filtered = [job for job in filtered if job["type"] == "gig"]
        logger.debug(f"Filtered to {len(filtered)} gigs")
        
    if new_only:
        cutoff = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        filtered = [
            job for job in filtered 
            if "posted_date" in job and (
                parsed_date := _parse_date(job["posted_date"])
            ) and parsed_date >= cutoff - timedelta(days=1)
        ]
        logger.debug(f"Filtered to {len(filtered)} new postings")
        
    return filtered

def _parse_date(date_str):
    """Parse date string to datetime object"""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").replace(
            hour=0, minute=0, second=0, microsecond=0
        )
    except (ValueError, TypeError):
        logger.error(f"Failed to parse date: {date_str}")
        return None

def _text_similarity(text1, text2):
    """Calculate similarity ratio between two strings"""
    if not text1 or not text2:
        return 0
    return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()

def _is_duplicate(job, existing_job, similarity_threshold=0.85):
    """
    Check if two jobs are duplicates based on multiple criteria
    
    Args:
        job: New job listing to check
        existing_job: Previously seen job to compare against
        similarity_threshold: Minimum similarity ratio to consider as duplicate
        
    Returns:
        bool: True if jobs are likely duplicates
    """
    # Check exact URL match
    if job["url"] == existing_job["url"]:
        return True
        
    # Check title similarity
    title_similarity = _text_similarity(job["title"], existing_job["title"])
    if title_similarity > similarity_threshold:
        # If titles are very similar, check company
        company_similarity = _text_similarity(
            job.get("company", ""), 
            existing_job.get("company", "")
        )
        if company_similarity > similarity_threshold:
            logger.debug(
                f"Found duplicate: {job['title']} at {job.get('company', 'Unknown')}"
                f" (similarity: title={title_similarity:.2f}, company={company_similarity:.2f})"
            )
            return True
            
    return False

def deduplicate_jobs(jobs):
    """
    Remove duplicate job listings based on URL or content similarity
    
    Args:
        jobs (list): List of job dictionaries
        
    Returns:
        list: Deduplicated list of jobs
    """
    unique_jobs = []
    
    for job in jobs:
        # Check against all existing unique jobs
        is_duplicate = any(
            _is_duplicate(job, existing_job) 
            for existing_job in unique_jobs
        )
        
        if not is_duplicate:
            unique_jobs.append(job)
    
    duplicates_removed = len(jobs) - len(unique_jobs)
    logger.debug(f"Removed {duplicates_removed} duplicates")
    return unique_jobs 