"""
Tests for Indeed API integration.
"""

import os
from datetime import datetime, timedelta
import pytest
from unittest.mock import patch, MagicMock
from jobscanner.scrapers.indeed import IndeedScraper

@pytest.fixture
def mock_env_vars():
    """Mock environment variables for testing"""
    with patch.dict(os.environ, {
        'INDEED_CLIENT_ID': 'test_client_id',
        'INDEED_CLIENT_SECRET': 'test_client_secret',
        'INDEED_API_BASE_URL': 'https://test.indeed.com/oauth/v2',
        'INDEED_SEARCH_API_URL': 'https://test.indeed.com/ads/search/v1'
    }):
        yield

@pytest.fixture
def mock_token_response():
    """Mock OAuth token response"""
    return {
        'access_token': 'test_access_token',
        'expires_in': 3600
    }

@pytest.fixture
def mock_search_response():
    """Mock API search response"""
    return {
        'results': [
            {
                'jobtitle': 'Senior Designer',
                'company': 'Creative Co',
                'formattedLocation': 'Toronto, ON',
                'url': 'https://example.com/job1',
                'snippet': 'Job description here',
                'date': '2024-03-19T12:00:00Z',
                'salary': '$80,000 - $100,000 per year'
            },
            {
                'jobtitle': 'UI/UX Designer',
                'company': 'Tech Corp',
                'formattedLocation': 'Remote',
                'url': 'https://example.com/job2',
                'snippet': 'Another job description',
                'date': '2024-03-18T14:30:00Z'
            }
        ]
    }

def test_indeed_scraper_initialization(mock_env_vars):
    """Test IndeedScraper initialization with environment variables"""
    scraper = IndeedScraper()
    assert scraper.client_id == 'test_client_id'
    assert scraper.client_secret == 'test_client_secret'
    assert scraper.API_BASE_URL == 'https://test.indeed.com/oauth/v2'
    assert scraper.SEARCH_API_URL == 'https://test.indeed.com/ads/search/v1'

def test_indeed_scraper_missing_credentials():
    """Test IndeedScraper initialization with missing credentials"""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError) as exc_info:
            IndeedScraper()
        assert "Indeed API credentials not found" in str(exc_info.value)

@patch('requests.Session')
def test_get_access_token(mock_session, mock_env_vars, mock_token_response):
    """Test getting OAuth access token"""
    # Setup mock response
    mock_response = MagicMock()
    mock_response.json.return_value = mock_token_response
    mock_session.return_value.post.return_value = mock_response
    
    scraper = IndeedScraper()
    token = scraper._get_access_token()
    
    assert token == 'test_access_token'
    assert scraper.access_token == 'test_access_token'
    assert scraper.token_expires_at is not None
    
    # Verify request
    mock_session.return_value.post.assert_called_with(
        'https://test.indeed.com/oauth/v2/tokens',
        auth=('test_client_id', 'test_client_secret'),
        data={'grant_type': 'client_credentials'},
        timeout=30
    )

@patch('requests.Session')
def test_search_jobs(mock_session, mock_env_vars, mock_token_response, mock_search_response):
    """Test searching for jobs"""
    # Setup mock responses
    token_resp = MagicMock()
    token_resp.json.return_value = mock_token_response
    
    search_resp = MagicMock()
    search_resp.json.return_value = mock_search_response
    
    mock_session.return_value.post.return_value = token_resp
    mock_session.return_value.get.return_value = search_resp
    
    # Perform search
    scraper = IndeedScraper()
    jobs = scraper.search('designer', 'Toronto')
    
    assert len(jobs) == 2
    
    # Verify first job
    assert jobs[0]['title'] == 'Senior Designer'
    assert jobs[0]['company'] == 'Creative Co'
    assert jobs[0]['location'] == 'Toronto, ON'
    assert jobs[0]['salary'] == '$80,000 - $100,000 per year'
    assert jobs[0]['source'] == 'Indeed'
    assert jobs[0]['type'] == 'job'
    assert jobs[0]['posted_date'] == '2024-03-19'
    assert jobs[0]['description'] == 'Job description here'
    
    # Verify second job
    assert jobs[1]['title'] == 'UI/UX Designer'
    assert jobs[1]['location'] == 'Remote'
    assert 'salary' not in jobs[1]
    
    # Verify API request
    mock_session.return_value.get.assert_called_with(
        'https://test.indeed.com/ads/search/v1',
        params={
            'q': 'designer',
            'l': 'Toronto',
            'start': 0,
            'limit': 25,
            'fromage': 30,
            'sort': 'date',
            'co': 'ca'
        },
        headers={'Authorization': 'Bearer test_access_token'},
        timeout=30
    )

@patch('requests.Session')
def test_search_with_radius(mock_session, mock_env_vars, mock_token_response, mock_search_response):
    """Test searching with radius parameter"""
    # Setup mock responses
    token_resp = MagicMock()
    token_resp.json.return_value = mock_token_response
    
    search_resp = MagicMock()
    search_resp.json.return_value = mock_search_response
    
    mock_session.return_value.post.return_value = token_resp
    mock_session.return_value.get.return_value = search_resp
    
    # Perform search with radius
    scraper = IndeedScraper()
    scraper.search('designer', 'Toronto', radius=50)
    
    # Verify radius was included in API call
    args, kwargs = mock_session.return_value.get.call_args
    assert kwargs['params']['radius'] == 50

def test_parse_date():
    """Test date parsing"""
    scraper = IndeedScraper()
    
    # Test valid date
    assert scraper._parse_date('2024-03-19T12:00:00Z') == '2024-03-19'
    
    # Test invalid date
    assert scraper._parse_date('invalid-date') is None 