# JobScanner Pro 🔍

A powerful job and gig finder tool focused on creative opportunities in Canada, with automated application capabilities.

## 🎯 Features

- **Multi-Platform Scraping**: Aggregates jobs from:
  - Indeed.ca
  - Canada Job Bank
  - Craigslist (Toronto)
  - Kijiji (Gigs section)

- **Dual Interface**:
  - CLI for power users
  - GUI (Tkinter) for easy interaction

- **Smart Filtering**:
  - Job/Gig categorization
  - Deduplication
  - Custom filters (new-only, gigs-only)

- **Auto-Apply System**:
  - Email template system
  - Form auto-fill (via Playwright)
  - Application tracking

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.8+ required
python --version

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Copy the example config:
```bash
cp config.example.yml config.yml
```

2. Edit `config.yml` with your details:
```yaml
user:
  name: "Your Name"
  email: "your.email@example.com"
  location: "Brampton, ON"
  resume_path: "path/to/resume.pdf"

search:
  default_radius: 25  # km
  refresh_interval: 60  # minutes
```

## 💻 Usage

### CLI Mode

```bash
# Basic job search
python main.py search "graphic designer" --location "Brampton, ON"

# Search gigs only
python main.py search "photographer" --gigs-only

# Export results
python main.py search "web developer" --export csv
```

### GUI Mode

```bash
python gui/app_tkinter.py
```

### Auto-Apply Mode

```bash
# Review and apply to matched jobs
python apply.py --matches jobs.csv

# Auto-apply with specific template
python apply.py --template "templates/creative.txt"
```

## 📁 Project Structure

```
jobscanner/
├── main.py               # CLI entrypoint
├── apply.py             # Auto-apply system
├── config.yml           # User configuration
├── requirements.txt     # Python dependencies
├── .cursor             # Cursor IDE configuration
├── outputs/
│   ├── jobs.csv        # Exported job listings
│   ├── jobs.json       # JSON format job data
│   └── applied_jobs.db # SQLite DB of applied jobs
├── core/
│   └── search.py       # Core search logic
├── scrapers/
│   ├── indeed.py       # Indeed.ca scraper
│   ├── jobbank.py      # Canada Job Bank scraper
│   ├── craigslist.py   # Craigslist scraper
│   └── kijiji.py       # Kijiji gigs scraper
├── utils/
│   ├── filters.py      # Job filtering and deduplication
│   └── logger.py       # Logging utilities
├── gui/
│   └── app_tkinter.py  # GUI application
├── auto/
│   ├── email_sender.py # Email automation
│   └── playwright_apply.py # Form automation
├── templates/
│   └── email_template.txt # Email templates
└── README.md           # Project documentation
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Test specific component
pytest tests/test_scrapers.py
```

## 🛣 Roadmap

See [ai/plan.md](ai/plan.md) for detailed development phases and progress.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Disclaimer

This tool is for educational purposes only. Please review and comply with the terms of service of all job platforms before use. Some platforms may prohibit automated scraping or application submission.

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Uses Playwright for web automation
- Job data from Indeed.ca, Canada Job Bank, Craigslist, and Kijiji 