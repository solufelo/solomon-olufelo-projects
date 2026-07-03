import { pgTable, uuid, text, timestamp, boolean, integer } from 'drizzle-orm/pg-core';

// Tenants / Agency accounts
export const tenants = pgTable('tenants', {
  id: uuid('id').defaultRandom().primaryKey(),
  name: text('name').notNull(),
  subdomain: text('subdomain').unique().notNull(),
  createdAt: timestamp('created_at').defaultNow().notNull(),
});

// User Profiles (Creators & Clients)
export const profiles = pgTable('profiles', {
  id: uuid('id').primaryKey(), // Maps to Supabase auth.users UUID
  tenantId: uuid('tenant_id').references(() => tenants.id),
  fullName: text('full_name').notNull(),
  email: text('email').unique().notNull(),
  role: text('role').default('client').notNull(), // 'admin' | 'creator' | 'client'
  createdAt: timestamp('created_at').defaultNow().notNull(),
});

// Booking Services
export const services = pgTable('services', {
  id: uuid('id').defaultRandom().primaryKey(),
  tenantId: uuid('tenant_id').references(() => tenants.id),
  title: text('title').notNull(),
  price: integer('price').notNull(), // represented in cents (e.g. 5000 = $50.00)
  durationMin: integer('duration_min').default(60).notNull(),
});

// Bookings
export const bookings = pgTable('bookings', {
  id: uuid('id').defaultRandom().primaryKey(),
  tenantId: uuid('tenant_id').references(() => tenants.id),
  clientId: uuid('client_id').references(() => profiles.id),
  serviceId: uuid('service_id').references(() => services.id),
  sessionDate: timestamp('session_date').notNull(),
  status: text('status').default('pending').notNull(), // 'pending' | 'confirmed' | 'cancelled'
  createdAt: timestamp('created_at').defaultNow().notNull(),
});
