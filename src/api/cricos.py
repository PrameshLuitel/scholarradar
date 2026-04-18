import json
import re
from typing import Optional

import structlog
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

from src.database.client import get_db

log = structlog.get_logger("api.cricos")

app = FastAPI(title="CRICOS Database API")

class CricosSearchRequest(BaseModel):
    query: Optional[str] = None
    state: Optional[str] = None
    level: Optional[str] = None
    university: Optional[str] = None
    max_fee: Optional[float] = None
    min_duration: Optional[int] = None
    max_duration: Optional[int] = None
    page: int = 1
    page_size: int = 50

@app.get("/universities")
async def get_universities():
    try:
        db = get_db()
        # Get unique universities from courses table with CRICOS codes
        result = db.table("courses").select("university").not_.is_("cricos_code", "null").execute()
        
        # Extract unique university names and sort them
        if result.data:
            unique_unis = sorted(list(set([c['university'] for c in result.data if c.get('university')])))
            return {"data": [{"name": name} for name in unique_unis]}
        return {"data": []}
    except Exception as e:
        log.error("universities_fetch_failed", error=str(e))
        return {"error": str(e), "data": []}

@app.post("/search")
async def search_cricos(req: CricosSearchRequest):
    try:
        db = get_db()
        parsed_filters = {}
        
        # 1. Smart filter extraction - regex first (0 tokens), AI fallback (<50 tokens)
        if req.query and req.query.strip():
            query_lower = req.query.lower().strip()
            import re as regex_module
            
            # FAST PATH: Regex-based extraction (0 tokens, instant)
            # City→State mapping
            city_state_map = {
                'sydney': 'NSW', 'melbourne': 'VIC', 'brisbane': 'QLD', 'perth': 'WA',
                'adelaide': 'SA', 'hobart': 'TAS', 'canberra': 'ACT', 'darwin': 'NT'
            }
            for city, state in city_state_map.items():
                if city in query_lower:
                    parsed_filters['state'] = state
                    break
            
            # Direct state mentions (word boundary match to avoid false positives)
            for st in ['NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS', 'ACT', 'NT']:
                # Use word boundary to avoid matching 'nt' in 'intelligence', 'act' in 'action', etc.
                if regex_module.search(r'\b' + st.lower() + r'\b', query_lower):
                    parsed_filters['state'] = st
                    break
            
            # Level extraction
            if any(x in query_lower for x in ['bachelor', 'undergrad', 'b.a', 'b.s']):
                parsed_filters['level'] = 'bachelor'
            elif any(x in query_lower for x in ['postgrad', 'postgraduate']):
                parsed_filters['level'] = 'master'
            elif 'mba' in query_lower or 'msba' in query_lower:
                # MBA/MSBA are master's degrees, but don't set level here - let keyword handle it
                pass
            elif 'master' in query_lower or query_lower.endswith(' ms') or 'ma ' in query_lower or ' msc' in query_lower or query_lower.endswith(' msc'):
                parsed_filters['level'] = 'master'
            elif any(x in query_lower for x in ['phd', 'doctorate', 'doctor of', 'ph.d']):
                parsed_filters['level'] = 'doctorate'
            elif 'diploma' in query_lower:
                parsed_filters['level'] = 'diploma'
            elif any(x in query_lower for x in ['certificate', 'cert ']):
                parsed_filters['level'] = 'certificate'
            
            # Fee extraction (patterns: "under 50k", "below 40000", "less than 30k")
            fee_patterns = [
                r'(?:under|below|less than|upto|up to|max|maximum)\s*\$?\s*(\d+(?:\.\d+)?)(k|k\b|000)?',
                r'\$?(\d+(?:\.\d+)?)(k|k\b|000)\s*(?:aud|dollars)?(?:\s|$)'
            ]
            for pattern in fee_patterns:
                fee_match = regex_module.search(pattern, query_lower)
                if fee_match:
                    amount = float(fee_match.group(1))
                    suffix = fee_match.group(2) or ''
                    if 'k' in suffix.lower():
                        amount *= 1000
                    parsed_filters['max_fee'] = amount
                    break
            
            # Fee intent words (cheap, affordable, budget)
            if not parsed_filters.get('max_fee'):
                if any(x in query_lower for x in ['cheap', 'affordable', 'low cost', 'budget', 'inexpensive', 'low-price']):
                    parsed_filters['max_fee'] = 25000  # Default "cheap" threshold
                elif any(x in query_lower for x in ['moderate', 'reasonable', 'mid-range', 'mid range']):
                    parsed_filters['max_fee'] = 40000  # Default "moderate" threshold
            
            # Duration extraction (patterns: "2 years", "24 months", "1-2 years")
            duration_patterns = [
                (r'(?:min|minimum|at least|from)\s*(\d+)\s*(?:months?|mo\b)', 'min_duration', 1),
                (r'(?:max|maximum|up to|upto|under|less than)\s*(\d+)\s*(?:months?|mo\b)', 'max_duration', 1),
                (r'(\d+)\s*[-–to]+\s*(\d+)\s*(?:months?|mo\b)', 'duration_range', None),
                (r'(?:min|minimum|at least)\s*(\d+)\s*(?:years?|yr\b)', 'min_duration', 12),
                (r'(?:max|maximum|up to|upto)\s*(\d+)\s*(?:years?|yr\b)', 'max_duration', 12),
            ]
            for pattern, field, multiplier in duration_patterns:
                dur_match = regex_module.search(pattern, query_lower)
                if dur_match:
                    if field == 'duration_range':
                        parsed_filters['min_duration'] = int(dur_match.group(1)) * (multiplier or 1)
                        parsed_filters['max_duration'] = int(dur_match.group(2)) * (multiplier or 1)
                    else:
                        parsed_filters[field] = int(dur_match.group(1)) * multiplier
                    break
            
            # University extraction - common Australian unis
            uni_patterns = [
                (r'\b(university\s+of\s+\w+)', 'full'),
                (r'\b(monash|unsw|uts|rmit|deakin|qut|uq|usyd|unimelb|anu|murdoch|ecu|flinders|cdu|utas|bond|macquarie|griffith|latrobe|uwa|unisa|victoria|swinburne|jcu|csu|scu|usc|uon|uow|acu|nd|cqu)', 'short')
            ]
            for pattern, uni_type in uni_patterns:
                uni_match = regex_module.search(pattern, query_lower)
                if uni_match:
                    parsed_filters['university'] = uni_match.group(1).title()
                    break
            
            # Keyword extraction - remove known filter terms, keep the rest
            filter_terms = [
                'in', 'at', 'for', 'of', 'under', 'below', 'above', 'less', 'than', 'up', 'to',
                'sydney', 'melbourne', 'brisbane', 'perth', 'adelaide', 'hobart', 'canberra', 'darwin',
                'nsw', 'vic', 'qld', 'wa', 'sa', 'tas', 'act', 'nt',
                'bachelor', 'master', 'phd', 'doctorate', 'diploma', 'certificate',
                'undergrad', 'postgrad', 'postgraduate',
                'months', 'month', 'years', 'year', 'yrs', 'yr',
                'university', 'uni', 'college', 'institute',
                'monash', 'unsw', 'uts', 'rmit', 'deakin', 'qut', 'uq', 'usyd', 'unimelb', 'anu',
                'bond', 'macquarie', 'griffith', 'latrobe', 'uwa', 'unisa', 'victoria', 'swinburne'
            ]
            # Extract potential keywords (2+ letter words not in filter terms)
            words = regex_module.findall(r'\b[a-z]{2,}\b', query_lower)
            keywords = [w for w in words if w not in filter_terms and w not in city_state_map]
            if keywords:
                # Join remaining meaningful terms as keyword
                parsed_filters['keyword'] = ' '.join(keywords[:3])  # Max 3 keywords
            
            # SLOW PATH: AI enhancement ALWAYS runs to extract semantic meaning
            # This ensures complex queries work even if regex got some filters
            from src.utils.groq_cascade import non_streaming_groq
            
            system = """You are a search query analyzer for Australian CRICOS courses. Extract ALL possible filters from ANY type of query.

YOUR GOAL: Understand the user's INTENT, not just keywords. Think like a human counselor.

IMPORTANT: Fix typos and misspellings automatically!
- "sceince" → "science", "data sceince" → "data science"
- "engeneering" → "engineering", "nursng" → "nursing"
- "busines" → "business", "computr" → "computer"
- "queensland" → "QLD", "victoria" → "VIC", "new south wales" → "NSW"
- ANY misspelled field of study, location, or term should be corrected

CRITICAL RULES FOR DEGREE TYPES:
- "MBA" or "mba" → keyword: "MBA business administration" (KEEP "MBA" in keyword!)
- "MSBA" or "msba" → keyword: "MSBA business analytics" (KEEP "MSBA" in keyword!)
- "MSC" or "msc" → keyword: "MSc science" 
- "MA" or "ma" → keyword: "MA arts"
- DO NOT remove MBA, MSBA, MSC, MA from keyword - they are important search terms!

LOCATION MAPPING (CRITICAL - understand ALL variations):
- Full state names: "queensland"→"QLD", "victoria"→"VIC", "new south wales"→"NSW", "western australia"→"WA", "south australia"→"SA", "tasmania"→"TAS", "australian capital territory"→"ACT", "northern territory"→"NT"
- Cities: "sydney"→"NSW", "melbourne"→"VIC", "brisbane"→"QLD", "perth"→"WA", "adelaide"→"SA", "hobart"→"TAS", "canberra"→"ACT", "darwin"→"NT"
- Regional: "gold coast"→"QLD", "sunshine coast"→"QLD", "newcastle"→"NSW", "wollongong"→"NSW", "geelong"→"VIC", "cairns"→"QLD", "townsville"→"QLD"
- "in Queensland", "at Sydney", "near Melbourne", "around Perth" → extract state
- "east coast", "west coast" → infer multiple states if ambiguous

FEE INTENT RECOGNITION (understand context):
- "cheap", "affordable", "low cost", "budget", "inexpensive", "lowest fees" → max_fee: 25000
- "moderate", "reasonable", "mid-range", "average" → max_fee: 40000
- "premium", "expensive", "high-end", "top-tier" → NO fee filter (show all, including expensive)
- "under 50k", "below 40000", "less than 30k", "within 35000" → extract exact number
- "scholarship", "fully funded", "free" → max_fee: 0 (special case)

DURATION INTENT:
- "short", "quick", "fast", "accelerated" → max_duration: 12 (1 year)
- "long", "extended", "comprehensive" → min_duration: 24 (2 years)
- "2 years", "24 months", "3 year", "18 months" → extract exact duration
- "fast-track", "intensive" → max_duration: 12

CAREER/GOAL-BASED QUERIES (understand intent):
- "I want to become a nurse" → keyword: "nursing"
- "become a software engineer" → keyword: "computer science software engineering"
- "work in AI" → keyword: "artificial intelligence"
- "career in data" → keyword: "data science analytics"
- "job in business" → keyword: "business administration management"
- "teaching career" → keyword: "education teaching"
- "psychologist" → keyword: "psychology"
- "doctor", "physician" → keyword: "medicine medical"
- "lawyer", "attorney" → keyword: "law legal"

UNIVERSITY PREFERENCES:
- "Group of Eight", "Go8", "top universities", "prestigious" → NO specific filter (show top unis)
- "regional universities", "outside major cities" → exclude Sydney/Melbourne/Brisbane
- Specific unis: "Monash", "UNSW", "University of Sydney", "USYD", "UniMelb", "ANU", "UQ", "RMIT", "QUT", "Deakin", "Macquarie", "UTS", "Bond", "La Trobe", "Griffith", "Flinders", "Curtin", "UWA", "University of Melbourne"

COURSE CODE DETECTION:
- CRICOS codes: 6 digits (e.g., "098765", "123456") or 1 letter + 5 digits (e.g., "A12345")
- If found, add to keyword for exact matching

AVAILABLE FIELDS TO EXTRACT:
- state: NSW, VIC, QLD, WA, SA, TAS, ACT, NT
- level: bachelor, master, doctorate, diploma, certificate, vocational
- max_fee: number in AUD (cheap→25000, under 50k→50000)
- min_duration: number in months
- max_duration: number in months
- university: institution name (exact or partial)
- keyword: course name, subject, field of study, course code, career goal, ANY search terms

EXTRACTION RULES:
1. ALWAYS fix typos/misspellings before extracting
2. Extract EVERYTHING mentioned - be thorough and liberal
3. KEEP degree abbreviations (MBA, MSBA, MSC, MA) in keyword - critical for search!
4. Map ALL location names (full names, abbreviations, cities, regions) to state codes
5. Recognize fee intent words (cheap, affordable, budget) and set max_fee
6. Handle course codes - keep in keyword for exact matching
7. Convert career goals to fields of study ("become a nurse" → "nursing")
8. Handle "OR" queries: "data science or engineering" → keyword:"data science engineering"
9. Understand "I want to study X", "looking for X", "interested in X" → X is keyword
10. Handle comparative: "better than", "vs", "compare" → NO filter, just search both
11. For ambiguous queries, extract what you can and let search handle the rest
12. Return ONLY valid JSON with fields you found (omit fields not mentioned)

QUERY TYPE EXAMPLES:

**Simple Course Search:**
- "msba" → {"keyword": "MSBA business analytics"}
- "mba" → {"keyword": "MBA business administration"}
- "engineering" → {"keyword": "engineering"}
- "data science" → {"keyword": "data science"}

**Location-Based:**
- "msba in sydney" → {"keyword": "MSBA business analytics", "state": "NSW"}
- "engineering courses in Queensland" → {"keyword": "engineering", "state": "QLD"}
- "cheap nursing in melbourne" → {"keyword": "nursing", "state": "VIC", "max_fee": 25000}
- "IT courses Perth" → {"keyword": "IT information technology", "state": "WA"}
- "Victoria universities" → {"state": "VIC", "keyword": "bachelor"}

**Fee-Conscious:**
- "msba in sydney under 50k" → {"keyword": "MSBA business analytics", "state": "NSW", "max_fee": 50000, "level": "master"}
- "affordable engineering" → {"keyword": "engineering", "max_fee": 25000}
- "cheap MBA courses" → {"keyword": "MBA business administration", "max_fee": 25000}
- "budget friendly data science" → {"keyword": "data science", "max_fee": 25000}

**Career/Goal-Based:**
- "I want to become a nurse" → {"keyword": "nursing"}
- "want to work in AI" → {"keyword": "artificial intelligence"}
- "career in software engineering" → {"keyword": "software engineering computer science"}
- "I want to be a psychologist" → {"keyword": "psychology"}
- "become a doctor" → {"keyword": "medicine medical"}

**Duration-Based:**
- "short business courses in Sydney" → {"keyword": "business", "state": "NSW", "max_duration": 12}
- "quick MBA programs" → {"keyword": "MBA business administration", "max_duration": 12}
- "2 year masters in Melbourne" → {"keyword": "masters", "state": "VIC", "min_duration": 24, "max_duration": 24}

**University-Specific:**
- "phd computer science monash" → {"level": "doctorate", "keyword": "computer science", "university": "Monash"}
- "MBA at UNSW" → {"keyword": "MBA business administration", "university": "UNSW", "level": "master"}
- "University of Sydney engineering" → {"keyword": "engineering", "university": "University of Sydney"}

**Complex Multi-Filter:**
- "I want to do an engineering course in queensland for cheap" → {"keyword": "engineering", "state": "QLD", "max_fee": 25000}
- "affordable IT masters in Perth under 2 years" → {"keyword": "IT information technology", "state": "WA", "level": "master", "max_fee": 25000, "max_duration": 24}
- "cheap bachelor nursing in Adelaide" → {"keyword": "nursing", "state": "SA", "level": "bachelor", "max_fee": 25000}

**Course Codes:**
- "098765" → {"keyword": "098765"}
- "course code 123456" → {"keyword": "123456"}

**Multiple Subjects (OR):**
- "data science or AI masters" → {"keyword": "data science artificial intelligence", "level": "master"}
- "engineering or computer science" → {"keyword": "engineering computer science"}

**Typo Corrections:**
- "DATA SCEINCE OR engineering" → {"keyword": "data science engineering"}
- "computr sceince masters" → {"keyword": "computer science", "level": "master"}
- "nursng courses in Sydney" → {"keyword": "nursing", "state": "NSW"}

**Natural Conversational:**
- "I'm looking for affordable psychology programs in Adelaide" → {"keyword": "psychology", "state": "SA", "max_fee": 25000}
- "Can you find me cheap business courses in Brisbane?" → {"keyword": "business", "state": "QLD", "max_fee": 25000}
- "Show me MBA programs under 40k" → {"keyword": "MBA business administration", "max_fee": 40000, "level": "master"}
- "What are some good data science courses in Melbourne?" → {"keyword": "data science", "state": "VIC"}
"""
            user = f"Query: {req.query}"
            
            try:
                res = await non_streaming_groq(system, user, max_tokens=120, temperature=0.1)
                content = res.get("content", "{}").strip()
                content = regex_module.sub(r'^```(?:json)?\s*', '', content)
                content = regex_module.sub(r'\s*```$', '', content)
                ai_filters = json.loads(content)
                
                # Smart merge: AI overrides regex for better accuracy
                for key, val in ai_filters.items():
                    if val and val not in ['all', 'any', '']:
                        parsed_filters[key] = val
                
                log.info("cricos_ai_enhanced", query=req.query, regex_filters=len(parsed_filters), ai_filters=parsed_filters)
            except Exception as e:
                log.warning("cricos_ai_enhancement_failed", error=str(e))
                # If AI fails, keep regex filters
        
        # 2. Build Supabase Query
        # Target ONLY CRICOS courses (from data.gov.au) - courses with cricos_code populated
        # Once migration runs and scraper populates data, this will show real CRICOS data
        query_builder = db.table("courses").select("*", count="exact")
        
        # Filter for courses that have CRICOS codes (official government data)
        # Using not_.is_() to filter out NULL cricos_code values
        # This ensures we only show real CRICOS data, not IDP data
        try:
            query_builder = query_builder.not_.is_("cricos_code", "null")
        except:
            # If column doesn't exist yet, fallback to Australian courses
            query_builder = query_builder.eq("country", "australia")
        
        # Apply combined filters (Explicit UI filters take precedence over AI filters)
        state_filter = req.state or parsed_filters.get("state")
        if state_filter and state_filter.lower() not in ["all", "any", ""]:
            query_builder = query_builder.ilike("state", f"%{state_filter}%")
            
        level_filter = req.level or parsed_filters.get("level")
        if level_filter and level_filter.lower() not in ["all", "any", ""]:
            # Standardize level - more comprehensive mapping
            lvl = level_filter.lower()
            if any(k in lvl for k in ('undergrad', 'bachelor', 'b.a', 'b.s', 'bachelor degree')):
                query_builder = query_builder.or_("level.ilike.%bachelor%,level.ilike.%undergraduate%")
            elif any(k in lvl for k in ('postgrad', 'master', 'mba', 'master degree')):
                query_builder = query_builder.or_("level.ilike.%master%,level.ilike.%postgraduate%")
            elif any(k in lvl for k in ('doctorate', 'phd', 'doctor', 'doctoral')):
                # Match both "Doctoral Degree" and "Doctorate" 
                query_builder = query_builder.or_("level.ilike.%doctoral%,level.ilike.%doctorate%,level.ilike.%phd%")
            elif any(k in lvl for k in ('diploma', 'advanced diploma')):
                query_builder = query_builder.or_("level.ilike.%diploma%")
            elif any(k in lvl for k in ('certificate', 'cert')):
                query_builder = query_builder.or_("level.ilike.%certificate%")
            elif 'vocational' in lvl or 'vet' in lvl:
                query_builder = query_builder.or_("level.ilike.%vocational%")
            else:
                # Fallback: search for the exact level term
                query_builder = query_builder.ilike("level", f"%{level_filter}%")
        
        # University filter (UI filter takes precedence, but also check AI extraction)
        university_filter = req.university or parsed_filters.get("university")
        if university_filter and university_filter.lower() not in ["all", "any", ""]:
            query_builder = query_builder.ilike("university", f"%{university_filter}%")
                
        max_fee = req.max_fee or parsed_filters.get("max_fee")
        if max_fee:
            try:
                max_fee_float = float(max_fee)
                query_builder = query_builder.lte("tuition_fee", max_fee_float)
            except ValueError:
                pass
        
        # Duration filters (UI filters take precedence, but also check AI extraction)
        min_duration = req.min_duration or parsed_filters.get("min_duration")
        if min_duration:
            try:
                query_builder = query_builder.gte("duration_months", int(min_duration))
            except ValueError:
                pass
        
        max_duration = req.max_duration or parsed_filters.get("max_duration")
        if max_duration:
            try:
                query_builder = query_builder.lte("duration_months", int(max_duration))
            except ValueError:
                pass
                
        keyword = parsed_filters.get("keyword")
        if keyword:
            # Expand keyword with common abbreviations/synonyms
            keyword_expansions = {
                'msba': 'MSBA business analytics',
                'mba': 'MBA business administration',
                'msc': 'MSc science',
                'ma': 'MA arts',
                'bba': 'BBA business administration',
                'bs': 'BSc science',
                'ba': 'BA arts',
                'it': 'IT information technology',
                'cs': 'CS computer science',
                'ai': 'AI artificial intelligence',
                'ml': 'ML machine learning',
                'ds': 'DS data science',
                'biz': 'business',
                'eng': 'engineering',
                'psy': 'psychology',
                'edu': 'education',
                'nurs': 'nursing',
                'med': 'medicine',
                'law': 'law',
                'arch': 'architecture',
                'design': 'design',
                'finance': 'finance',
                'account': 'accounting',
                'marketing': 'marketing',
                'management': 'management',
            }
            
            keyword_lower = keyword.lower()
            search_terms = [keyword]
            
            # Add expansions if keyword matches abbreviation
            for abbrev, full in keyword_expansions.items():
                if abbrev in keyword_lower or keyword_lower in abbrev:
                    search_terms.append(full)
                    break
            
            # Split keyword by " or " to handle multiple subjects
            if ' or ' in keyword_lower:
                or_parts = [p.strip() for p in keyword.split(' or ')]
                search_terms.extend(or_parts)
            
            # Handle plurals and variations (engineering→engineer, sciences→science)
            additional_terms = []
            for term in search_terms:
                # Remove common suffixes
                if term.endswith('s') and not term.endswith('ss'):
                    additional_terms.append(term[:-1])  # engineeringS → engineering
                if term.endswith('ing'):
                    additional_terms.append(term[:-3] if len(term) > 4 else term)  # engineerING → engineer
                if term.endswith('ion'):
                    additional_terms.append(term[:-3])  # informatION → informat
                # Handle "Master of X" or "Bachelor of X" patterns
                if 'master of ' in keyword_lower or 'bachelor of ' in keyword_lower:
                    # Extract the subject after "of"
                    import re as re_module
                    of_match = re_module.search(r'(?:master|bachelor) of (.+)', keyword_lower)
                    if of_match:
                        additional_terms.append(of_match.group(1).strip())
            search_terms.extend(additional_terms)
            
            # Remove duplicates while preserving order
            seen = set()
            unique_terms = []
            for term in search_terms:
                if term not in seen:
                    seen.add(term)
                    unique_terms.append(term)
            search_terms = unique_terms
            
            # Build OR query for all search terms
            or_conditions = []
            for term in search_terms:
                or_conditions.append(f"name.ilike.%{term}%")
                or_conditions.append(f"subject.ilike.%{term}%")
                # Also search in level for degree types like MBA, MSBA
                if len(term) <= 10:  # Short terms like MBA, MSBA
                    or_conditions.append(f"level.ilike.%{term}%")
                # Search in cricos_code for exact course codes
                if re.match(r'^\d{5,6}$', term) or re.match(r'^[A-Z]\d{5}$', term, re.IGNORECASE):
                    or_conditions.append(f"cricos_code.ilike.%{term}%")
            
            query_builder = query_builder.or_(",".join(or_conditions))
        
        # If user typed a query but AI didn't extract keyword, try broad search
        if req.query and req.query.strip() and not keyword and not parsed_filters.get("university"):
            # Search across name, university, and subject
            query_builder = query_builder.or_(f"name.ilike.%{req.query}%,university.ilike.%{req.query}%,subject.ilike.%{req.query}%")
        
        # Check if user wants sorting by fees (cheap, affordable, lowest fees)
        sort_by_fee = False
        if req.query:
            query_lower = req.query.lower()
            sort_by_fee = any(x in query_lower for x in ['cheap', 'affordable', 'lowest', 'budget', 'inexpensive', 'low cost'])
            
        # Pagination
        offset = (req.page - 1) * req.page_size
        
        # Apply sorting - if "cheap" is mentioned, sort by fees ascending
        if sort_by_fee:
            query_builder = query_builder.order("tuition_fee", desc=False)  # Lowest to highest
        
        query_builder = query_builder.range(offset, offset + req.page_size - 1)
        
        result = query_builder.execute()
        
        # PROGRESSIVE RELAXATION: If 0 results, try with relaxed filters
        if result.count == 0 and req.page == 1 and req.query:
            log.info("cricos_zero_results_relaxing", query=req.query, original_filters=parsed_filters)
            
            # Try without keyword first (keep structural filters)
            if keyword:
                relaxed_builder = db.table("courses").select("*", count="exact")
                try:
                    relaxed_builder = relaxed_builder.not_.is_("cricos_code", "null")
                except:
                    relaxed_builder = relaxed_builder.eq("country", "australia")
                
                # Apply only structural filters (state, level, university, fee, duration)
                if parsed_filters.get("state"):
                    relaxed_builder = relaxed_builder.ilike("state", f"%{parsed_filters['state']}%")
                if parsed_filters.get("level"):
                    lvl = parsed_filters['level'].lower()
                    if 'bachelor' in lvl:
                        relaxed_builder = relaxed_builder.or_("level.ilike.%bachelor%,level.ilike.%undergraduate%")
                    elif 'master' in lvl:
                        relaxed_builder = relaxed_builder.or_("level.ilike.%master%,level.ilike.%postgraduate%")
                    elif any(x in lvl for x in ['doctor', 'phd']):
                        relaxed_builder = relaxed_builder.or_("level.ilike.%doctoral%,level.ilike.%doctorate%")
                if parsed_filters.get("university"):
                    relaxed_builder = relaxed_builder.ilike("university", f"%{parsed_filters['university']}%")
                if parsed_filters.get("max_fee"):
                    relaxed_builder = relaxed_builder.lte("tuition_fee", float(parsed_filters['max_fee']))
                
                relaxed_builder = relaxed_builder.range(offset, offset + req.page_size - 1)
                relaxed_result = relaxed_builder.execute()
                
                if relaxed_result.count > 0:
                    result = relaxed_result
                    log.info("cricos_relaxed_no_keyword", query=req.query, relaxed_count=relaxed_result.count)
            
            # If still 0, try broad keyword search only
            if result.count == 0:
                broad_builder = db.table("courses").select("*", count="exact")
                try:
                    broad_builder = broad_builder.not_.is_("cricos_code", "null")
                except:
                    broad_builder = broad_builder.eq("country", "australia")
                
                # Search across all text fields
                broad_builder = broad_builder.or_(
                    f"name.ilike.%{req.query}%," 
                    f"university.ilike.%{req.query}%," 
                    f"subject.ilike.%{req.query}%," 
                    f"level.ilike.%{req.query}%"
                )
                broad_builder = broad_builder.range(offset, offset + req.page_size - 1)
                broad_result = broad_builder.execute()
                
                if broad_result.count > 0:
                    result = broad_result
                    log.info("cricos_broad_search", query=req.query, broad_count=broad_result.count)
        
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
        
        # Enrich course data with university contact information
        enriched_data = []
        if result.data:
            # Get unique provider codes from courses
            provider_codes = list(set([c.get('provider_code') for c in result.data if c.get('provider_code')]))
            
            # Fetch university details for these provider codes
            university_map = {}
            if provider_codes:
                try:
                    uni_query = db.table("universities").select("*").in_("provider_code", provider_codes)
                    uni_result = uni_query.execute()
                    if uni_result.data:
                        university_map = {u['provider_code']: u for u in uni_result.data if u.get('provider_code')}
                except Exception as e:
                    log.warning("failed_to_fetch_university_data", error=str(e))
            
            # Also try matching by university name if provider_code lookup failed
            if not university_map:
                uni_names = list(set([c.get('university') for c in result.data if c.get('university')]))
                if uni_names:
                    try:
                        uni_query = db.table("universities").select("*").in_("name", uni_names)
                        uni_result = uni_query.execute()
                        if uni_result.data:
                            university_map = {u['name']: u for u in uni_result.data if u.get('name')}
                    except Exception as e:
                        log.warning("failed_to_fetch_university_by_name", error=str(e))
            
            # Merge university data into courses
            for course in result.data:
                enriched_course = course.copy()
                provider_code = course.get('provider_code')
                uni_name = course.get('university')
                
                # Try provider_code first, then name
                uni_data = university_map.get(provider_code) or university_map.get(uni_name)
                
                if uni_data:
                    enriched_course['website'] = uni_data.get('website')
                    enriched_course['contact_phone'] = uni_data.get('phone_number')
                    enriched_course['contact_email'] = uni_data.get('email_address')
                    enriched_course['institution_type'] = uni_data.get('institution_type')
                    enriched_course['postal_address'] = uni_data.get('postal_address')
                    enriched_course['total_students'] = uni_data.get('total_students')
                enriched_data.append(enriched_course)
        
        return {
            "data": enriched_data,
            "total_count": result.count,
            "page": req.page,
            "page_size": req.page_size,
            "filters_applied": parsed_filters,
            "search_strategy": "relaxed" if result.count > 0 and req.page == 1 and req.query and keyword else "strict",
            "ai_enhanced": True if req.query else False
        }
        
    except Exception as e:
        log.error("cricos_search_failed", error=str(e))
        return {
            "error": str(e),
            "data": [],
            "total_count": 0
        }
