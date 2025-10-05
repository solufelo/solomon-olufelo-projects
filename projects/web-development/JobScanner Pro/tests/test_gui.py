import pytest
import tkinter as tk
from unittest.mock import Mock, patch, mock_open
from pathlib import Path

from jobscanner.gui.app_tkinter import JobScannerGUI

@pytest.fixture
def gui():
    """Create a GUI instance for testing"""
    root = tk.Tk()
    app = JobScannerGUI(root)
    yield app
    root.destroy()

def test_gui_initialization(gui):
    """Test that GUI initializes with correct default values"""
    # Check window title
    assert gui.root.title() == "JobScanner Pro"
    
    # Check default values
    assert gui.role_var.get() == ""
    assert gui.location_var.get() == "Brampton, ON"
    
    # Check source checkboxes
    assert all(var.get() for var in gui.sources.values())
    
    # Check config initialization
    assert gui.config["search"]["platforms"]["indeed"] is False
    assert gui.config["search"]["platforms"]["jobbank"] is True
    assert gui.config["search"]["platforms"]["craigslist"] is True
    assert gui.config["search"]["platforms"]["kijiji"] is True

def test_search_with_empty_role(gui):
    """Test search behavior with empty role field"""
    # Perform search with empty role
    gui.search()
    
    # Check that no results were added
    assert len(gui.results) == 0
    assert len(gui.tree.get_children()) == 0

@patch('jobscanner.gui.app_tkinter.JobSearch')
def test_successful_search(mock_job_search, gui):
    """Test successful search operation"""
    # Mock search results
    mock_results = [
        {
            "title": "Test Job",
            "company": "Test Company",
            "location": "Brampton, ON",
            "source": "jobbank",
            "url": "http://test.com"
        }
    ]
    
    # Configure mock
    mock_instance = Mock()
    mock_instance.search.return_value = mock_results
    mock_job_search.return_value = mock_instance
    
    # Set search parameters
    gui.role_var.set("Software Developer")
    gui.location_var.set("Brampton, ON")
    
    # Perform search
    gui.search()
    
    # Verify search was called with correct parameters
    mock_instance.search.assert_called_once_with(
        query="Software Developer",
        location="Brampton, ON"
    )
    
    # Check results were added to tree
    assert len(gui.results) == 1
    assert len(gui.tree.get_children()) == 1
    
    # Verify tree item values
    item = gui.tree.get_children()[0]
    values = gui.tree.item(item)["values"]
    assert values == ["Test Job", "Test Company", "Brampton, ON", "jobbank"]

@patch('jobscanner.gui.app_tkinter.webbrowser')
def test_open_job_link(mock_webbrowser, gui):
    """Test opening job URL on double-click"""
    # Add a mock result
    gui.results = [{"url": "http://test.com"}]
    gui.tree.insert("", tk.END, values=("Test Job", "Company", "Location", "Source"))
    
    # Simulate double-click on first item
    item = gui.tree.get_children()[0]
    gui.tree.selection_set(item)
    gui.open_job_link(None)  # Event object not needed for test
    
    # Verify browser was opened with correct URL
    mock_webbrowser.open.assert_called_once_with("http://test.com")

def test_clear_results(gui):
    """Test clearing search results"""
    # Add some mock results
    gui.results = [{"title": "Test"}]
    gui.tree.insert("", tk.END, values=("Test Job", "Company", "Location", "Source"))
    
    # Clear results
    gui.clear_results()
    
    # Verify everything was cleared
    assert len(gui.results) == 0
    assert len(gui.tree.get_children()) == 0

@patch('jobscanner.gui.app_tkinter.Path')
def test_export_csv(mock_path, gui, tmp_path):
    """Test exporting results to CSV"""
    # Mock results
    gui.results = [
        {
            "title": "Test Job",
            "company": "Test Company",
            "location": "Brampton, ON",
            "source": "jobbank",
            "url": "http://test.com"
        }
    ]
    
    # Configure mock path
    mock_output_dir = Mock()
    mock_output_file = Mock()
    mock_path.return_value = mock_output_dir
    mock_output_dir.__truediv__ = Mock(return_value=mock_output_file)
    
    # Export results
    m = mock_open()
    with patch('builtins.open', m):
        gui.export_csv()
        
        # Verify directory was created
        mock_output_dir.mkdir.assert_called_once_with(exist_ok=True)
        
        # Verify file was opened for writing
        m.assert_called_once_with(mock_output_file, "w", newline="")
        
        # Verify CSV was written
        handle = m()
        assert handle.write.call_count > 0

def test_source_selection(gui):
    """Test source selection checkboxes"""
    # Initially all sources should be enabled
    for var in gui.sources.values():
        assert var.get() is True
    
    # Disable a source
    gui.sources["jobbank"].set(False)
    
    # Verify config gets updated during search
    with patch('jobscanner.gui.app_tkinter.JobSearch') as mock_job_search:
        mock_instance = Mock()
        mock_job_search.return_value = mock_instance
        mock_instance.search.return_value = []
        
        gui.search()
        
        # Verify JobSearch was initialized with correct config
        mock_job_search.assert_called_once()
        config = mock_job_search.call_args[1]["config"]
        assert config["search"]["platforms"]["jobbank"] is False
        assert config["search"]["platforms"]["craigslist"] is True
        assert config["search"]["platforms"]["kijiji"] is True 