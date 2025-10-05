#!/usr/bin/env python3
"""
Debug script to test Brampton job searches and diagnose issues
"""

import sys
import logging
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from jobscanner.core.search import JobSearch

def setup_debug_logging():
    """Setup detailed logging for debugging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def test_brampton_search():
    """Test job search in Brampton with detailed output"""
    print("🔍 JobScanner Pro - Brampton Search Debug Tool")
    print("=" * 60)
    
    # Setup logging
    setup_debug_logging()
    
    # Configuration
    config = {
        "search": {
            "platforms": {
                "indeed": True,
                "jobbank": True,
                "craigslist": True,
                "kijiji": True
            }
        }
    }
    
    # Test parameters
    test_cases = [
        {
            "query": "graphic designer",
            "location": "Brampton, ON", 
            "radius": 25
        },
        {
            "query": "designer",
            "location": "Brampton, ON",
            "radius": 50  # Try larger radius
        },
        {
            "query": "marketing",
            "location": "Brampton, ON",
            "radius": 25
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🧪 Test Case {i}: '{test_case['query']}' in {test_case['location']} ({test_case['radius']}km)")
        print("-" * 40)
        
        try:
            # Initialize search
            search = JobSearch(config)
            
            # Perform search
            results = search.search(
                query=test_case["query"],
                location=test_case["location"],
                radius=test_case["radius"]
            )
            
            print(f"✅ Total Results: {len(results)} jobs found")
            
            # Break down by source
            sources = {}
            for job in results:
                source = job.get("source", "unknown")
                sources[source] = sources.get(source, 0) + 1
            
            print("\n📊 Results by Source:")
            for source, count in sources.items():
                print(f"  • {source.title()}: {count} jobs")
            
            # Show sample results
            if results:
                print(f"\n📝 Sample Jobs (first 3):")
                for j, job in enumerate(results[:3], 1):
                    print(f"  {j}. {job.get('title', 'No Title')}")
                    print(f"     Company: {job.get('company', 'Unknown')}")
                    print(f"     Location: {job.get('location', 'Unknown')}")
                    print(f"     Source: {job.get('source', 'Unknown')}")
                    print()
            
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("🔧 Troubleshooting Tips:")
    print("• If no results: Try broader search terms like 'design' or 'marketing'")
    print("• If few results: Increase radius to 50km or try 'Toronto, ON'")
    print("• Check individual sources: Some may be temporarily down")
    print("• Location issues: Try 'Mississauga, ON' or 'Toronto, ON' for comparison")
    
def test_individual_scrapers():
    """Test each scraper individually to isolate issues"""
    print("\n🔍 Individual Scraper Test")
    print("=" * 40)
    
    from jobscanner.scrapers.jobbank import JobBankScraper
    from jobscanner.scrapers.craigslist import CraigslistScraper
    from jobscanner.scrapers.kijiji import KijijiScraper
    
    scrapers = [
        ("JobBank", JobBankScraper()),
        ("Craigslist", CraigslistScraper()),
        ("Kijiji", KijijiScraper())
    ]
    
    for name, scraper in scrapers:
        print(f"\n🧪 Testing {name}...")
        try:
            jobs = scraper.search(
                query="designer",
                location="Brampton, ON",
                radius=25
            )
            print(f"✅ {name}: {len(jobs)} jobs found")
            if jobs:
                sample = jobs[0]
                print(f"   Sample: {sample.get('title', 'No title')} at {sample.get('company', 'No company')}")
        except Exception as e:
            print(f"❌ {name}: Error - {e}")

if __name__ == "__main__":
    test_brampton_search()
    test_individual_scrapers() 