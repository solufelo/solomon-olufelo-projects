# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Enhanced Search Filtering System:**
  - Remote vs on-site job filtering with smart detection
  - Area-based search with radius control and distance mapping
  - Advanced filter options (--remote-only, --on-site-only CLI flags)
  - Intelligent remote job detection using keywords and patterns
  - Support for hybrid work arrangements

- **NLP-Powered Resume Analysis:**
  - Multi-format document support (PDF, DOCX, TXT) using textract and python-docx
  - spaCy and NLTK integration for advanced text processing
  - Skill categorization across 6 categories (design software, web technologies, marketing skills, etc.)
  - Experience years extraction with pattern matching
  - Intelligent keyword scoring and ranking system with frequency analysis
  - Resume-based search term generation for personalized job matching

- **Advanced Salary Filtering System:**
  - Comprehensive salary format parsing (hourly, annual, monthly)
  - Range and single amount detection with smart parsing
  - K-format support (e.g., $50K, $40K-60K)
  - Negotiable salary detection using keyword patterns
  - Cross-format comparison and normalization for filtering
  - Real-time salary filtering integrated into search results

- **Indeed API Resolution and Web Scraping Implementation:**
  - **API Deprecation Investigation:** Discovered Indeed API changes (October 2024)
  - **Industry Analysis:** Documented $3/call pricing model and organic traffic removal
  - **Web Scraping Conversion:** Rebuilt Indeed scraper using BeautifulSoup
  - **Rate Limiting Implementation:** Added respectful 2-second delays and 429 error handling
  - **Configuration Updates:** Re-enabled Indeed as active job source
  - **Fallback Strategy:** Prepared system for similar API changes from other job sites

- **Completely Redesigned GUI Interface:**
  - **Essential Search Fields Section:**
    - Job title with intelligent suggestions for creative roles
    - Company search (optional)
    - Location dropdown with popular GTA cities
    - Radius control (5-100km)
    - Additional keywords field
  - **Job Preferences Panel:**
    - Job type filter (full-time, part-time, contract, freelance, internship)
    - Experience level filtering (entry-level to 10+ years)
    - Work style preferences (remote, on-site, hybrid, any)
  - **Salary Range Filtering:**
    - Min/max salary inputs
    - Salary type selection (hourly, annual, monthly)
  - **Resume/CV Integration:**
    - File upload for resume and cover letter
    - Automatic keyword extraction for enhanced job matching
    - Option to use resume keywords for related job discovery
  - **Enhanced User Experience:**
    - Tabbed interface (Search tab, Results tab)
    - Real-time loading indicators with progress bar
    - Threaded search to prevent UI freezing
    - Professional styling with modern themes

- **Smart Search Capabilities:**
  - **Intelligent Search Term Generation:**
    - Synonym expansion for job titles (e.g., "graphic designer" → "visual designer", "brand designer")
    - Related role discovery based on job categories
    - Resume keyword integration for personalized matching
  - **Multi-term Search Strategy:**
    - Primary search with main job title
    - Secondary searches with related terms
    - Comprehensive result aggregation and deduplication
  - **Match Scoring System:**
    - Relevance scoring based on search term matches
    - Bonus points for exact title matches
    - Percentage-based match ratings in results

- **Enhanced Results Display:**
  - **Comprehensive Results Table:**
    - Added salary, posting date, and match percentage columns
    - Better column sizing and scrollable interface
    - Results summary with statistics (total jobs, remote count, average match)
  - **Smart Result Organization:**
    - Automatic sorting by match score
    - Remote job indicators
    - Truncated text with tooltips for long entries

- **Advanced Export and File Management:**
  - **Enhanced Export Features:**
    - Timestamped CSV exports with all job details
    - Search parameters export in JSON format
    - Match scores and descriptions included in exports
  - **File Management Integration:**
    - "Open Exports Folder" button for easy file access
    - Cross-platform folder opening (Windows, macOS, Linux)
    - Organized output structure with timestamps

- **Performance and UX Improvements:**
  - Asynchronous search processing to prevent UI blocking
  - Real-time status updates during search operations
  - Comprehensive error handling and user feedback
  - Search validation and input sanitization

- Initial project structure and scaffolding:
  - Created base repository with proper `jobscanner/` project folder
  - Defined `.cursor` rules file with entry points and module rules
  - Set up proper Python package structure with dependencies
- Basic documentation:
  - Comprehensive README.md with project purpose, usage, and future scope
  - Detailed project planning in `plan.md`
  - Product requirements in `prd.md`
- Core project files:
  - `requirements.txt` with comprehensive dependencies including NLP libraries
  - `config.yml` with user and search settings
  - `utils/resume_parser.py` for NLP-powered resume analysis
  - `utils/salary_parser.py` for advanced salary filtering
  - `main.py` CLI entry point with argument parsing
  - `core/search.py` for coordinating job searches
  - `utils/filters.py` for job filtering and deduplication
  - `utils/logger.py` for logging configuration
- Scraper implementations:
  - `scrapers/base.py` base scraper interface
  - `scrapers/indeed.py` Indeed.ca implementation (converted from API to web scraping)
  - `scrapers/jobbank.py` Canada Job Bank implementation with:
    - Enhanced retry mechanisms
    - Robust rate limiting
    - Improved error handling
    - **Fixed CSS selectors for proper job parsing**
  - `scrapers/craigslist.py` Craigslist Toronto implementation with:
    - Support for both jobs and gigs sections
    - Category-based searching
    - Location filtering for Brampton area
    - Rate limiting protection
  - `scrapers/kijiji.py` Kijiji implementation with:
    - Dual support for jobs and services/gigs sections
    - Category-specific searching (art, media, design, etc.)
    - GTA location mapping and filtering
    - Price/compensation parsing
    - Rate limiting protection
