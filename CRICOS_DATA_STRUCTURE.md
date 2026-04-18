# CRICOS Data Structure - Complete Documentation

## Data Source
**Official Australian Government CRICOS Dataset**
- URL: https://data.gov.au/data/dataset/cricos
- Format: Excel (.xlsx) file updated monthly
- Scraped automatically via GitHub Actions (monthly_cricos_scraper.yml)

## Excel File Structure (5 Sheets)

### 1. Purpose Statement (Metadata - Ignored)
- Contains information about CRICOS and generation date
- Not imported into database

### 2. Institutions (1,548 providers)
**Primary key**: CRICOS Provider Code

Columns:
- CRICOS Provider Code (e.g., "00001K", "00002J")
- Trading Name
- Institution Name
- Institution Type (Government, Private, etc.)
- Institution Capacity (student count)
- Website
- Postal Address (Lines 1-4, City, State, Postcode)

**Saved to**: `universities` table

### 3. Courses (26,172 courses)
**Primary key**: CRICOS Course Code

Columns:
- CRICOS Provider Code (FK to Institutions)
- Institution Name
- **CRICOS Course Code** (e.g., "078241E", "089976G") - Unique identifier
- Course Name
- VET National Code (for vocational courses)
- Dual Qualification
- **Field of Education 1**: Broad, Narrow, Detailed (Subject categories)
- **Field of Education 2**: Broad, Narrow, Detailed (Secondary subjects)
- **Course Level** (e.g., "Bachelor", "Master", "Diploma", "Certificate IV")
- Foundation Studies (Yes/No)
- Work Component (Yes/No, Hours/Week, Weeks, Total Hours)
- Course Language (usually "English")
- **Duration (Weeks)** - Converted to months in our DB
- **Tuition Fee** (in AUD)
- Non Tuition Fee
- Estimated Total Course Cost
- Expired (Yes/No)

**Saved to**: `courses` table with cricos_code, provider_code, level, duration_months, tuition_fee, subject_category, subject

### 4. Locations (3,907 locations)
**Links**: Provider Code → Physical addresses

Columns:
- CRICOS Provider Code (FK to Institutions)
- Institution Name
- Location Name (e.g., "Main Campus", "City Campus")
- Location Type
- Full Address (Lines 1-4, City, State, Postcode)

**Purpose**: Maps where providers have campuses

### 5. Course Locations (46,483 rows) - **LINKING TABLE**
**Critical for joining**: Course → Location with State

Columns:
- CRICOS Provider Code
- Institution Name  
- **CRICOS Course Code** (FK to Courses)
- Location Name
- **Location City**
- **Location State** (NSW, VIC, QLD, WA, SA, TAS, ACT, NT)

**This is how we get state data for each course!**

## How Data is Combined

```
Courses Table
    ↓ (JOIN on CRICOS Course Code)
Course Locations Table → Gets: State, City
    ↓
Institutions Table → Gets: Provider details, website, address
    
Final Result: Each course has:
- Name, CRICOS code, provider code
- University name
- State & City (from Course Locations)
- Level, duration, tuition fee
- Subject categories (Field of Education)
- IELTS requirements (if available from other sources)
```

## Current Database Schema

### `courses` table (24,297 CRICOS courses)
- id (UUID)
- name (Course name)
- university (Institution name)
- country ("Australia")
- city (From Course Locations)
- level (Course Level from Excel)
- subject (Field of Education Narrow)
- subject_category (Field of Education Broad)
- duration_months (Converted from weeks)
- tuition_fee (AUD)
- currency ("AUD")
- **cricos_code** (CRICOS Course Code - Primary identifier)
- **provider_code** (CRICOS Provider Code - Links to university)
- **state** (From Course Locations - Currently NULL, needs fix)
- is_active (True)
- created_at, updated_at, last_verified

### `universities` table (1,515 CRICOS providers)
- id (UUID)
- name (Institution name)
- country ("Australia")
- city (From postal address)
- **provider_code** (CRICOS Provider Code - Primary identifier)
- **state** (From postal address)
- website
- total_students (Institution capacity)
- created_at, updated_at

## What's Working Now

✅ **24,297 official CRICOS courses** from data.gov.au
✅ **Real CRICOS codes** (government identifiers)
✅ **Provider codes** for all institutions
✅ **1,515 universities** with provider information
✅ **Course levels** (Bachelor, Master, Diploma, etc.)
✅ **Tuition fees** in AUD
✅ **Duration** in months
✅ **Subject categories** (Field of Education)
✅ **Monthly automatic updates** via GitHub Actions

## What Needs Fixing

❌ **State data** not populated for courses (Course Locations sheet not properly joined)
❌ **City data** for courses needs to come from Course Locations
✅ **Deduplication** issue in enhanced scraper needs fix

## Next Steps to Complete

1. Fix the bulk_upsert function to handle duplicate course codes properly
2. Re-run enhanced scraper to populate state and city from Course Locations sheet
3. Verify all 26,172 courses have state data populated
4. Update API filters to work with state data once available

## Data Freshness

- **Scraped**: Monthly (1st of each month at midnight UTC)
- **Source**: data.gov.au (official Australian government)
- **Last updated**: April 18, 2026
- **Next update**: May 1, 2026 (automatic)

## Key Differences from IDP Data

| Aspect | IDP Data (WRONG) | CRICOS Data (CORRECT) |
|--------|-----------------|----------------------|
| Source | idp.com (aggregator) | data.gov.au (government) |
| CRICOS Codes | ❌ None | ✅ Official codes |
| Provider Codes | ❌ None | ✅ Official codes |
| State Data | ❌ Missing | ✅ Available (needs fix) |
| Course Count | 21,537 AU courses | 26,172 CRICOS courses |
| Authority | Third-party | Official registry |
| Visa Verification | ❌ Not authoritative | ✅ Official for student visas |
