"""
Unit tests for job filtering utilities.
"""

import pytest
from datetime import datetime, timedelta
from utils.filters import filter_jobs, deduplicate_jobs

@pytest.fixture
def test_jobs():
    """Create a list of test jobs"""
    today = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    last_week = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    
    return [
        {
            "title": "Graphic Designer",
            "company": "Company A",
            "location": "Brampton, ON",
            "url": "https://example.com/job1",
            "type": "job",
            "posted_date": today
        },
        {
            "title": "Photographer",
            "company": "Independent",
            "location": "Toronto, ON",
            "url": "https://example.com/job2",
            "type": "gig",
            "posted_date": yesterday
        },
        {
            "title": "Web Developer",
            "company": "Company B",
            "location": "Mississauga, ON",
            "url": "https://example.com/job3",
            "type": "job",
            "posted_date": last_week
        },
        # Duplicate job with different URL
        {
            "title": "Graphic Designer",
            "company": "Company A",
            "location": "Brampton, ON",
            "url": "https://example.com/job4",
            "type": "job",
            "posted_date": today
        }
    ]

def test_filter_jobs_gigs_only(test_jobs):
    """Test filtering for gigs only"""
    filtered = filter_jobs(test_jobs, gigs_only=True)
    assert len(filtered) == 1
    assert filtered[0]["type"] == "gig"
    assert filtered[0]["title"] == "Photographer"

def test_filter_jobs_new_only(test_jobs):
    """Test filtering for new jobs only"""
    filtered = filter_jobs(test_jobs, new_only=True)
    today = datetime.now().strftime("%Y-%m-%d")
    
    assert len(filtered) == 2
    for job in filtered:
        assert job["posted_date"] == today

def test_filter_jobs_combined(test_jobs):
    """Test combining multiple filters"""
    filtered = filter_jobs(test_jobs, gigs_only=True, new_only=True)
    assert len(filtered) == 0  # No gigs from today in test data

def test_deduplicate_jobs(test_jobs):
    """Test job deduplication"""
    unique = deduplicate_jobs(test_jobs)
    
    # Should remove one duplicate job
    assert len(unique) == 3
    
    # Check URLs are unique
    urls = [job["url"] for job in unique]
    assert len(urls) == len(set(urls))

def test_empty_filters():
    """Test filtering empty job list"""
    empty_jobs = []
    assert filter_jobs(empty_jobs, gigs_only=True) == []
    assert filter_jobs(empty_jobs, new_only=True) == []
    assert deduplicate_jobs(empty_jobs) == []

def test_filter_jobs_no_date(test_jobs):
    """Test filtering jobs without dates"""
    jobs = test_jobs.copy()
    for job in jobs:
        del job["posted_date"]
    
    # Should not raise errors
    filtered = filter_jobs(jobs, new_only=True)
    assert filtered == []  # No jobs with dates 