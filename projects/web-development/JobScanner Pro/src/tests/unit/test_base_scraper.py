"""
Unit tests for the base scraper class.
"""

import pytest
from scrapers.base import BaseScraper

class TestScraper(BaseScraper):
    """Test implementation of BaseScraper"""
    def search(self, query, location, radius=None):
        return []

def test_clean_text():
    """Test text cleaning functionality"""
    scraper = TestScraper()
    
    # Test cases
    assert scraper._clean_text("  test  ") == "test"
    assert scraper._clean_text("multiple    spaces") == "multiple spaces"
    assert scraper._clean_text("\n\nlines\n") == "lines"
    assert scraper._clean_text(None) == ""
    assert scraper._clean_text("") == ""

def test_validate_job(sample_job_data, sample_gig_data):
    """Test job validation"""
    scraper = TestScraper()
    
    # Valid jobs should pass
    assert scraper._validate_job(sample_job_data) is True
    assert scraper._validate_job(sample_gig_data) is True
    
    # Test missing required fields
    invalid_job = sample_job_data.copy()
    for field in ["title", "company", "location", "url", "type"]:
        invalid_job = sample_job_data.copy()
        del invalid_job[field]
        assert scraper._validate_job(invalid_job) is False
    
    # Test invalid job type
    invalid_job = sample_job_data.copy()
    invalid_job["type"] = "invalid"
    assert scraper._validate_job(invalid_job) is False

def test_abstract_search():
    """Test that BaseScraper cannot be instantiated directly"""
    with pytest.raises(TypeError):
        BaseScraper() 