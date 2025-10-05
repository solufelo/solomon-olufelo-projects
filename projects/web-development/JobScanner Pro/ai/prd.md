# Product Requirements Document (PRD): JobScanner Pro

## 1. Overview
JobScanner Pro is a tool designed to help users find and apply to creative jobs and gigs in Brampton, Ontario (and eventually any role/location in Canada). It provides both CLI and GUI interfaces, with optional automation for job applications.

## 2. Goals
- Aggregate creative job and gig listings from multiple Canadian sources.
- Provide easy-to-use CLI and GUI interfaces for searching and filtering jobs.
- Enable semi-automated job applications via email or web forms.
- Support future enhancements like notifications, scheduling, and job tracking.

## 3. Features & Phases
### Phase 0: Project Scaffold & Planning ✅
- Base repo, configuration, and documentation setup completed
- Proper package structure with src layout implemented
- Development guidelines and testing infrastructure in place

### Phase 1: Job + Gig Scraper (MVP – CLI) ✅
- Successfully implemented scrapers for:
  - Canada Job Bank (with retry mechanisms and rate limiting)
  - Craigslist Toronto (with location filtering)
  - Kijiji Gigs (with category support)
  - Indeed.ca (temporarily disabled due to Cloudflare)
- Robust CLI interface with:
  - Comprehensive argument parsing
  - Rich terminal output with progress indicators
  - Source filtering and sorting options
  - Error handling and user feedback
- Output formats: CSV and JSON with structured data

### Phase 2: Job Filtering & Deduplication ✅
- Job/Gig tagging system implemented
- URL/ID-based deduplication working
- Implemented filters:
  - New-only (last 24h)
  - Gigs-only/Jobs-only
  - Source-specific filtering
  - Location-based with radius support
- Pending: Salary parsing and filtering

### Phase 3: GUI Interface (Tkinter) 🚧
- User-friendly GUI for job search and export.
- Optional auto-apply integration.

### Phase 4: Auto-Apply System 🚧
- Match job type and application method.
- Send templated emails or autofill forms.
- Track applied jobs in a database.

### Phase 5: Enhancements 🚧
- Notifications, scheduling, resume generator, job tracker UI.

## 4. User Stories
- As a job seeker, I want to search for creative jobs and gigs in my area so I can find relevant opportunities.
- As a user, I want to filter and deduplicate job listings so I don’t see repeats.
- As a user, I want a GUI to make searching and applying easier.
- As a power user, I want to automate applications to save time.
- As a user, I want to be notified of new jobs and track my application status.

## 5. Success Criteria
### Phase 1 & 2 (Completed):
- ✅ Users can search jobs via CLI with multiple filters
- ✅ Scrapers reliably fetch jobs from implemented platforms
- ✅ Results are properly deduplicated and filtered
- ✅ Data is exported in both CSV and JSON formats
- ✅ Comprehensive test suite ensures reliability

### Remaining Criteria:
- Users can search and export job listings via CLI and GUI.
- Scrapers reliably fetch jobs from all target platforms.
- Deduplication and filtering work as expected.
- Auto-apply system sends emails or fills forms correctly.
- Users can track applied jobs and avoid duplicates.
- Documentation is clear and up-to-date.

## 6. Out of Scope
- International job scraping (initially Canada only)
- Full automation of all job applications (manual review encouraged)

## 7. Future Scope
- Expand to other locations and job types.
- Integrate with additional job boards.
- Advanced resume/portfolio customization. 