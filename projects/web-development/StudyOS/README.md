# findYOU OS — Productivity & Study Operating System 🚀

A comprehensive, full-stack productivity workspace and cognitive dashboard built with Wasp, combining Spaced Repetition learning tools, Pomodoro focus timers, an Eisenhower Task Matrix, and Python/Playwright scraping automation.

> [!NOTE]
> **Project Status:** This repository is an **active work in progress (WIP)** and serves as the primary interactive showcase featured on [captainsolo.ca/demo](https://captainsolo.ca/demo). The Wasp dashboard, Leitner flashcard deck engine, task boards, and pomodoro clocks are operational. Current focus is merging the standalone Python scraper scripts into the core application database.

---

## 🎯 Architecture & Highlight Features

*   **Eisenhower Task Matrix (Completed):** Category board grouping tasks dynamically into priority quadrants: Urgent & Important (Do), Important/Not Urgent (Plan), Urgent/Not Important (Delegate), and Not Urgent/Important (Eliminate).
*   **Spaced Repetition Decks (Completed):** Flashcard deck compiler leveraging the Leitner review algorithm to automatically adjust review intervals (Box 1 to Box 5).
*   **Pomodoro Focus Engine (Completed):** Timed study intervals with cycle tracking and statistics logging mapped to individual decks.
*   **Python Crawler Integration (In Progress):** Standalone Playwright scripts that crawl local developer challenges and job posts, writing matches directly to SQLite database pools.
*   **Cognitive Gamification (Completed):** Built-in reaction speed mini-games with local leaderboard score logs for focus exercises.

---

## 🛠️ Tech Stack & Utilities

### Core Application
- **Wasp Framework:** Declarative compilation engine connecting the React client app with the Node/Prisma backend server.
- **React & TypeScript:** Type-safe components and responsive layout patterns.
- **PostgreSQL / SQLite:** Relational storage for decks, cards, task objects, and history statistics.
- **Tailwind CSS:** Responsive grid styling and glassmorphism UI.

### Automation Scrapers
- **Python 3.10+** (running sandboxed task execution routines).
- **Playwright Library:** Automated headless browser crawing and parsing filters.

---

## 🚀 Getting Started & Installation

### Prerequisites
- Node.js (v18+ recommended)
- Wasp CLI installed globally
- Python 3.10+ (for task crawlers)

### Local Configuration

1. **Start Wasp application compiler:**
   ```bash
   wasp start
   ```

2. **Initialize Database migrations:**
   Ensure database instances are active locally, then sync structures:
   ```bash
   wasp db migrate-dev
   ```

3. **Access Local Workspace:**
   - App Workspace: `http://localhost:3000`
   - Database Admin Studio: `wasp db studio`

---

## 📁 Repository Structure

```
StudyOS/                  # findYOU OS application root
├── main.wasp             # Declarative Wasp routes, auth, and query mappings
├── schema.prisma         # Relational database models (User, Deck, Card, Task, GameScore)
├── src/
│   ├── client/           # React dashboard UI, Eisenhower boards, Pomodoro timers
│   ├── server/           # Prisma Queries, task scheduling, database mutation operations
│   └── shared/           # Shared interface definitions
├── scripts/
│   └── scrapers/         # Python Playwright crawlers and database write-backs
└── README.md
```

---

## 🏁 Development Roadmap

- [x] **Phase 1: Architecture & Scaffolding:** Initializing Wasp project targets, Prisma structure, and client routers.
- [x] **Phase 2: Spaced Repetition Engine:** Leitner box logic, deck lists, flashcard creation forms.
- [x] **Phase 3: Eisenhower Task Planner:** Priority matrices, drag-toggle completion status.
- [x] **Phase 4: Focus Timer Clocks:** Pomodoro sessions, logging cycle statistics, session metrics.
- [x] **Phase 5: Playwright Crawler Scripting:** Standalone headless browser crawlers extracting career postings.
- [/] **Phase 6: Relational Database Sync:** Writing Playwright crawler output files directly to Prisma Task databases.
- [ ] **Phase 7: Cloud Deployments:** Deployment of dashboard to Render/Fly.io.

---

## ⚠️ Integrity & Rules
- Private credentials and local `findyou.db` pools are excluded from Git commits.
- Accessibility standards (WCAG 2.1 AA) are followed across all dashboard views.