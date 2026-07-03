# JobScanner Pro — Creative Gig Finder 🔍

A powerful Python command-line and desktop interface utility designed to aggregate, scrape, filter, and auto-apply to creative job opportunities and local gigs across Canada.

> [!NOTE]
> **Project Status:** This repository is an **active work in progress (WIP)** and serves as the primary pipeline powering Solomon's career discovery flows. Scraper modules for Canada Job Bank, Craigslist, Kijiji, and Indeed (via web-scraping fallback) are complete, alongside an NLP-powered resume keyword matching system. Active development is focused on the semi-automated Playwright form-filler.

---

## 🎯 Architecture & Highlight Features

*   **Multi-Platform Aggregator (Completed):** Scrapes and parses listings from Canada Job Bank (custom class selectors), Kijiji (Gigs), Craigslist (Toronto), and Indeed.ca (organic scraper parser).
*   **NLP Resume Keyword Analysis (Completed):** Integrated `spaCy` and `NLTK` models scanning local PDF/Docx resumes to extract skill profiles (design, coding, editing) and score job relevance.
*   **Tkinter Desktop Dashboard (Completed):** Redesigned tabbed GUI showing loading indicators, search radius parameters, salary ranges, match percentages, and folder management actions.
*   **Normalized Salary Parser (Completed):** normalizes and filters over 15 distinct salary formats (annual, hourly, monthly, e.g. "$50K" or "$30-$45/hr") into clear comparative metrics.
*   **Playwright Auto-Apply (In Progress):** Semi-automated application system generating custom templates and pre-filling standard online job application forms.

---

## 🛠️ Tech Stack & Utilities

### Core Automation
- **Python 3.10+** for scripting, data extraction, and threading logic.
- **Playwright:** Headless browser crawls, selector mapping, and automated application forms inputs.
- **SQLite:** Stores match logs, applied statuses, and deduplication keys.

### NLP & UI Libraries
- **spaCy (v3.8+) & NLTK (v3.9+):** Natural language parsing for skill categorization.
- **Tkinter (Python Standard Library):** Multi-threaded desktop user interface.
- **Pytest:** Local testing harness for scraper validation.

---

## 🚀 Getting Started & Configuration

### Prerequisites
- Python 3.10+ installed
- Pip package manager

### Configuration Setup

1. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Config File:**
   Copy the example config to active config:
   ```bash
   cp config.example.yml config.yml
   ```
   Edit `config.yml` with your details:
   ```yaml
   user:
     name: "Solomon Olufelo"
     email: "work@captainsolo.ca"
     location: "Brampton, ON"
     resume_path: "resumes/resume.pdf"
   ```

3. **Running the Utility:**
   - **CLI Search Mode:**
     ```bash
     python main.py search "web developer" --location "Brampton, ON" --gigs-only
     ```
   - **Launch Tkinter Desktop Dashboard:**
     ```bash
     python gui/app_tkinter.py
     ```
   - **Launch Auto-Apply Script:**
     ```bash
     python apply.py --matches outputs/jobs.csv
     ```

---

## 📁 Repository Structure

```
JobScanner Pro/
├── jobscanner/          # Module directory containing core search operations
│   ├── scrapers/        # Platform-specific scrapers (indeed.py, jobbank.py, kijiji.py)
│   ├── core/            # Main crawler loops and result aggregators
│   └── utils/           # Deduplication filters, NLP parsers, and salary extractors
├── gui/
│   └── app_tkinter.py   # Desktop user interface panels
├── outputs/             # Local database storage (applied_jobs.db, jobs.csv)
├── tests/               # Scraper testing scripts and fixture modules
├── requirements.txt     # Python package declarations
└── README.md
```

---

## 🏁 Development Roadmap

- [x] **Phase 0: Scaffold & Setup:** Project folder structure, configuration schemas, and Cursor workspace rules.
- [x] **Phase 1: CLI Scraper Modules:** Target platform APIs (JobBank, Kijiji, Craigslist) and output file mappings (CSV/JSON).
- [x] **Phase 2: Deduplication Filters:** Filtering duplicate postings by unique identifiers and scraping timestamps.
- [x] **Phase 3: GUI Desktop Interface:** Dynamic tabs, search suggest dropdowns, thread pools.
- [x] **Phase 4: spaCy Skill Parsing:** spaCy/NLTK NLP integrations, resume profile scoring, and normalizations.
- [x] **Phase 5: Indeed Web Scraping Port:** Converting Indeed search to web-scraping parsing after API deprecations.
- [/] **Phase 6: Auto-Apply Automations:** Email template generators, Playwright input injections, application status logs.
- [ ] **Phase 7: Scheduled Triggers:** Background cron runners, desktop alerts, and advanced email alerts.

---

## ⚠️ Disclaimer
This tool is for personal and educational search assistance. Users must comply with the terms of service of each target platform before running scraping operations.