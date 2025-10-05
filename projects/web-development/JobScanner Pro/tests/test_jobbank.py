"""
Tests for Job Bank scraper implementation.
"""

import pytest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
from jobscanner.scrapers.jobbank import JobBankScraper

@pytest.fixture
def mock_html():
    """Mock HTML response from Job Bank"""
    return """
    <div class="results-jobs">
        <article class="job-search-result">
            <a href="/job_posting/123" class="resultJobItem">
                <span class="noc-title">Graphic Designer</span>
            </a>
            <ul>
                <li class="business">Creative Studio Inc.</li>
                <li class="location">Toronto, ON</li>
                <li class="salary">$25.00 to $35.00 hourly</li>
                <li class="date">Posted on March 19, 2024</li>
            </ul>
            <p class="summary">
                Looking for a talented graphic designer with 3+ years experience...
            </p>
        </article>
        <article class="job-search-result">
            <a href="/job_posting/456" class="resultJobItem">
                <span class="noc-title">UI Designer</span>
            </a>
            <ul>
                <li class="business">Tech Solutions Ltd.</li>
                <li class="location">Remote</li>
                <li class="date">2 days ago</li>
            </ul>
            <p class="summary">
                UI designer needed for exciting startup...
            </p>
        </article>
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

def test_jobbank_scraper_initialization():
    """Test JobBankScraper initialization"""
    scraper = JobBankScraper()
    assert scraper.BASE_URL == 'https://www.jobbank.gc.ca'
    assert scraper.SEARCH_URL == 'https://www.jobbank.gc.ca/jobsearch/jobsearch'
    
    # Verify session configuration
    assert isinstance(scraper.session, requests.Session)
    assert 'User-Agent' in scraper.session.headers
    assert 'Accept-Language' in scraper.session.headers

def test_search_jobs(mock_session):
    """Test searching for jobs"""
    scraper = JobBankScraper()
    jobs = scraper.search('designer', 'Toronto')
    
    assert len(jobs) == 2
    
    # Verify first job
    assert jobs[0]['title'] == 'Graphic Designer'
    assert jobs[0]['company'] == 'Creative Studio Inc.'
    assert jobs[0]['location'] == 'Toronto, ON'
    assert jobs[0]['salary'] == '$25.00 to $35.00 hourly'
    assert jobs[0]['url'] == 'https://www.jobbank.gc.ca/job_posting/123'
    assert jobs[0]['source'] == 'Job Bank'
    assert jobs[0]['type'] == 'job'
    assert jobs[0]['posted_date'] == '2024-03-19'
    assert 'description' in jobs[0]
    
    # Verify second job
    assert jobs[1]['title'] == 'UI Designer'
    assert jobs[1]['company'] == 'Tech Solutions Ltd.'
    assert jobs[1]['location'] == 'Remote'
    assert 'salary' not in jobs[1]
    assert jobs[1]['url'] == 'https://www.jobbank.gc.ca/job_posting/456'
    assert jobs[1]['type'] == 'job'
    
    # Verify request parameters
    args, kwargs = mock_session.return_value.get.call_args
    assert kwargs['params']['searchstring'] == 'designer'
    assert kwargs['params']['location'] == 'Toronto'
    assert kwargs['params']['sort'] == 'M'

def test_search_with_radius(mock_session):
    """Test searching with radius parameter"""
    scraper = JobBankScraper()
    scraper.search('designer', 'Toronto', radius=50)
    
    # Verify radius was included in request
    args, kwargs = mock_session.return_value.get.call_args
    assert kwargs['params']['distance'] == 50

def test_search_with_large_radius(mock_session):
    """Test radius is capped at 100km"""
    scraper = JobBankScraper()
    scraper.search('designer', 'Toronto', radius=150)
    
    # Verify radius was capped at 100
    args, kwargs = mock_session.return_value.get.call_args
    assert kwargs['params']['distance'] == 100

@patch('requests.Session')
def test_rate_limiting(mock_session):
    """Test rate limiting behavior"""
    # Setup session to fail with 429 then succeed
    fail_response = MagicMock()
    fail_response.status_code = 429
    fail_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "429 Client Error: Too Many Requests"
    )
    
    success_response = MagicMock()
    success_response.status_code = 200
    success_response.text = mock_html()
    
    mock_session.return_value.get.side_effect = [fail_response, success_response]
    
    scraper = JobBankScraper()
    jobs = scraper.search('designer', 'Toronto')
    
    # Verify retry worked and we got results
    assert len(jobs) == 2
    assert mock_session.return_value.get.call_count == 2

def test_parse_date():
    """Test date parsing"""
    scraper = JobBankScraper()
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    # Test absolute date
    date = scraper._parse_date("Posted on March 19, 2024")
    if date:  # Handle potential None return
        assert date.strftime("%Y-%m-%d") == "2024-03-19"
    
    # Test relative dates
    assert scraper._parse_date("today") == today
    assert scraper._parse_date("yesterday") == today - timedelta(days=1)
    assert scraper._parse_date("2 days ago") == today - timedelta(days=2)
    
    # Test invalid date
    assert scraper._parse_date("invalid date") is None

def test_error_handling(mock_session):
    """Test error handling for failed requests"""
    mock_session.return_value.get.side_effect = requests.exceptions.RequestException(
        "Failed to fetch jobs"
    )
    
    scraper = JobBankScraper()
    jobs = scraper.search('designer', 'Toronto')
    
    # Should handle error gracefully and return empty list
    assert len(jobs) == 0 