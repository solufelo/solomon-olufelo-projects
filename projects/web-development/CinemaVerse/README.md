# CinemaVerse — Movie & TV Tracking Platform 🎬

A full-stack, AI-enhanced movie and TV tracking web application that allows users to search titles, manage personalized watchlists, and receive AI-driven recommendations based on their viewing preferences.

> [!NOTE]
> **Project Status:** This repository is an **active work in progress (WIP)** built on the Wasp framework and deployed to Netlify. All core search capabilities, database watchlists, and user authentication modules are operational. The next developmental sprint focuses on refining the OpenRouter API integrations and AI recommender prompts.

---

## 🎯 Architecture & Highlight Features

*   **TMDB API Integration (Completed):** Direct searches, trailer streams, and metadata aggregation for thousands of movies and TV series.
*   **Personal Watchlists (Completed):** Detailed watchlists mapped directly to authenticated user profiles with watch progress indicators.
*   **OpenSaaS Boilerplate Foundation (Completed):** Implements a production-grade full-stack framework with built-in Tailwind styling, Prisma migrations, and routes.
*   **AI Recommendations (In Progress):** Generates personalized recommendations using TMDB viewing history processed through OpenRouter AI models.
*   **Google OAuth Authentication (Completed):** Built-in email/password credentials combined with Google OAuth API profiles.

---

## 🛠️ Tech Stack & Utilities

### Full-Stack Core
- **Wasp Framework:** Declarative configuration layer compile-generating the React frontend and Node.js backend.
- **Prisma ORM:** Database connection, relations mapping, and SQL query generation.
- **PostgreSQL:** Reliable relational store for user listings, watchlists, and discussion forums.

### Frontend
- **React** (via Wasp compiler bundle)
- **TypeScript** for type-safe components
- **Tailwind CSS** for responsive styling

### APIs & AI Integration
- **TMDB API:** Movie metadata, poster image endpoints, and search index queries.
- **OpenRouter API:** Connects watch histories to LLM recommendation prompts.

---

## 🚀 Getting Started & Installation

### Prerequisites
- Node.js (v18+ recommended)
- Wasp CLI (latest version installed)
- PostgreSQL local server or hosted connection URL

### Local Setup

1. **Install dependencies and start Wasp dev engine:**
   ```bash
   cd app/
   wasp start
   ```

2. **Database Migrations:**
   Ensure your local database connection is active, then apply migrations:
   ```bash
   wasp db migrate-dev
   ```

3. **Access Development Ports:**
   - Client App: `http://localhost:3000`
   - Server API logs will stream to the terminal.

---

## 📁 Repository Structure

```
CinemaVerse/
├── app/                  # Main Wasp application files
│   ├── src/
│   │   ├── client/       # React pages, buttons, and state logic
│   │   ├── server/       # Node.js actions, queries, and cron tasks
│   │   └── shared/       # Shared TS type interfaces
│   ├── main.wasp         # Declarative full-stack routing schema config
│   └── schema.prisma     # Prisma database schemas
├── e2e-tests/            # Playwright testing scripts
├── blog/                 # Documentation website (Astro/Starlight framework)
└── README.md
```

---

## 🏁 Development Roadmap

- [x] **Phase 1: Project Initialization:** Wasp boilerplate setup, database config, and OpenSaaS integration.
- [x] **Phase 2: TMDB Search Engine:** Direct API queries, search boxes, and responsive grid layouts.
- [x] **Phase 3: Watchlist Databases:** SQLite/Postgres schemas, card listing operations, and add/remove logic.
- [x] **Phase 4: Multi-Provider Auth:** Implementing secure email signup and Google OAuth hooks.
- [ ] **Phase 5: OpenRouter AI recommendations:** Custom system prompts generating title recommendations from watch logs.
- [ ] **Phase 6: Discussion Forums:** Social comment boards and episode progress reviews.
- [ ] **Phase 7: Production Deployments:** Static client build to Netlify and backend server build to Render.

---

## 🔒 Security & AI Guidelines
To maintain API limits and safety:
- Never commit private TMDB or OpenRouter keys; use `app/.env.server` configurations.
- All database operations are written as declarative Wasp actions to guarantee Prisma type safety.
