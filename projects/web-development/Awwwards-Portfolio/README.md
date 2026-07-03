# captainsolo.ca — Awwwards-Style Interactive Portfolio 🚀

A high-performance, immersive developer and creator portfolio built with React and Vite, featuring WebGL 3D scenes, physics-decoupled animations, a custom liquid-glass design system, and a Python-powered database backend.

> [!NOTE]
> **Project Status:** This repository contains the frontend and UI boilerplate for the live production site at [captainsolo.ca](https://captainsolo.ca). All core navigation, 3D scenes, Works showcase filters, and responsive styles are fully stable. Active development is focused on expanding the client portal and API notification webhooks.

---

## 🎯 Architecture & Highlight Features

*   **Immersive 3D Planet Scene (Completed):** Desktop users experience an interactive 3D WebGL planet rendered with React Three Fiber (R3F), preloaded using asset checkpoints.
*   **Procedural Mobile Fallback (Completed):** A lightweight `PlanetLite` procedural component renders inside the canvas for mobile viewports, avoiding heavy GLB download overhead.
*   **Interactive Works Showcase (Completed):** Dynamic cards with mouse-following hover expansions, dual-action URLs (Live Demo + GitHub), and tags (Development / Video / Motion).
*   **Liquid Glass Design System (Completed):** A responsive, accessible styling framework engineered with Tailwind CSS v4, supporting AODA/WCAG AA color-contrast compliance.
*   **Secure SQLite Backend (Completed):** A custom cPanel Python Passenger setup handling contact messages, SQLite admin credentials, and session cookie validation.

---

## 🛠️ Tech Stack & Utilities

### Frontend
- **React 19** & **TypeScript**
- **Vite** for fast, optimized HMR and code-splitting bundles
- **Three.js / React Three Fiber (R3F)** for WebGL rendering
- **GSAP (GreenSock)** for physics-independent marquee and element animations
- **Tailwind CSS v4** for utility-first styling and theme tokens

### Backend (cPanel Serverless)
- **Python / WSGI (Passenger)** for API routing
- **SQLite** for session, database, and project CMS queries
- **HTTP-Only Cookies** for persistent secure admin validation

---

## 🔧 Setup & Local Development

### Prerequisites
- Node.js (v20+ recommended)
- Python 3.10+ (for backend API development)

### Quick Start

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

3. **Access local preview:**
   - Frontend: `http://localhost:5173`
   - Active logs will print to the console.

---

## 📁 Repository Structure

```
captainsoloHQ/
├── src/
│   ├── components/       # 3D planet modules, contact forms, card UI
│   ├── context/          # Global theme states (Light default/Liquid blue)
│   ├── data/             # showcaseProjects.js (single source of truth)
│   ├── pages/            # Dashboard, Admin CMS portal, interactive /demo
│   └── sections/         # Home, About, Services, Works, Contact sections
├── tools/
│   ├── portfolio-backend/# Python api server, database models, passenger WSGI
│   └── apply-pipeline/   # Profile metadata and automated CSJ resume tools
├── public/               # Static models, high-res thumbnails, .htaccess caching rules
└── vite.config.js        # Build splitting definitions and assets configurations
```

---

## 🏁 Development Roadmap

- [x] **Phase 1: React & Vite Scaffolding:** Clean project setup, route structure, and Tailwind configuration.
- [x] **Phase 2: 3D Scene Integrations:** R3F Canvas setup, GLB preload, and lightweight mobile procedural meshes.
- [x] **Phase 3: Works Showcase:** Filter categories (All, Code, Video, Motion, WIP) and interactive card elements.
- [x] **Phase 4: cPanel Migration:** Porting from Netlify to cPanel, configuring SSL, custom `.htaccess` asset headers.
- [x] **Phase 5: Secure Contact Form API:** Python endpoint `/api/contact` routing inputs securely to `work@captainsolo.ca`.
- [x] **Phase 6: Admin CMS Dashboard:** SQLite schemas for projects and blog, cookie-based token validation, and seeding.
- [ ] **Phase 7: Modular Pages:** Add dedicated routes `/work/code` and `/work/video` as optimized lane wrappers.

---

## 🔒 Design & Safety Protocols
To maintain high performance and SEO:
- All static assets (e.g. `Planet.glb`) use `.htaccess` long-term caching rules.
- Route paths use dynamic lazy splitting (`React.lazy`) to minimize first paint bundle size.
- Sensitive environment variables are kept out of Git via standard `.env` templates.
