import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';
import * as schema from './schema';

const connectionString = process.env.DATABASE_URL || 'postgresql://postgres:postgres@localhost:5432/postgres';

// Disable prefetch as prepared statements are not supported in Supabase transaction pooling mode
export const client = postgres(connectionString, { prepare: false });
export const db = drizzle(client, { schema });
export * from './schema';
