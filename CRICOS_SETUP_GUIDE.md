# CRICOS Scraper - Setup and Verification Guide

## Current Status

### What's Working:
- Scraper successfully downloads CRICOS data from data.gov.au
- Processes 1,548 universities/institutions
- Processes 26,172 courses
- Joins course locations to get state and city data
- Frontend table layout created to show all data at once

### What Needs to Be Done:

## STEP 1: Run Database Migration (REQUIRED)

You need to add contact information columns to the universities table.

**Option A: Run in Supabase Dashboard (Recommended)**
1. Go to: https://app.supabase.com/project/ewtcagefczcxmudjwogh/sql/new
2. Copy and paste this SQL:
```sql
ALTER TABLE universities ADD COLUMN IF NOT EXISTS phone_number TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS email_address TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS postal_address TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS institution_type TEXT;
```
3. Click **RUN**

**Option B: Use the provided script**
```bash
cd /Users/prameshluitel/Documents/ScholarRadar
python add_university_contact_columns.py
```
This will show you the SQL to run in Supabase.

## STEP 2: Re-run Enhanced CRICOS Scraper

After running the migration:
```bash
cd /Users/prameshluitel/Documents/ScholarRadar
python -m src.scrapers.cricos_enhanced_scraper
```

This will:
- Download latest CRICOS data from data.gov.au
- Process all 5 sheets (Institutions, Courses, Locations, Course Locations)
- Join course data with location data (state, city)
- Join university data with contact information (phone, email, website)
- Upsert 1,548 universities and 26,172 courses to database

## STEP 3: Verify Data

Run the verification script:
```bash
python verify_cricos_data.py
```

This will show:
- Total courses with CRICOS codes
- Total universities with provider codes
- Sample course data (should show state, city, fees, duration, etc.)
- Sample university data (should show website, phone, email, etc.)
- Distribution of courses by state

## STEP 4: Test the Frontend

1. Start the backend server:
```bash
python -m src.mcp_server.server
```

2. Start the frontend (in another terminal):
```bash
cd frontend
npm run dev
```

3. Visit: http://localhost:5173/cricos

You should see a comprehensive table with ALL this information in columns:
- Course Name
- Institution Name
- CRICOS Code
- Provider Code
- Course Level
- City/Location
- State
- Tuition Fee (AUD)
- Duration (months)
- Website Link
- Contact Phone
- Contact Email

## Data Flow

```
data.gov.au (Australian Government CRICOS Dataset)
    ↓
CRICOS Excel File (5 sheets: Institutions, Courses, Locations, Course Locations, Purpose Statement)
    ↓
cricos_enhanced_scraper.py (Downloads & Parses ALL sheets)
    ↓
Joins: Courses + Course Locations (gets state, city)
Joins: Courses + Institutions (gets provider details)
    ↓
Supabase Database (courses table with cricos_code, state, city, etc.)
Supabase Database (universities table with provider_code, website, phone, email, etc.)
    ↓
/api/cricos/search (API joins course + university data)
    ↓
/cricos Frontend (Displays all data in a comprehensive table)
```

## What's Different from CRICOS Website

The official CRICOS website shows institution details separately from courses. Our implementation shows EVERYTHING in one table for easy comparison:

**CRICOS Website:**
- Institution page: Shows provider code, contact details, website, address
- Course page: Shows course details separately
- Need to click between pages to see all info

**Our Implementation:**
- Single table view with ALL information at once
- Course name + Institution + CRICOS code + Provider code + Location + State + Fees + Duration + Website + Contact
- Easy to compare courses side-by-side
- Filter by state, level, search with AI

## Troubleshooting

**If state is still NULL after running scraper:**
1. Check if Course Locations sheet was processed: Look for log line "Course location map has X entries"
2. Verify course has a CRICOS code that matches entries in Course Locations sheet
3. Check the course_location_map in the scraper logs

**If contact info is NULL:**
1. Ensure you ran the SQL migration to add columns
2. Check if the Institutions sheet has phone/email columns (some datasets may not include this)
3. Verify the column names match what the scraper expects

**If courses don't show on /cricos page:**
1. Check browser console for errors
2. Verify API endpoint: http://localhost:10000/api/cricos/search (POST with body: {"page": 1, "page_size": 50})
3. Ensure courses have cricos_code populated (API filters for cricos_code IS NOT NULL)

## Files Modified

1. **Frontend**: `/frontend/src/pages/Cricos.jsx`
   - Changed from card-based UI to comprehensive table layout
   - Added state filter dropdown
   - Shows all data in columns (no expand/collapse needed)

2. **Backend API**: `/src/api/cricos.py`
   - Added university data enrichment
   - Joins course data with university contact information
   - Returns website, phone, email for each course

3. **Scraper**: `/src/scrapers/cricos_enhanced_scraper.py`
   - Enhanced to extract phone, email, postal address, institution type
   - Better logging to debug data joins
   - Processes all 5 CRICOS sheets

4. **Database Model**: `/src/database/models.py`
   - Added phone_number, email_address, postal_address, institution_type to University model

## Next Steps

1. Run SQL migration (STEP 1 above)
2. Re-run scraper (STEP 2 above)
3. Verify data (STEP 3 above)
4. Test frontend (STEP 4 above)
5. If everything works, the /cricos page will show all CRICOS data in a comprehensive table format similar to the official CRICOS website but with all information visible at once!
