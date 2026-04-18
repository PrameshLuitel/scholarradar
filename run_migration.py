"""Run CRICOS migration directly using Supabase Management API"""
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

# Your Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
PROJECT_REF = "ewtcagefczcxmudjwogh"

print("Running CRICOS database migration...")
print(f"Project: {PROJECT_REF}")

# SQL to add CRICOS columns
sql_commands = """
-- Add CRICOS-specific columns to courses table
ALTER TABLE courses ADD COLUMN IF NOT EXISTS cricos_code TEXT;
ALTER TABLE courses ADD COLUMN IF NOT EXISTS provider_code TEXT;
ALTER TABLE courses ADD COLUMN IF NOT EXISTS state TEXT;

-- Add CRICOS-specific columns to universities table  
ALTER TABLE universities ADD COLUMN IF NOT EXISTS provider_code TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS state TEXT;

-- Add indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_courses_cricos_code ON courses(cricos_code) WHERE cricos_code IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_courses_state ON courses(state) WHERE state IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_courses_provider_code ON courses(provider_code) WHERE provider_code IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_universities_provider_code ON universities(provider_code) WHERE provider_code IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_universities_state ON universities(state) WHERE state IS NOT NULL;
"""

# Use the Supabase REST API to execute SQL
# We'll execute each command separately through the API
headers = {
    "apikey": SUPABASE_SERVICE_KEY,
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

# Execute SQL through pgbouncer using direct connection
# Since we can't run raw SQL via REST API, we'll use Python supabase client with RPC
from supabase import create_client

print("\nConnecting to Supabase...")
supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# Try to add columns using a different approach - execute via SQL function
# We'll create a temporary SQL execution function
print("\nAdding columns to courses table...")

# Test if columns exist first by trying to query them
try:
    result = supabase.table("courses").select("cricos_code").limit(1).execute()
    print("✓ cricos_code column already exists")
except Exception as e:
    if "42703" in str(e):
        print("✗ cricos_code column missing - need to create it")
        print("\nIMPORTANT: You need to run the SQL migration manually in Supabase Dashboard")
        print("Go to: https://app.supabase.com/project/ewtcagefczcxmudjwogh/sql/new")
        print("\nCopy and paste this SQL:")
        print(sql_commands)
    else:
        print(f"Error: {e}")
