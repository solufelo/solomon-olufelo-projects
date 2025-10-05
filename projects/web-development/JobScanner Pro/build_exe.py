#!/usr/bin/env python3
"""
Build script for creating JobScanner Pro executables
Supports both CLI and GUI versions with optimized packaging
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("✓ PyInstaller already installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed successfully")

def clean_build_dirs():
    """Clean previous build directories"""
    dirs_to_clean = ["build", "dist", "__pycache__"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✓ Cleaned {dir_name} directory")

def create_gui_executable():
    """Create GUI executable using PyInstaller"""
    print("\n🚀 Building GUI executable...")
    
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window (GUI only)
        "--name=JobScannerPro-GUI",     # Executable name
        "--icon=assets/icon.ico",       # Icon (if available)
        "--add-data=jobscanner/config.yml;jobscanner/", # Include config
        "--add-data=config.yml;.",      # Include root config
        "--hidden-import=nltk",         # Ensure NLTK is included
        "--hidden-import=spacy",        # Ensure spaCy is included
        "--hidden-import=selenium",     # Ensure Selenium is included
        "--hidden-import=playwright",   # Ensure Playwright is included
        "--hidden-import=requests",     # Ensure requests is included
        "--hidden-import=beautifulsoup4", # Ensure BS4 is included
        "--hidden-import=pandas",       # Ensure pandas is included
        "--hidden-import=yaml",         # Ensure PyYAML is included
        "--collect-all=spacy",          # Collect all spaCy data
        "--collect-all=nltk",           # Collect all NLTK data
        "--collect-submodules=jobscanner", # Include all jobscanner modules
        "jobscanner/gui/app_tkinter.py" # Main GUI file
    ]
    
    # Remove icon parameter if file doesn't exist
    if not os.path.exists("assets/icon.ico"):
        cmd = [arg for arg in cmd if not arg.startswith("--icon")]
    
    try:
        subprocess.check_call(cmd)
        print("✓ GUI executable created successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating GUI executable: {e}")
        return False

def create_cli_executable():
    """Create CLI executable using PyInstaller"""
    print("\n🚀 Building CLI executable...")
    
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--console",                    # Keep console window for CLI
        "--name=JobScannerPro-CLI",     # Executable name
        "--add-data=jobscanner/config.yml;jobscanner/", # Include config
        "--add-data=config.yml;.",      # Include root config
        "--hidden-import=nltk",         # Ensure NLTK is included
        "--hidden-import=spacy",        # Ensure spaCy is included
        "--hidden-import=selenium",     # Ensure Selenium is included
        "--hidden-import=playwright",   # Ensure Playwright is included
        "--hidden-import=requests",     # Ensure requests is included
        "--hidden-import=beautifulsoup4", # Ensure BS4 is included
        "--hidden-import=pandas",       # Ensure pandas is included
        "--hidden-import=yaml",         # Ensure PyYAML is included
        "--hidden-import=rich",         # Ensure rich is included
        "--collect-all=spacy",          # Collect all spaCy data
        "--collect-all=nltk",           # Collect all NLTK data
        "--collect-submodules=jobscanner", # Include all jobscanner modules
        "jobscanner/main.py"            # Main CLI file
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✓ CLI executable created successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating CLI executable: {e}")
        return False

def download_nltk_data():
    """Download required NLTK data"""
    print("\n📦 Downloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        print("✓ NLTK data downloaded successfully")
    except Exception as e:
        print(f"⚠️  Warning: Could not download NLTK data: {e}")

def download_spacy_model():
    """Download required spaCy model"""
    print("\n📦 Downloading spaCy model...")
    try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        print("✓ spaCy model downloaded successfully")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Warning: Could not download spaCy model: {e}")

def main():
    """Main build process"""
    print("🏗️  JobScanner Pro - Executable Builder")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("jobscanner"):
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)
    
    # Install dependencies
    install_pyinstaller()
    download_nltk_data()
    download_spacy_model()
    
    # Clean previous builds
    clean_build_dirs()
    
    # Create executables
    gui_success = create_gui_executable()
    cli_success = create_cli_executable()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Build Summary:")
    
    if gui_success:
        gui_path = Path("dist/JobScannerPro-GUI.exe" if sys.platform == "win32" else "dist/JobScannerPro-GUI")
        print(f"✓ GUI Executable: {gui_path}")
    else:
        print("❌ GUI Executable: Failed")
    
    if cli_success:
        cli_path = Path("dist/JobScannerPro-CLI.exe" if sys.platform == "win32" else "dist/JobScannerPro-CLI")
        print(f"✓ CLI Executable: {cli_path}")
    else:
        print("❌ CLI Executable: Failed")
    
    if gui_success or cli_success:
        print(f"\n📁 Executables saved to: {Path('dist').absolute()}")
        print("\n💡 Tips:")
        print("  • Test the executables on a clean system")
        print("  • GUI version doesn't require command line")
        print("  • CLI version: Use 'JobScannerPro-CLI \"job title\" --location \"city\"'")
        
        # Create a simple batch/shell script for easy CLI usage
        if sys.platform == "win32":
            create_batch_script()
        else:
            create_shell_script()
    
    print("\n🎉 Build process completed!")

def create_batch_script():
    """Create a batch script for easy CLI usage on Windows"""
    batch_content = '''@echo off
echo JobScanner Pro - Quick Search
echo.
set /p job_title="Enter job title: "
set /p location="Enter location (default: Brampton, ON): "

if "%location%"=="" set location=Brampton, ON

echo.
echo Searching for "%job_title%" in "%location%"...
echo.

JobScannerPro-CLI.exe "%job_title%" --location "%location%" --verbose

pause
'''
    with open("dist/QuickSearch.bat", "w") as f:
        f.write(batch_content)
    print("✓ Created QuickSearch.bat for easy CLI usage")

def create_shell_script():
    """Create a shell script for easy CLI usage on Unix systems"""
    shell_content = '''#!/bin/bash
echo "JobScanner Pro - Quick Search"
echo
read -p "Enter job title: " job_title
read -p "Enter location (default: Brampton, ON): " location

if [ -z "$location" ]; then
    location="Brampton, ON"
fi

echo
echo "Searching for '$job_title' in '$location'..."
echo

./JobScannerPro-CLI "$job_title" --location "$location" --verbose

read -p "Press Enter to continue..."
'''
    with open("dist/quick_search.sh", "w") as f:
        f.write(shell_content)
    os.chmod("dist/quick_search.sh", 0o755)
    print("✓ Created quick_search.sh for easy CLI usage")

if __name__ == "__main__":
    main() 