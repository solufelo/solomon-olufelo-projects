#!/usr/bin/env python3
"""
Test script to verify youth job scraping functionality.
"""

import sys
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from jobscanner.scrapers.jobbank import JobBankScraper

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def test_youth_jobs():
    """Test JobBank scraper with youth job support"""
    print("Testing JobBank scraper with youth job support...")
    print("="*60)
    
    try:
        scraper = JobBankScraper()
        print("✓ JobBank scraper initialized successfully")
        
        # Test search with a query that should return both regular and youth jobs
        results = scraper.search("camp counsellor", "Toronto, ON")
        print(f"✓ Search completed - Found {len(results)} total results")
        
        if results:
            # Count job types
            regular_jobs = [j for j in results if j.get("source") != "Canada Summer Jobs"]
            youth_jobs = [j for j in results if "Canada Summer Jobs" in str(j.get("source", ""))]
            
            print(f"  Regular jobs: {len(regular_jobs)}")
            print(f"  Youth jobs: {len(youth_jobs)}")
            print()
            
            # Show a few examples - mix of regular and youth jobs
            print("Sample results:")
            sample_count = 0
            
            # Show regular jobs first
            for job in results:
                if job.get("source") == "Job Bank" and sample_count < 2:
                    sample_count += 1
                    print(f"{sample_count}. [Regular] {job.get('title', 'N/A')} - {job.get('company', 'N/A')}")
                    print(f"   Location: {job.get('location', 'N/A')}")
                    print(f"   Source: {job.get('source', 'N/A')}")
                    if job.get('salary'):
                        print(f"   Salary: {job.get('salary')}")
                    print()
            
            # Show youth jobs
            for job in results:
                if job.get("source") == "Canada Summer Jobs" and sample_count < 5:
                    sample_count += 1
                    print(f"{sample_count}. [Youth] {job.get('title', 'N/A')} - {job.get('company', 'N/A')}")
                    print(f"   Location: {job.get('location', 'N/A')}")
                    print(f"   Source: {job.get('source', 'N/A')}")
                    if job.get('salary'):
                        print(f"   Salary: {job.get('salary')}")
                    print()
        else:
            print("⚠ No results found")
            
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run the test"""
    success = test_youth_jobs()
    
    print("="*60)
    if success:
        print("✓ Youth job scraping test PASSED")
    else:
        print("✗ Youth job scraping test FAILED")

if __name__ == "__main__":
    main() 