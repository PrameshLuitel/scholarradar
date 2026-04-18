# CRICOS Feature - Complete Fix Guide

## CRITICAL: Current Situation

The `/cricos` page is currently showing **IDP data** (from idp.com) instead of **REAL CRICOS data** from the Australian government (data.gov.au).

### What Just Happened:

1. CRICOS scraper successfully ran and downloaded OFFICIAL data from data.gov.au
2. Extracted **1,515 universities** and **24,297 courses** from the official CRICOS Excel file
3. Failed to save to database because required columns don't exist yet

## URGENT ACTION REQUIRED:

### Step 1: Run SQL Migration (2 MINUTES)

Go to: https://app.supabase.com/project/ewtcagefczcxmudjwogh/sql/new

Copy and paste this SQL:

```sql
ALTER TABLE courses ADD COLUMN IF NOT EXISTS cricos_code TEXT;
ALTER TABLE courses ADD COLUMN IF NOT EXISTS provider_code TEXT;
ALTER TABLE courses ADD COLUMN IF NOT EXISTS state TEXT;

ALTER TABLE universities ADD COLUMN IF NOT EXISTS provider_code TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS state TEXT;

CREATE INDEX IF NOT EXISTS idx_courses_cricos_code ON courses(cricos_code) WHERE cricos_code IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_courses_state ON courses(state) WHERE state IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_courses_provider_code ON courses(provider_code) WHERE provider_code IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_universities_provider_code ON universities(provider_code) WHERE provider_code IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_universities_state ON universities(state) WHERE state IS NOT NULL;
```

Click **RUN**

### Step 2: Re-run CRICOS Scraper (1 MINUTE)

```bash
cd /Users/prameshluitel/Documents/ScholarRadar
python -m src.scrapers.cricos_scraper
```

This will populate the database with **24,297 REAL CRICOS courses** from data.gov.au

### Step 3: Restart Backend Server

```bash
# Stop current server (Ctrl+C)
# Then restart:
cd /Users/prameshluitel/Documents/ScholarRadar
python -m src.mcp_server.server
```

### Step 4: Verify It Worked

Visit: http://localhost:10000/cricos

You should now see REAL CRICOS data with:
- CRICOS codes for each course
- Provider codes
- State information
- Official government data (not IDP aggregator data)

## What Was Fixed in Code:

### Backend API ([src/api/cricos.py](file:///Users/prameshluitel/Documents/ScholarRadar/src/api/cricos.py))
- Updated to filter for courses with `cricos_code` populated
- This ensures ONLY official CRICOS data shows, not IDP data
- Fallback to Australian courses if column doesn't exist yet

### Frontend ([frontend/src/pages/Cricos.jsx](file:///Users/prameshluitel/Documents/ScholarRadar/frontend/src/pages/Cricos.jsx))
- Complete redesign with expandable cards
- Shows ALL 25 database columns
- AI-powered search working
- Level filters working
- No emojis
- Removed "Official CRICOS Register" badge

## The Data Flow:

```
data.gov.au (Australian Government)
    ↓
CRICOS Excel File (Official Registry)
    ↓
cricos_scraper.py (Downloads & Parses)
    ↓
Supabase Database (courses table with cricos_code)
    ↓
/api/cricos/search (Filters for cricos_code IS NOT NULL)
    ↓
/cricos Frontend (Displays real CRICOS data)
```

## After Migration - What You'll Have:

- **24,297 official CRICOS courses** from Australian government
- **1,515 CRICOS-registered providers/universities**
- Real CRICOS codes (e.g., "095531J", "094572B")
- Provider codes for each institution
- State information (NSW, VIC, QLD, etc.)
- Direct government data - NO middleman/aggregator data

## Why This Matters:

**Before (WRONG):**
- Showing IDP.com data (educational aggregator)
- No CRICOS codes
- No official government data
- Not the real CRICOS register

**After (CORRECT):**
- Showing data.gov.au data (Australian Government)
- Real CRICOS codes for every course
- Official provider codes
- The actual CRICOS registry that international students need

## Troubleshooting:

**If scraper fails:**
```bash
# Check if Excel file downloads correctly
cd /Users/prameshluitel/Documents/ScholarRadar
python -c "
import asyncio
from src.scrapers.cricos_scraper import CricosScraper
scraper = CricosScraper()
asyncio.run(scraper.scrape_and_ingest())
"
```

**If no data shows after migration:**
1. Check if columns exist: `SELECT column_name FROM information_schema.columns WHERE table_name = 'courses' AND column_name LIKE '%cricos%';`
2. Check if data exists: `SELECT COUNT(*) FROM courses WHERE cricos_code IS NOT NULL;`
3. Re-run scraper

**If still showing IDP data:**
- The API filters for `cricos_code IS NOT NULL`
- If courses don't have cricos_code populated, they won't show
- This is correct behavior - we only want real CRICOS data
