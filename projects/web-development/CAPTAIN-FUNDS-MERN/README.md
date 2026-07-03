# Captain Funds — MERN Fundraising Platform 🚀

A comprehensive, role-based fundraising platform built with MongoDB, Express.js, React, and Node.js, designed to manage campaign operations, track donations, and generate admin analytics dashboards.

> [!NOTE]
> **Project Status:** This project is **fully complete and deployed live** on Netlify. It serves as a core full-stack production showcase on the portfolio. The authentication backend, user roles (Admin vs. Standard), dashboard, and database mapping are fully verified.

---

## 🎯 Architecture & Highlight Features

*   **Role-Based Access Control (RBAC):** Distinct interfaces and operational dashboards for standard donors and platform administrators.
*   **Dynamic Campaign Dashboard (Completed):** Real-time statistics, progress bars showing fundraising achievements, and interactive campaign search.
*   **Zustand State Management (Completed):** Centralized client-side state machine handling active authentication session tokens, cached campaign states, and global alerts.
*   **Structured API Routing (Completed):** Separated Express router schemas for security validation, campaign mutation actions, and database queries.
*   **MongoDB Relations (Completed):** Mongoose database mapping representing user profiles, donation lists, and campaigns.

---

## 🛠️ Tech Stack & Utilities

### Frontend
- **React 18** with **TypeScript**
- **Vite** for build compilation
- **Ant Design (antd)** for modular UI tables and widgets
- **Zustand** for lightweight client state management
- **React Router DOM** for routing configurations
- **Axios** for HTTP request handshakes

### Backend
- **Node.js** with **Express.js** framework
- **MongoDB Atlas** with **Mongoose ODM**
- **JSON Web Tokens (JWT)** for authentication sessions
- **bcryptjs** for cryptographically hashed password security

---

## 🔧 Setup & Local Development

### Prerequisites
- Node.js (v18+ recommended)
- MongoDB account (Atlas or local instance)

### Local Configuration

1. **Backend Environment:**
   Create a `.env` file in the `server` directory:
   ```env
   MONGODB_URL=your_mongodb_connection_string
   JWT_SECRET=your_jwt_secret_key
   PORT=5000
   ```

2. **Installation:**
   ```bash
   # Install server dependencies
   cd server
   npm install

   # Install client dependencies
   cd ../client
   npm install
   ```

3. **Start Development Servers:**
   - **Terminal 1 (Server):**
     ```bash
     cd server
     npm start
     ```
   - **Terminal 2 (Client):**
     ```bash
     cd client
     npm run dev
     ```

4. **Access:**
   - Frontend: `http://localhost:5173`
   - Backend API: `http://localhost:5000`

---

## 📁 Repository Structure

```
CAPTAIN-FUNDS-MERN/
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/     # UI forms and dashboards
│   │   ├── store/          # Zustand store models
│   │   ├── interfaces/     # TypeScript structures
│   │   └── pages/          # Auth, campaigns, donations, reports
├── server/                 # Express backend
│   ├── config/            # DB connect logic
│   ├── models/            # Mongoose schemas (User, Campaign, Donation)
│   ├── routes/            # Express endpoint schemas
│   └── middleware/        # JWT auth and rate limiting
├── docs/                  # Architectural guidelines
└── README.md
```

---

## 🏁 Development Roadmap

- [x] **Phase 1: Project Scaffold:** Monorepo folder separation, TypeScript setups, and Vite configuration.
- [x] **Phase 2: Database & Authentication:** SQLite/MongoDB user mapping, JWT token creation, password hashing.
- [x] **Phase 3: User Roles & RBAC:** Admin routing logic, user verification panels, and restricted access middleware.
- [x] **Phase 4: Dashboard Interface:** Real-time totals, Ant Design data grid integrations, and responsive navigation.
- [x] **Phase 5: Campaign Creation:** Form validation schemas, image uploads, database insertion operations.
- [x] **Phase 6: Donation Processing:** Linking user donations to campaigns, updating progress calculations in real-time.
- [ ] **Phase 7: Payment Gateway Integration:** Add secure Stripe Hosted Checkout bindings to replace simulated balances.

---

## 🔒 Security & AI Guidelines
To maintain codebase health:
- Environment secrets are kept inside `.env` configurations and never committed.
- API operations validate user session roles at the gateway level.
- All code changes strictly follow patterns defined in `docs/AI-DEVELOPMENT-RULES.md`.
