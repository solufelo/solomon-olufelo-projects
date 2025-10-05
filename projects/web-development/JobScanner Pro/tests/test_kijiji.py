"""
Tests for Kijiji scraper implementation.
"""

import pytest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
from jobscanner.scrapers.kijiji import KijijiScraper

@pytest.fixture
def mock_html():
    """Mock HTML response from Kijiji"""
    return """
    <div class="search-results">
        <div class="search-item">
            <a href="/job/123" class="title">Senior Graphic Designer</a>
            <div class="location">Brampton, ON</div>
            <div class="price">$30-40 per hour</div>
            <span class="date-posted">< 24 hours ago</span>
            <div class="business">Creative Agency Ltd.</div>
            <div class="description">
                Looking for an experienced graphic designer...
            </div>
        </div>
        <div class="search-item">
            <a href="/services/456" class="title">Freelance Web Designer</a>
            <div class="location">Mississauga, ON</div>
            <div class="price">$500 flat rate</div>
            <span class="date-posted">yesterday</span>
            <div class="description">
                Available for web design projects...
            </div>
        </div>
        <div class="search-item">
            <a href="/job/789" class="title">UI/UX Designer</a>
            <div class="location">Greater Toronto Area, ON</div>
            <span class="date-posted">15/03/2024</span>
            <div class="business">Tech Solutions Inc.</div>
            <div class="description">
                Looking for a talented UI/UX designer...
            </div>
        </div>
    </div>
    """

@pytest.fixture
def mock_session(mock_html):
    """Mock requests session"""
    with patch('requests.Session') as mock:
        session = mock.return_value
        response = MagicMock()
        response.text = mock_html
        response.status_code = 200
        session.get.return_value = response
        yield mock

def test_kijiji_scraper_initialization():
    """Test KijijiScraper initialization"""
    scraper = KijijiScraper()
    assert scraper.BASE_URL == 'https://www.kijiji.ca'
    assert scraper.JOBS_URL == 'https://www.kijiji.ca/b-jobs'
    assert scraper.SERVICES_URL == 'https://www.kijiji.ca/b-services'
    
    # Verify categories are set up
    assert 'art-media-design' in scraper.JOB_CATEGORIES
    assert 'artistic' in scraper.SERVICE_CATEGORIES
    
    # Verify session configuration
    assert isinstance(scraper.session, requests.Session)
    assert 'User-Agent' in scraper.session.headers
    assert 'Accept-Language' in scraper.session.headers

def test_get_location_id():
    """Test location ID mapping"""
    scraper = KijijiScraper()
    
    # Test known locations
    assert scraper._get_location_id("Brampton") == "1700272"
    assert scraper._get_location_id("Toronto, ON") == "1700273"
    assert scraper._get_location_id("Mississauga") == "1700277"
    
    # Test case insensitivity
    assert scraper._get_location_id("BRAMPTON") == "1700272"
    assert scraper._get_location_id("brampton, ontario") == "1700272"
    
    # Test default fallback
    assert scraper._get_location_id("Unknown City") == "1700272"

def test_search_jobs_section(mock_session):
    """Test searching jobs section"""
    scraper = KijijiScraper()
    jobs = scraper._search_section(
        scraper.JOBS_URL,
        "designer",
        "1700272",
        {"art-media-design": "c45"},
        "job"
    )
    
    assert len(jobs) == 3
    
    # Verify first job
    assert jobs[0]['title'] == 'Senior Graphic Designer'
    assert jobs[0]['location'] == 'Brampton, ON'
    assert jobs[0]['type'] == 'job'
    assert jobs[0]['salary'] == '$30-40 per hour'
    assert jobs[0]['company'] == 'Creative Agency Ltd.'
    assert jobs[0]['url'] == 'https://www.kijiji.ca/job/123'
    assert 'description' in jobs[0]
    
    # Verify gig posting
    assert jobs[1]['title'] == 'Freelance Web Designer'
    assert jobs[1]['type'] == 'job'
    assert jobs[1]['salary'] == '$500 flat rate'
    assert jobs[1]['company'] == 'See posting for details'

def test_search_with_radius(mock_session):
    """Test searching with radius parameter"""
    scraper = KijijiScraper()
    scraper.search("designer", "Brampton", radius=50)
    
    # Verify radius was included in request
    args, kwargs = mock_session.return_value.get.call_args
    assert kwargs['params']['radius'] == 50

def test_search_with_large_radius(mock_session):
    """Test radius is capped at 100km"""
    scraper = KijijiScraper()
    scraper.search("designer", "Brampton", radius=150)
    
    # Verify radius was capped at 100
    args, kwargs = mock_session.return_value.get.call_args
    assert kwargs['params']['radius'] == 100

def test_parse_date():
    """Test date parsing"""
    scraper = KijijiScraper()
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    # Test relative dates
    assert scraper._parse_date("< 24 hours ago") == today.strftime("%Y-%m-%d")
    assert scraper._parse_date("yesterday") == (today - timedelta(days=1)).strftime("%Y-%m-%d")
    
    # Test absolute date
    assert scraper._parse_date("15/03/2024") == "2024-03-15"
    
    # Test invalid date
    assert scraper._parse_date("invalid date") is None

@patch('time.sleep')  # Mock sleep to speed up tests
def test_rate_limiting(mock_sleep, mock_session):
    """Test rate limiting behavior"""
    scraper = KijijiScraper()
    scraper.search("designer", "Toronto")
    
    # Verify delays were added between requests
    assert mock_sleep.call_count >= 1

def test_error_handling(mock_session):
    """Test error handling for failed requests"""
    mock_session.return_value.get.side_effect = requests.exceptions.RequestException(
        "Failed to fetch jobs"
    )
    
    scraper = KijijiScraper()
    jobs = scraper.search("designer", "Toronto")
    
    # Should handle error gracefully and return empty list
    assert len(jobs) == 0 