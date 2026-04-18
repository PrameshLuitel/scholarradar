"""
Add contact information columns to universities table
Run this once to add the required columns for CRICOS data
"""
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY in .env file")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# SQL to add columns
sql_statements = """
ALTER TABLE universities ADD COLUMN IF NOT EXISTS phone_number TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS email_address TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS postal_address TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS institution_type TEXT;
"""

print("Adding contact information columns to universities table...")

try:
    # Execute SQL via Supabase RPC or direct query
    # Note: You may need to run this directly in Supabase SQL editor if RPC is not available
    print("\nPlease run the following SQL in your Supabase dashboard:")
    print("https://app.supabase.com/project/ewtcagefczcxmudjwogh/sql/new")
    print("\n" + "="*80)
    print(sql_statements)
    print("="*80)
    print("\nAfter running the SQL, re-run the CRICOS scraper:")
    print("python -m src.scrapers.cricos_enhanced_scraper")
    
except Exception as e:
    print(f"Error: {e}")
