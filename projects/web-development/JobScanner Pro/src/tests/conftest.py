"""
Pytest configuration and shared fixtures.
"""

import pytest
import yaml
from pathlib import Path

@pytest.fixture
def test_config():
    """Provide test configuration"""
    return {
        "user": {
            "name": "Test User",
            "email": "test@example.com",
            "location": "Brampton, ON",
            "resume_path": "./assets/test_resume.pdf",
            "portfolio_url": "https://example.com/portfolio"
        },
        "search": {
            "default_radius": 25,
            "refresh_interval": 60,
            "platforms": {
                "indeed": True,
                "jobbank": True,
                "craigslist": True,
                "kijiji": True
            }
        },
        "logging": {
            "level": "DEBUG",
            "file": "outputs/test_jobscanner.log"
        }
    }

@pytest.fixture
def mock_response():
    """Mock response class for testing scrapers"""
    class MockResponse:
        def __init__(self, text, status_code=200):
            self.text = text
            self.status_code = status_code
        
        def raise_for_status(self):
            if self.status_code != 200:
                raise Exception(f"Status code: {self.status_code}")
    
    return MockResponse

@pytest.fixture
def sample_job_data():
    """Sample job data for testing"""
    return {
        "title": "Test Job",
        "company": "Test Company",
        "location": "Brampton, ON",
        "description": "This is a test job description",
        "url": "https://example.com/job/123",
        "type": "job",
        "salary": "$50,000 - $60,000",
        "posted_date": "2024-01-01"
    }

@pytest.fixture
def sample_gig_data():
    """Sample gig data for testing"""
    return {
        "title": "Test Gig",
        "company": "Independent / Gig",
        "location": "Toronto, ON",
        "description": "This is a test gig description",
        "url": "https://example.com/gig/456",
        "type": "gig",
        "salary": "$50/hour",
        "posted_date": "2024-01-01"
    } 