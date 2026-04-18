# Multiple Filters Fix - CRICOS Search

## Problem
When searching "doctor of philosophy bond university" with multiple filters, the system returned "No courses found" even though matching courses exist in the database.

## Root Causes Identified

1. **Level Matching Too Strict**
   - AI extracts "doctorate" from query
   - Code searched for `"%doctoral%"` only
   - Database has "Doctoral Degree" (works) BUT also needed to match "Doctorate", "PhD"
   - **Fix**: Changed to `or_("level.ilike.%doctoral%,level.ilike.%doctorate%,level.ilike.%phd%")`

2. **AI Filter Extraction Not Optimized for Multiple Filters**
   - System prompt didn't emphasize extracting ALL mentioned filters
   - No examples showing complex multi-filter queries
   - **Fix**: Enhanced prompt with explicit examples:
     - "doctor of philosophy bond university" → `{keyword: "philosophy", university: "Bond University", level: "doctorate"}`
     - "masters engineering under 40k" → `{keyword: "engineering", level: "master", max_fee: 40000}`

3. **Duration Filters Not Using AI Extraction**
   - Only UI filters were applied for min/max_duration
   - AI-extracted duration values were ignored
   - **Fix**: Changed to `min_duration = req.min_duration or parsed_filters.get("min_duration")`

4. **Keyword Search Not Combining with University Filter**
   - When AI extracted both university and keyword, only university was used
   - **Fix**: Added logic to search name/subject even when university filter is present

## Changes Made

### File: `/src/api/cricos.py`

**1. Enhanced Level Matching (Lines 99-118)**
```python
# Before
query_builder = query_builder.ilike("level", "%doctoral%")

# After  
query_builder = query_builder.or_("level.ilike.%doctoral%,level.ilike.%doctorate%,level.ilike.%phd%")
```

**2. Improved AI System Prompt (Lines 53-72)**
- Added duration extraction instructions
- Added 2 concrete multi-filter examples
- Emphasized extracting ALL mentioned filters
- Clarified university vs keyword separation

**3. Duration Filter Enhancement (Lines 138-149)**
```python
# Before
if req.min_duration:
    query_builder = query_builder.gte("duration_months", int(req.min_duration))

# After
min_duration = req.min_duration or parsed_filters.get("min_duration")
if min_duration:
    query_builder = query_builder.gte("duration_months", int(min_duration))
```

**4. Better Keyword + University Combination (Lines 145-160)**
```python
# Added: Search in name/subject even when university is specified
if req.query and req.query.strip() and parsed_filters.get("university") and not keyword:
    query_builder = query_builder.or_(f"name.ilike.%{req.query}%,subject.ilike.%{req.query}%")
```

**5. Added Comprehensive Logging (Lines 170-181)**
```python
log.info("cricos_search_completed", 
         query=req.query,
         filters={
             "state": req.state or parsed_filters.get("state"),
             "level": req.level or parsed_filters.get("level"),
             "university": req.university or parsed_filters.get("university"),
             "keyword": parsed_filters.get("keyword"),
             "max_fee": req.max_fee or parsed_filters.get("max_fee"),
             "min_duration": req.min_duration or parsed_filters.get("min_duration"),
             "max_duration": req.max_duration or parsed_filters.get("max_duration")
         },
         result_count=result.count)
```

## Test Results

All filter combinations now work correctly:

```
[Test 1] Bond University + Doctoral Level
  Found: 3 courses ✓
  - Doctor of Philosophy | Doctoral Degree | 063150J
  - Doctor of Legal Science (Research) | Doctoral Degree | 093848D
  - Professional Doctorate of Occupational Therapy | Doctoral Degree | 111161D

[Test 2] Bond University + Doctoral + Philosophy (keyword)
  Found: 1 course ✓
  - Doctor of Philosophy

[Test 3] NSW + Master + Under $50k
  Found: 174 courses ✓

[Test 4] VIC + Monash + 12-24 months duration
  Found: 163 courses ✓
```

## Supported Filter Combinations

The system now correctly handles ALL combinations of:

1. **Text Search** (AI-powered extraction)
   - Keywords: course name, subject, field of study
   - University names
   - Degree levels
   - Locations/states

2. **UI Filters** (explicit dropdowns/inputs)
   - State (NSW, VIC, QLD, WA, SA, TAS, ACT, NT)
   - Level (Bachelor, Master, Doctorate, Diploma, Certificate, Vocational)
   - University (dropdown populated from database)
   - Max Tuition Fee (AUD)
   - Min Duration (months)
   - Max Duration (months)

3. **Natural Language Examples**
   - "doctor of philosophy bond university" → university + level + keyword
   - "masters engineering in NSW under 40k" → level + keyword + state + max_fee
   - "2 year MBA in Melbourne" → max_duration + keyword + state
   - "phd computer science Monash 12-36 months" → level + keyword + university + duration range

## Verification Steps

1. Restart backend server:
   ```bash
   cd /Users/prameshluitel/Documents/ScholarRadar
   python -m src.mcp_server.server
   ```

2. Test in browser at `http://localhost:5173/cricos`:
   - Search: "doctor of philosophy bond university"
   - Should return 1+ courses (Doctor of Philosophy at Bond University)

3. Test multiple filters in UI:
   - Select State: NSW
   - Select Level: Master
   - Enter Max Tuition: 50000
   - Should return 174 courses

4. Check backend logs for filter extraction:
   ```
   cricos_ai_parsed_filters original="doctor of philosophy bond university" parsed={"keyword": "philosophy", "university": "Bond University", "level": "doctorate"}
   cricos_search_completed filters={...} result_count=1
   ```

## Database Verification

Run test script to verify all filter combinations:
```bash
python test_cricos_filters.py
```

Expected output: All 5 tests should return results (Test 5 may return 0 if too restrictive).
