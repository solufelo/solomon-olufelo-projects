"""
Unit tests for the Indeed scraper.
"""

import pytest
from unittest.mock import patch, MagicMock
from scrapers.indeed import IndeedScraper

# Sample HTML response
SAMPLE_INDEED_HTML = """
<div class="job_seen_beacon">
    <h2 class="jobTitle">
        <a href="/job/123">Senior Graphic Designer</a>
    </h2>
    <span class="companyName">Creative Agency Inc</span>
    <div class="companyLocation">Brampton, ON</div>
    <div class="salary-snippet">$60,000 - $80,000 a year</div>
    <span class="date">3 days ago</span>
    <div class="job-snippet">Looking for a creative designer...</div>
</div>
"""

@pytest.fixture
def indeed_scraper():
    """Create an Indeed scraper instance"""
    return IndeedScraper()

def test_indeed_initialization(indeed_scraper):
    """Test Indeed scraper initialization"""
    assert isinstance(indeed_scraper, IndeedScraper)
    assert indeed_scraper.BASE_URL == "https://ca.indeed.com"
    assert indeed_scraper.SEARCH_URL == "https://ca.indeed.com/jobs"

@patch('requests.Session')
def test_indeed_search(mock_session, indeed_scraper, mock_response):
    """Test Indeed job search"""
    # Setup mock response
    mock_session_instance = MagicMock()
    mock_session_instance.get.return_value = mock_response(SAMPLE_INDEED_HTML)
    mock_session.return_value = mock_session_instance
    
    # Perform search
    jobs = indeed_scraper.search("graphic designer", "Brampton, ON", radius=25)
    
    # Verify request
    mock_session_instance.get.assert_called_with(
        indeed_scraper.SEARCH_URL,
        params={
            "q": "graphic designer",
            "l": "Brampton, ON",
            "radius": 25,
            "start": 0
        },
        timeout=30
    )
    
    # Verify response parsing
    assert len(jobs) == 1
    job = jobs[0]
    assert job["title"] == "Senior Graphic Designer"
    assert job["company"] == "Creative Agency Inc"
    assert job["location"] == "Brampton, ON"
    assert job["type"] == "job"
    assert job["salary"] == "$60,000 - $80,000 a year"
    assert "posted_date" in job
    assert job["description"] == "Looking for a creative designer..."

def test_indeed_parse_date(indeed_scraper):
    """Test Indeed date parsing"""
    # Test various date formats
    assert indeed_scraper._parse_date("Today")
    assert indeed_scraper._parse_date("Just posted")
    assert indeed_scraper._parse_date("3 days ago")
    
    # Test invalid dates
    assert indeed_scraper._parse_date("invalid date") is None
    assert indeed_scraper._parse_date("") is None
    assert indeed_scraper._parse_date(None) is None

@patch('requests.Session')
def test_indeed_error_handling(mock_session, indeed_scraper, mock_response):
    """Test Indeed error handling"""
    # Setup mock error response
    mock_session_instance = MagicMock()
    mock_session_instance.get.side_effect = Exception("Network error")
    mock_session.return_value = mock_session_instance
    
    # Verify error handling
    jobs = indeed_scraper.search("test", "test")
    assert jobs == []  # Should return empty list on error
    
    # Test invalid HTML
    mock_session_instance.get.side_effect = None
    mock_session_instance.get.return_value = mock_response("invalid html")
    jobs = indeed_scraper.search("test", "test")
    assert jobs == []  # Should handle invalid HTML gracefully 