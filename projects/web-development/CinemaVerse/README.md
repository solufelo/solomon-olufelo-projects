# CinemaVerse - Movie & TV Tracking Platform

🎬 A full-stack web application for tracking movies and TV shows with AI-powered recommendations.

**Live Demo**: [Coming Soon - Deploy to Render]

## Tech Stack
- **Framework**: [Wasp](https://wasp.sh) (React + Node.js + PostgreSQL)
- **Frontend**: React, TypeScript, Tailwind CSS
- **Backend**: Node.js, Express, Prisma ORM
- **Database**: PostgreSQL
- **APIs**: TMDB (movie data), OpenRouter (AI recommendations)
- **Authentication**: Email/Password + Google OAuth

## Features
- 🔍 Search movies and TV shows (TMDB API)
- 📝 Personal watchlists with progress tracking
- 🤖 AI-powered recommendations
- 👤 User authentication (email + Google)
- 📱 Responsive design
- 🎭 Episode tracking for TV shows
- 💬 Discussion forums

## Project Structure
1. `app/` - Main Wasp web application
2. `e2e-tests/` - Playwright end-to-end tests  
3. `blog/` - Documentation site (Astro/Starlight)

## Quick Start
```bash
cd app/
wasp start
```

## Deployment
See deployment guides in `app/` directory:
- `portfolio-deployment.md` - Free Render deployment for portfolio
- `render-deployment-guide.md` - Detailed Render setup
- `fly-deployment-guide.md` - Fly.io deployment (paid)

Built with ❤️ using [OpenSaaS](https://opensaas.sh) template
