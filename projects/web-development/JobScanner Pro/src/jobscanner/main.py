#!/usr/bin/env python3
"""
JobScanner Pro - Creative Job & Gig Finder (Canada Edition)
Main entry point for the CLI interface.
"""

import argparse
import logging
import sys
from pathlib import Path
import yaml
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich import print as rprint

# Local imports
from .core.search import JobSearch
from .utils.logger import setup_logger

# Initialize rich console
console = Console()

def load_config():
    """Load configuration from config.yml"""
    config_path = Path(__file__).parent / "config.yml"
    try:
        with open(config_path) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        console.print(f"[red]Error:[/red] config.yml not found at {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        console.print(f"[red]Error parsing config.yml:[/red] {e}")
        sys.exit(1)

def setup_argparse():
    """Setup command line argument parsing"""
    parser = argparse.ArgumentParser(
        description="JobScanner Pro - Find and apply to creative jobs in Canada"
    )
    
    parser.add_argument(
        "query",
        help="Job search query (e.g., 'graphic designer')"
    )
    
    parser.add_argument(
        "--location",
        default="Brampton, ON",
        help="Job location (default: Brampton, ON)"
    )
    
    parser.add_argument(
        "--radius",
        type=int,
        help="Search radius in km (default: from config)"
    )
    
    parser.add_argument(
        "--gigs-only",
        action="store_true",
        help="Only show gig postings"
    )
    
    parser.add_argument(
        "--new-only",
        action="store_true",
        help="Only show new postings"
    )
    
    parser.add_argument(
        "--remote-only",
        action="store_true",
        help="Only show remote jobs"
    )
    
    parser.add_argument(
        "--on-site-only",
        action="store_true",
        help="Only show on-site jobs"
    )
    
    parser.add_argument(
        "--source",
        choices=["indeed", "jobbank", "craigslist", "kijiji"],
        help="Only show results from specific source"
    )
    
    parser.add_argument(
        "--sort",
        choices=["date", "title", "company", "location"],
        default="date",
        help="Sort results by field (default: date)"
    )
    
    parser.add_argument(
        "--export",
        choices=["csv", "json"],
        help="Export results to specified format"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed job descriptions"
    )
    
    return parser

def sort_jobs(jobs, sort_by):
    """Sort jobs by specified field"""
    if sort_by == "date":
        return sorted(jobs, key=lambda x: x.get("posted_date", ""), reverse=True)
    return sorted(jobs, key=lambda x: x.get(sort_by, "").lower())

def display_results_table(jobs, verbose=False):
    """Display job results in a formatted table"""
    if not jobs:
        console.print("\n[yellow]No jobs found matching your criteria.[/yellow]")
        return
        
    # Create table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Title", style="cyan")
    table.add_column("Company", style="green")
    table.add_column("Location", style="blue")
    table.add_column("Type", style="yellow")
    table.add_column("Source", style="red")
    if verbose:
        table.add_column("Description", style="white", no_wrap=False)
    table.add_column("Posted", style="green")
    table.add_column("Salary", style="yellow")
    
    # Add rows
    for job in jobs:
        row = [
            job["title"],
            job["company"],
            job["location"],
            job["type"].capitalize(),
            job.get("source", "Unknown").capitalize(),
        ]
        if verbose:
            desc = job.get("description", "")
            row.append(desc[:200] + "..." if len(desc) > 200 else desc)
        row.extend([
            job.get("posted_date", "N/A"),
            job.get("salary", "Not specified")
        ])
        table.add_row(*row)
    
    # Print results
    console.print(f"\n[bold]Found {len(jobs)} jobs:[/bold]")
    console.print(table)
    
    # Print URLs separately for easy copying
    if verbose:
        console.print("\n[bold]Job URLs:[/bold]")
        for i, job in enumerate(jobs, 1):
            console.print(f"{i}. {job['url']}")

def main():
    """Main execution function"""
    # Load configuration
    config = load_config()
    
    # Setup logging
    setup_logger(config["logging"]["level"], config["logging"]["file"])
    logger = logging.getLogger(__name__)
    
    # Parse arguments
    parser = setup_argparse()
    args = parser.parse_args()
    
    try:
        # Initialize job search
        search = JobSearch(config)
        
        # Show progress during search
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Searching for jobs...", total=None)
            
            # Perform search
            results = search.search(
                query=args.query,
                location=args.location,
                radius=args.radius or config["search"]["default_radius"],
                gigs_only=args.gigs_only,
                new_only=args.new_only,
                remote_only=args.remote_only,
                on_site_only=args.on_site_only
            )
            
            progress.update(task, completed=True)
        
        # Filter by source if specified
        if args.source:
            results = [job for job in results if job.get("source") == args.source]
        
        # Sort results
        results = sort_jobs(results, args.sort)
        
        # Export or display results
        if args.export:
            output_file = f"outputs/jobs.{args.export}"
            search.export_results(results, output_file, format=args.export)
            console.print(f"\n[green]Results exported to {output_file}[/green]")
        else:
            display_results_table(results, verbose=args.verbose)
            
    except KeyboardInterrupt:
        console.print("\n[yellow]Search cancelled by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error during job search: {e}")
        console.print(f"\n[red]Error during job search:[/red] {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 