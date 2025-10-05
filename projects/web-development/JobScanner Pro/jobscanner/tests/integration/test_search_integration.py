"""
Integration tests for combined search functionality.
"""

import pytest
from core.search import JobSearch
from utils.filters import filter_jobs, deduplicate_jobs

def test_search_integration(test_config):
    """Test full search integration with all scrapers"""
    # Initialize search with test config
    search = JobSearch(test_config)
    
    # Perform search
    results = search.search(
        query="graphic designer",
        location="Brampton, ON",
        radius=25,
        gigs_only=False,
        new_only=False
    )
    
    # Verify results structure
    assert isinstance(results, list)
    for job in results:
        assert isinstance(job, dict)
        assert all(key in job for key in ["title", "company", "location", "url", "type"])
    
    # Verify no duplicates
    urls = [job["url"] for job in results]
    assert len(urls) == len(set(urls))

def test_search_with_filters(test_config):
    """Test search with various filters"""
    search = JobSearch(test_config)
    
    # Test gigs only
    gig_results = search.search(
        query="photographer",
        location="Brampton, ON",
        gigs_only=True
    )
    assert all(job["type"] == "gig" for job in gig_results)
    
    # Test new only
    new_results = search.search(
        query="designer",
        location="Brampton, ON",
        new_only=True
    )
    assert all("posted_date" in job for job in new_results)

def test_search_export(test_config, tmp_path):
    """Test exporting search results"""
    search = JobSearch(test_config)
    
    # Get some results
    results = search.search(
        query="web developer",
        location="Brampton, ON"
    )
    
    # Test CSV export
    csv_file = tmp_path / "test_jobs.csv"
    search.export_results(results, str(csv_file), format="csv")
    assert csv_file.exists()
    
    # Test JSON export
    json_file = tmp_path / "test_jobs.json"
    search.export_results(results, str(json_file), format="json")
    assert json_file.exists()

def test_search_error_handling(test_config):
    """Test search error handling"""
    search = JobSearch(test_config)
    
    # Test with invalid location
    results = search.search(
        query="test",
        location="Invalid Location"
    )
    assert isinstance(results, list)  # Should return empty list, not error
    
    # Test with empty query
    results = search.search(
        query="",
        location="Brampton, ON"
    )
    assert isinstance(results, list)
    
    # Test with all platforms disabled
    test_config["search"]["platforms"] = {
        "indeed": False,
        "jobbank": False,
        "craigslist": False,
        "kijiji": False
    }
    search = JobSearch(test_config)
    results = search.search(
        query="test",
        location="Brampton, ON"
    )
    assert results == [] 