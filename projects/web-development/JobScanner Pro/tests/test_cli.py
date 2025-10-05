"""
Tests for the CLI interface.
"""

import pytest
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path
import json
import yaml
from io import StringIO

from jobscanner.main import setup_argparse, load_config, main

@pytest.fixture
def mock_config():
    """Create a mock configuration"""
    return {
        "search": {
            "default_radius": 25,
            "platforms": {
                "indeed": True,
                "jobbank": True,
                "craigslist": True,
                "kijiji": True
            }
        },
        "logging": {
            "level": "INFO",
            "file": "outputs/jobscanner.log"
        }
    }

@pytest.fixture
def sample_jobs():
    """Create sample job listings for testing"""
    return [
        {
            "title": "Senior Designer",
            "company": "Creative Co",
            "location": "Toronto, ON",
            "type": "job",
            "source": "indeed",
            "url": "https://example.com/job1",
            "posted_date": "2024-03-15",
            "salary": "$80,000 - $100,000"
        },
        {
            "title": "Photographer",
            "company": "Freelance",
            "location": "Brampton, ON",
            "type": "gig",
            "source": "kijiji",
            "url": "https://example.com/job2",
            "posted_date": "2024-03-14"
        },
        {
            "title": "Art Director",
            "company": "Agency Inc",
            "location": "Mississauga, ON",
            "type": "job",
            "source": "jobbank",
            "url": "https://example.com/job3",
            "posted_date": "2024-03-13",
            "salary": "$90,000/year"
        }
    ]

def test_argument_parsing():
    """Test command line argument parsing"""
    parser = setup_argparse()
    
    # Test basic query
    args = parser.parse_args(["graphic designer"])
    assert args.query == "graphic designer"
    assert args.location == "Brampton, ON"  # Default value
    
    # Test with location and radius
    args = parser.parse_args([
        "developer",
        "--location", "Toronto, ON",
        "--radius", "30"
    ])
    assert args.query == "developer"
    assert args.location == "Toronto, ON"
    assert args.radius == 30
    
    # Test with filters
    args = parser.parse_args([
        "photographer",
        "--gigs-only",
        "--new-only",
        "--source", "kijiji"
    ])
    assert args.gigs_only is True
    assert args.new_only is True
    assert args.source == "kijiji"
    
    # Test with export and sort
    args = parser.parse_args([
        "artist",
        "--export", "json",
        "--sort", "date",
        "--verbose"
    ])
    assert args.export == "json"
    assert args.sort == "date"
    assert args.verbose is True

@patch("builtins.open")
def test_load_config_success(mock_open, mock_config):
    """Test successful config loading"""
    mock_open.return_value.__enter__.return_value = StringIO(
        yaml.dump(mock_config)
    )
    
    config = load_config()
    assert config["search"]["default_radius"] == 25
    assert all(config["search"]["platforms"].values())
    assert config["logging"]["level"] == "INFO"

@patch("builtins.open")
def test_load_config_file_not_found(mock_open):
    """Test config loading when file not found"""
    mock_open.side_effect = FileNotFoundError()
    
    with pytest.raises(SystemExit):
        load_config()

@patch("builtins.open")
def test_load_config_invalid_yaml(mock_open):
    """Test config loading with invalid YAML"""
    mock_open.return_value.__enter__.return_value = StringIO("invalid: yaml: :")
    
    with pytest.raises(SystemExit):
        load_config()

@pytest.mark.integration
def test_cli_export_json(sample_jobs, tmp_path, mock_config):
    """Test exporting results to JSON"""
    # Create mock search object
    mock_search = MagicMock()
    mock_search.search.return_value = sample_jobs
    
    # Setup test output directory
    output_dir = tmp_path / "outputs"
    output_dir.mkdir()
    output_file = output_dir / "jobs.json"
    
    # Run CLI with export
    with patch("jobscanner.main.JobSearch", return_value=mock_search), \
         patch("jobscanner.main.load_config", return_value=mock_config), \
         patch.object(sys, "argv", ["jobscanner", "test query", "--export", "json"]):
        main()
        
        # Verify JSON output
        assert output_file.exists()
        with open(output_file) as f:
            exported_jobs = json.load(f)
            assert len(exported_jobs) == len(sample_jobs)
            assert exported_jobs[0]["title"] == sample_jobs[0]["title"]

@pytest.mark.integration
def test_cli_source_filter(sample_jobs, mock_config):
    """Test filtering results by source"""
    # Create mock search object
    mock_search = MagicMock()
    mock_search.search.return_value = sample_jobs
    
    # Run CLI with source filter
    with patch("jobscanner.main.JobSearch", return_value=mock_search), \
         patch("jobscanner.main.load_config", return_value=mock_config), \
         patch.object(sys, "argv", ["jobscanner", "test query", "--source", "indeed"]):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            
            # Verify only indeed jobs are shown
            assert "Senior Designer" in output  # indeed job
            assert "Photographer" not in output  # kijiji job
            assert "Art Director" not in output  # jobbank job

@pytest.mark.integration
def test_cli_error_handling(mock_config):
    """Test CLI error handling"""
    # Create mock search object that raises an exception
    mock_search = MagicMock()
    mock_search.search.side_effect = Exception("Test error")
    
    # Run CLI and check error handling
    with patch("jobscanner.main.JobSearch", return_value=mock_search), \
         patch("jobscanner.main.load_config", return_value=mock_config), \
         patch.object(sys, "argv", ["jobscanner", "test query"]):
        with pytest.raises(SystemExit):
            main()

def test_cli_keyboard_interrupt(mock_config):
    """Test handling of keyboard interrupt"""
    # Create mock search object that raises KeyboardInterrupt
    mock_search = MagicMock()
    mock_search.search.side_effect = KeyboardInterrupt()
    
    # Run CLI and check interrupt handling
    with patch("jobscanner.main.JobSearch", return_value=mock_search), \
         patch("jobscanner.main.load_config", return_value=mock_config), \
         patch.object(sys, "argv", ["jobscanner", "test query"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
            assert exc_info.value.code == 0  # Clean exit 