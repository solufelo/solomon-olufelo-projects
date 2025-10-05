#!/usr/bin/env python3
"""
Simple build script for JobScanner Pro GUI executable
Minimal configuration for troubleshooting or basic builds
"""

import os
import sys
import subprocess

def build_gui():
    """Build GUI executable with minimal configuration"""
    print("🚀 Building JobScanner Pro GUI (Simple Version)...")
    
    # Basic PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=JobScannerPro",
        "jobscanner/gui/app_tkinter.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable created successfully!")
        print(f"📁 Location: {os.path.abspath('dist/JobScannerPro.exe' if sys.platform == 'win32' else 'dist/JobScannerPro')}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

def main():
    """Main function"""
    if not os.path.exists("jobscanner"):
        print("❌ Please run from the project root directory")
        sys.exit(1)
    
    # Install PyInstaller if needed
    try:
        import PyInstaller
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    build_gui()

if __name__ == "__main__":
    main() 