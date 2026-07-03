# Creative Engine — Scalable Agency Operating System 🚀

A multi-tenant, serverless booking, checkout, and client-management pipeline designed to automate scheduling, payment deposits, and intake pipelines for GTA creatives and agencies.

> [!NOTE]
> **Project Status:** This repository is the **next active target** on the development roadmap. Work will begin immediately following the final release of the `light-years-game` executable and web demo. The monorepo layout and Next.js boilerplate setup are initialized.

---

## 🎯 Architecture & Highlight Features

*   **Monorepo Core (Turborepo):** Combines separate agency checkouts and developer management dashboards inside a single unified typescript project, sharing a centralized Tailwind UI package.
*   **Cryptographic Tenant Isolation (Supabase RLS):** Database-level security enforcing strict tenant data segregation via PostgreSQL Row-Level Security (RLS) rules.
*   **Stripe Connect Checkout (Planned):** Automated retainer deposit collections and transaction routing for client bookings.
*   **Edge Subdomain Rewriting (Planned):** Next.js middleware that intercepts custom subdomain paths (e.g. `nolosses.creativeengine.ca`) and resolves them dynamically.
*   **AI Onboarding Setup Wizard (Planned):** Dynamic setup assistant powered by the Vercel AI SDK and local LLMs (Ollama) to extract services, durations, and rates via conversational intake.

---

## 🛠️ Tech Stack & Utilities

### Frameworks & UI
- **Turborepo** for monorepo build caching and execution pipelines
- **Next.js (App Router)** for frontend deployment and React Server Actions
- **Tailwind CSS** & **shadcn/ui** for fluid liquid-glass styling configurations

### Database & Security
- **Supabase (PostgreSQL)** for transactional persistence
- **Drizzle ORM** for compile-time safe database queries and automated schema migrations
- **Postgres Row-Level Security (RLS)** for tenant workspace isolation

### Payments & Automation
- **Stripe Connect** for hosted billing checkouts and webhook reconciliations
- **Vercel AI SDK** with **Ollama** (local development) / OpenAI (production) for client setup automation

---

## 📁 Monorepo Layout

```
creative-engine/
├── apps/
│   ├── boilerplate/      # The bare-metal SaaS core (Auth, Stripe Billing, Tenant Admin)
│   └── client-demo/      # The customized client storefront (Beta template for @nolosses)
├── packages/
│   ├── ui/               # Shared primitives library (Calendars, Buttons, Form inputs)
│   └── database/         # Shared Drizzle schemas and PostgreSQL connection helpers
├── package.json
└── turbo.json
```

---

## 📊 Database Schema Model

Drizzle relational definitions enforcing security-isolated booking routes:

```typescript
// Tenants / Agency workspaces
export const tenants = pgTable('tenants', {
  id: uuid('id').defaultRandom().primaryKey(),
  name: text('name').notNull(),
  subdomain: text('subdomain').unique().notNull(),
  createdAt: timestamp('created_at').defaultNow().notNull(),
});

// Profiles (Creators & Clients)
export const profiles = pgTable('profiles', {
  id: uuid('id').primaryKey(), // Maps to Supabase auth.users
  tenantId: uuid('tenant_id').references(() => tenants.id),
  fullName: text('full_name').notNull(),
  email: text('email').unique().notNull(),
  role: text('role').default('client').notNull(), // 'admin' | 'creator' | 'client'
});

// Booking Services
export const services = pgTable('services', {
  id: uuid('id').defaultRandom().primaryKey(),
  tenantId: uuid('tenant_id').references(() => tenants.id),
  title: text('title').notNull(),
  price: integer('price').notNull(), // represented in cents
});

// Bookings
export const bookings = pgTable('bookings', {
  id: uuid('id').defaultRandom().primaryKey(),
  tenantId: uuid('tenant_id').references(() => tenants.id),
  clientId: uuid('client_id').references(() => profiles.id),
  serviceId: uuid('service_id').references(() => services.id),
  sessionDate: timestamp('session_date').notNull(),
  status: text('status').default('pending').notNull(),
});
```

---

## 🏁 Development Roadmap

- [x] **Phase 1: Foundation Setup:** Turborepo initialization, package configurations, ESLint/Prettier setups, and local workspace hooks.
- [ ] **Phase 2: DB & RLS Core:** Setting up Supabase relational tables and deploying PostgreSQL Row-Level Security policies.
- [ ] **Phase 3: The Booking Slice:** Developing reusable calendar components and hooking client selections to Server Actions.
- [ ] **Phase 4: Stripe Connect Setup:** Implementing checkout session endpoints and handling webhook validations.
- [ ] **Phase 5: Subdomain Routing Middleware:** Coding Next.js middleware hooks to parse incoming subdomains and rewrite dynamic paths.
- [ ] **Phase 6: AI Onboarding Agent:** Wiring Vercel AI SDK panels to auto-populate services database tables.
- [ ] **Phase 7: Live Deploy & GTM:** Custom domain mapping and live testing the `@nolosses` studio portal.

---

## 🔒 Safety & Deployment Protocols
- Local database instances use Docker configs. Production schemas enforce strict SSL certificates.
- Stripe client credentials are dynamically parsed through encrypted server actions.
