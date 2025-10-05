"""
Tests for job filtering and deduplication utilities.
"""

import pytest
from datetime import datetime, timedelta
from jobscanner.utils.filters import filter_jobs, deduplicate_jobs

def test_filter_jobs_gigs_only():
    """Test filtering to show only gigs"""
    test_jobs = [
        {"title": "Job 1", "type": "job"},
        {"title": "Gig 1", "type": "gig"},
        {"title": "Job 2", "type": "job"},
        {"title": "Gig 2", "type": "gig"}
    ]
    
    filtered = filter_jobs(test_jobs, gigs_only=True)
    assert len(filtered) == 2
    assert all(job["type"] == "gig" for job in filtered)

def test_filter_jobs_new_only():
    """Test filtering to show only new jobs"""
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    old_date = today - timedelta(days=2)
    
    test_jobs = [
        {
            "title": "New Job 1",
            "posted_date": today.strftime("%Y-%m-%d")
        },
        {
            "title": "New Job 2",
            "posted_date": yesterday.strftime("%Y-%m-%d")
        },
        {
            "title": "Old Job",
            "posted_date": old_date.strftime("%Y-%m-%d")
        }
    ]
    
    filtered = filter_jobs(test_jobs, new_only=True)
    assert len(filtered) == 2
    assert all(
        datetime.strptime(job["posted_date"], "%Y-%m-%d") >= yesterday
        for job in filtered
    )

def test_filter_jobs_combined():
    """Test combining multiple filters"""
    today = datetime.now()
    old_date = today - timedelta(days=2)
    
    test_jobs = [
        {
            "title": "New Job",
            "type": "job",
            "posted_date": today.strftime("%Y-%m-%d")
        },
        {
            "title": "New Gig",
            "type": "gig",
            "posted_date": today.strftime("%Y-%m-%d")
        },
        {
            "title": "Old Job",
            "type": "job",
            "posted_date": old_date.strftime("%Y-%m-%d")
        },
        {
            "title": "Old Gig",
            "type": "gig",
            "posted_date": old_date.strftime("%Y-%m-%d")
        }
    ]
    
    filtered = filter_jobs(test_jobs, gigs_only=True, new_only=True)
    assert len(filtered) == 1
    assert filtered[0]["title"] == "New Gig"

def test_deduplicate_jobs_exact_url():
    """Test deduplication based on exact URL matches"""
    test_jobs = [
        {
            "title": "Designer",
            "company": "Company A",
            "url": "https://example.com/job1"
        },
        {
            "title": "Designer",
            "company": "Company A",
            "url": "https://example.com/job1"  # Duplicate URL
        },
        {
            "title": "Developer",
            "company": "Company B",
            "url": "https://example.com/job2"
        }
    ]
    
    unique = deduplicate_jobs(test_jobs)
    assert len(unique) == 2
    assert unique[0]["url"] != unique[1]["url"]

def test_deduplicate_jobs_similar_content():
    """Test deduplication based on similar titles and companies"""
    test_jobs = [
        {
            "title": "Senior Graphic Designer",
            "company": "Creative Studio",
            "url": "https://example.com/job1"
        },
        {
            "title": "Sr. Graphic Designer",  # Similar title
            "company": "Creative Studio",      # Same company
            "url": "https://example.com/job2"
        },
        {
            "title": "Web Developer",
            "company": "Tech Corp",
            "url": "https://example.com/job3"
        }
    ]
    
    unique = deduplicate_jobs(test_jobs)
    assert len(unique) == 2
    assert any(job["title"] == "Web Developer" for job in unique)

def test_deduplicate_jobs_missing_fields():
    """Test deduplication with missing optional fields"""
    test_jobs = [
        {
            "title": "Designer",
            "url": "https://example.com/job1"
        },
        {
            "title": "Designer",
            "company": None,
            "url": "https://example.com/job2"
        },
        {
            "title": "Different Job",
            "url": "https://example.com/job3"
        }
    ]
    
    unique = deduplicate_jobs(test_jobs)
    assert len(unique) == 2  # Should keep one designer job and the different job 