#!/usr/bin/env python3
"""
Build script for creating JobScanner Pro executables
Fixed version with proper platform-specific syntax
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

def get_add_data_separator():
    """Get the correct separator for --add-data based on platform"""
    return ";" if sys.platform == "win32" else ":"

def create_gui_executable():
    """Create GUI executable using PyInstaller"""
    print("\n🚀 Building GUI executable...")
    
    sep = get_add_data_separator()
    
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window (GUI only)
        "--name=JobScannerPro-GUI",     # Executable name
        f"--add-data=jobscanner/config.yml{sep}jobscanner/", # Include config
        f"--add-data=config.yml{sep}.",      # Include root config
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
    
    # Add icon if available
    if os.path.exists("assets/icon.ico"):
        cmd.insert(-1, "--icon=assets/icon.ico")
    
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
    
    sep = get_add_data_separator()
    
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--console",                    # Keep console window for CLI
        "--name=JobScannerPro-CLI",     # Executable name
        f"--add-data=jobscanner/config.yml{sep}jobscanner/", # Include config
        f"--add-data=config.yml{sep}.",      # Include root config
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

def main():
    """Main build process"""
    print("🏗️  JobScanner Pro - Executable Builder (Fixed)")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("jobscanner"):
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)
    
    # Install dependencies
    install_pyinstaller()
    
    # Clean previous builds
    clean_build_dirs()
    
    # Create executables
    gui_success = create_gui_executable()
    cli_success = create_cli_executable()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Build Summary:")
    
    if gui_success:
        gui_ext = ".exe" if sys.platform == "win32" else ""
        gui_path = Path(f"dist/JobScannerPro-GUI{gui_ext}")
        print(f"✓ GUI Executable: {gui_path}")
    else:
        print("❌ GUI Executable: Failed")
    
    if cli_success:
        cli_ext = ".exe" if sys.platform == "win32" else ""
        cli_path = Path(f"dist/JobScannerPro-CLI{cli_ext}")
        print(f"✓ CLI Executable: {cli_path}")
    else:
        print("❌ CLI Executable: Failed")
    
    if gui_success or cli_success:
        print(f"\n📁 Executables saved to: {Path('dist').absolute()}")
        print("\n💡 Tips:")
        print("  • Test the executables on a clean system")
        print("  • GUI version doesn't require command line")
        print("  • CLI version: Use './JobScannerPro-CLI \"job title\" --location \"city\"'")
    
    print("\n🎉 Build process completed!")

if __name__ == "__main__":
    main() 