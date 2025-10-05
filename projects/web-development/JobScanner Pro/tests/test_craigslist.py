"""
Tests for Craigslist scraper implementation.
"""

import pytest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from datetime import datetime
import requests
from jobscanner.scrapers.craigslist import CraigslistScraper

@pytest.fixture
def mock_html():
    """Mock HTML response from Craigslist"""
    return """
    <ul class="rows">
        <li class="result-row">
            <a href="/job/123" class="result-title">Senior Graphic Designer</a>
            <span class="result-hood">(Brampton)</span>
            <time class="result-date" datetime="2024-03-19T10:00:00">Mar 19</time>
            <span class="result-price">$30/hr</span>
        </li>
        <li class="result-row">
            <a href="/gig/456" class="result-title">Freelance UI Designer</a>
            <span class="result-hood">(Mississauga)</span>
            <time class="result-date" datetime="2024-03-18T15:30:00">Mar 18</time>
            <span class="result-price">$500</span>
        </li>
        <li class="result-row">
            <a href="/job/789" class="result-title">Web Designer</a>
            <time class="result-date" datetime="2024-03-17T09:00:00">Mar 17</time>
        </li>
    </ul>
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

def test_craigslist_scraper_initialization():
    """Test CraigslistScraper initialization"""
    scraper = CraigslistScraper()
    assert scraper.BASE_URL == 'https://toronto.craigslist.org'
    assert scraper.JOBS_URL == 'https://toronto.craigslist.org/search/jjj'
    assert scraper.GIGS_URL == 'https://toronto.craigslist.org/search/ggg'
    
    # Verify categories are set up
    assert 'art' in scraper.JOB_CATEGORIES
    assert 'creative' in scraper.GIG_CATEGORIES
    
    # Verify session configuration
    assert isinstance(scraper.session, requests.Session)
    assert 'User-Agent' in scraper.session.headers
    assert 'Accept-Language' in scraper.session.headers

def test_search_jobs_section(mock_session):
    """Test searching jobs section"""
    scraper = CraigslistScraper()
    jobs = scraper._search_section(
        scraper.JOBS_URL,
        "designer",
        {"art": "art"},
        "job"
    )
    
    assert len(jobs) == 3
    
    # Verify first job
    assert jobs[0]['title'] == 'Senior Graphic Designer'
    assert jobs[0]['location'] == 'Brampton'
    assert jobs[0]['type'] == 'job'
    assert jobs[0]['salary'] == '$30/hr'
    assert jobs[0]['posted_date'] == '2024-03-19'
    assert jobs[0]['url'] == '/job/123'
    
    # Verify job without salary
    assert jobs[2]['title'] == 'Web Designer'
    assert 'salary' not in jobs[2]
    assert jobs[2]['location'] == 'Toronto, ON'  # Default when no location

def test_search_with_location_filter(mock_session):
    """Test location filtering"""
    scraper = CraigslistScraper()
    jobs = scraper.search("designer", "Brampton", radius=20)
    
    # Should only include Brampton and nearby cities
    locations = [job['location'].lower() for job in jobs]
    assert any('brampton' in loc for loc in locations)
    assert any('mississauga' in loc for loc in locations)

def test_parse_date():
    """Test date parsing"""
    scraper = CraigslistScraper()
    
    # Test ISO format date
    assert scraper._parse_date("2024-03-19T10:00:00") == "2024-03-19"
    
    # Test invalid date
    assert scraper._parse_date("invalid-date") is None

def test_filter_by_distance():
    """Test distance-based filtering"""
    scraper = CraigslistScraper()
    test_jobs = [
        {"location": "Brampton", "title": "Job 1"},
        {"location": "Toronto, ON", "title": "Job 2"},
        {"location": "Mississauga", "title": "Job 3"},
        {"location": "Ottawa", "title": "Job 4"},
        {"location": "Vaughan", "title": "Job 5"}
    ]
    
    filtered = scraper._filter_by_distance(test_jobs, 20)
    
    # Should include Brampton, Mississauga, Vaughan, and default Toronto
    assert len(filtered) == 4
    assert any(job["location"] == "Brampton" for job in filtered)
    assert any(job["location"] == "Mississauga" for job in filtered)
    assert any(job["location"] == "Vaughan" for job in filtered)
    assert any(job["location"] == "Toronto, ON" for job in filtered)
    
    # Should not include Ottawa
    assert not any(job["location"] == "Ottawa" for job in filtered)

@patch('time.sleep')  # Mock sleep to speed up tests
def test_rate_limiting(mock_sleep, mock_session):
    """Test rate limiting behavior"""
    scraper = CraigslistScraper()
    scraper.search("designer", "Toronto")
    
    # Verify delays were added between requests
    assert mock_sleep.call_count >= 1

def test_error_handling(mock_session):
    """Test error handling for failed requests"""
    mock_session.return_value.get.side_effect = requests.exceptions.RequestException(
        "Failed to fetch jobs"
    )
    
    scraper = CraigslistScraper()
    jobs = scraper.search("designer", "Toronto")
    
    # Should handle error gracefully and return empty list
    assert len(jobs) == 0 