- Testing infrastructure:
  - Comprehensive test suite for all scrapers
  - SQLite DB tests for duplicate prevention
  - Integration tests for search functionality
  - Test fixtures and configuration
  - Mock responses for consistent testing
- **Production-Ready NLP Libraries:**
  - spaCy 3.8.7 with English language model for advanced text processing
  - NLTK 3.9.1 with tokenization, POS tagging, and named entity recognition
  - Document processing libraries: PyPDF2, python-docx, textract
  - Skill database with 300+ recognized skills across 6 categories
  - Real-time keyword extraction and job matching algorithms
- Development guidelines in `rules.md`
- Enhanced CLI functionality:
  - Added comprehensive argument parsing with tests
  - Implemented rich terminal output
  - Added progress spinner and source filtering
  - Added sorting options for results
  - Added proper error handling and user feedback
  - **New CLI flags: --remote-only, --on-site-only**
- Testing infrastructure:
  - Added test_cli.py with comprehensive test cases
  - Added conftest.py with shared test fixtures
  - Added proper package structure with __init__.py files
  - Updated setup.py with test dependencies
  - Added integration tests for CLI functionality

### Changed
- User configuration in `config.yml`:
  - Set email to "solomonolufelo@outlook.com"
  - Updated resume path to "./assets/Solomon_Resume.rtf"
  - **Re-enabled Indeed scraper** (converted from API to web scraping)
- **Dependencies and Libraries:**
  - Added 18+ new NLP and document processing libraries
  - Installed spaCy with English language model (en_core_web_sm)
  - Added NLTK with required data packages (punkt, stopwords, POS tagger)
  - Integrated PyPDF2, python-docx, and textract for document parsing
  - Updated six library to resolve compatibility issues
- **Major GUI Architecture Overhaul:**
  - Completely redesigned interface from basic form to professional tabbed layout
  - Enhanced from 800x600 to 1200x800 window size for better usability
  - Improved component organization with logical grouping
  - Better responsive design with proper grid layouts
- **Search Algorithm Enhancement:**
  - Upgraded from single-term to multi-term intelligent search
  - Implemented relevance scoring and ranking system
  - Added resume-based keyword extraction and matching
- **Filter System Improvements:**
  - Enhanced core filters module with remote job detection
  - Improved location-based filtering with distance mapping
  - Added comprehensive job preference filtering
- Fixed date parsing in Job Bank scraper to properly handle datetime objects
- Enhanced Job Bank scraper with improved retry mechanisms and rate limiting
- **Fixed critical JobBank scraper CSS selectors** - now finding 20+ jobs per search
- Temporarily disabled Indeed.ca scraper due to Cloudflare protection issues
- Updated project structure to use src layout
- Enhanced error handling in CLI with proper exit codes
- Added rich package for improved terminal output
- Updated source names in GUI to match backend expectations
- Improved config handling for platform selection
- Enhanced package structure for better test discovery

### Fixed
- **Critical JobBank Scraper Issues:**
  - Fixed incorrect CSS selectors ("action-buttons" vs "job-search-result")
  - Fixed title selector ("noctitle" vs "noc-title")
  - Corrected search URL endpoint (/jobsearch instead of /search-job)
  - Now successfully parsing job listings and finding results
- **Indeed API Resolution:**
  - Investigated and documented Indeed API deprecation (October 2024)
  - Resolved 404 endpoint errors by converting to web scraping
  - Fixed rate limiting issues with proper delay implementation
  - Restored Indeed as functional job source
- Resolved ModuleNotFoundError for 'core' module
- Fixed import issues in main.py using relative imports
- Fixed package structure with proper __init__.py files
- Fixed GUI integration with JobSearch class:
  - Corrected search parameters
  - Added proper config initialization
  - Fixed source selection handling
- Fixed test suite issues:
  - Corrected mock usage in export tests
  - Fixed package discovery in test environment
  - Added proper test fixtures and cleanup

### Performance Improvements
- **Asynchronous Search Processing:**
  - Implemented threaded search operations to prevent UI blocking
  - Added real-time progress indicators and status updates
  - Enhanced user experience during long search operations
- **Smart Caching and Deduplication:**
  - Improved duplicate detection across multiple search terms
  - Optimized result aggregation and sorting
  - Reduced redundant API calls through intelligent search strategies

### Security
- Enhanced input validation and sanitization
- Secure file handling for resume/CV uploads
- Safe cross-platform file system operations

### Pending (Next Steps)
- **Phase 4: Auto-Apply System Development:**
  - Email template system with dynamic job application generation
  - Playwright-based form detection and auto-fill capabilities
  - Application tracking database (SQLite) for applied jobs
  - Integration testing for end-to-end application workflow
- **Quality Assurance and Testing:**
  - Comprehensive test suite for NLP and smart search features
  - Performance testing for large result sets and multiple job sources
  - Cross-platform testing for file management features
  - Load testing for concurrent search operations
- **System Enhancements:**
  - Fine-tune Indeed web scraper selectors for improved job detection
  - Notification system for new job matches with desktop alerts
  - Advanced analytics dashboard for job market trends and salary insights
  - Machine learning-based job recommendations and career progression suggestions
