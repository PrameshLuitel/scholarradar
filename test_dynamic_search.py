#!/usr/bin/env python3
"""Test dynamic CRICOS search - regex filter extraction."""

import re
import json

def extract_filters_regex(query):
    """Test regex-based filter extraction (0 tokens)."""
    query_lower = query.lower().strip()
    parsed_filters = {}
    
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
        if re.search(r'\b' + st.lower() + r'\b', query_lower):
            parsed_filters['state'] = st
            break
    
    # Level extraction
    if any(x in query_lower for x in ['bachelor', 'undergrad', 'b.a', 'b.s']):
        parsed_filters['level'] = 'bachelor'
    elif any(x in query_lower for x in ['postgrad', 'mba', 'msba']):
        parsed_filters['level'] = 'master'
    elif 'master' in query_lower or ' ms ' in query_lower or query_lower.endswith(' ms') or 'ma ' in query_lower or ' msc' in query_lower or query_lower.endswith(' msc'):
        parsed_filters['level'] = 'master'
    elif any(x in query_lower for x in ['phd', 'doctorate', 'doctor of', 'ph.d']):
        parsed_filters['level'] = 'doctorate'
    elif 'diploma' in query_lower:
        parsed_filters['level'] = 'diploma'
    elif any(x in query_lower for x in ['certificate', 'cert ']):
        parsed_filters['level'] = 'certificate'
    
    # Fee extraction
    fee_patterns = [
        r'(?:under|below|less than|upto|up to|max|maximum)\s*\$?\s*(\d+(?:\.\d+)?)(k|k\b|000)?',
        r'\$?(\d+(?:\.\d+)?)(k|k\b|000)\s*(?:aud|dollars)?(?:\s|$)'
    ]
    for pattern in fee_patterns:
        fee_match = re.search(pattern, query_lower)
        if fee_match:
            amount = float(fee_match.group(1))
            suffix = fee_match.group(2) or ''
            if 'k' in suffix.lower():
                amount *= 1000
            parsed_filters['max_fee'] = amount
            break
    
    # Duration extraction
    duration_patterns = [
        (r'(?:min|minimum|at least|from)\s*(\d+)\s*(?:months?|mo\b)', 'min_duration', 1),
        (r'(?:max|maximum|up to|upto|under|less than)\s*(\d+)\s*(?:months?|mo\b)', 'max_duration', 1),
        (r'(\d+)\s*[-–to]+\s*(\d+)\s*(?:months?|mo\b)', 'duration_range', None),
        (r'(?:min|minimum|at least)\s*(\d+)\s*(?:years?|yr\b)', 'min_duration', 12),
        (r'(?:max|maximum|up to|upto)\s*(\d+)\s*(?:years?|yr\b)', 'max_duration', 12),
    ]
    for pattern, field, multiplier in duration_patterns:
        dur_match = re.search(pattern, query_lower)
        if dur_match:
            if field == 'duration_range':
                parsed_filters['min_duration'] = int(dur_match.group(1)) * (multiplier or 1)
                parsed_filters['max_duration'] = int(dur_match.group(2)) * (multiplier or 1)
            else:
                parsed_filters[field] = int(dur_match.group(1)) * multiplier
            break
    
    # University extraction
    uni_patterns = [
        (r'\b(university\s+of\s+\w+)', 'full'),
        (r'\b(monash|unsw|uts|rmit|deakin|qut|uq|usyd|unimelb|anu|murdoch|ecu|flinders|cdu|utas|bond|macquarie|griffith|latrobe|uwa|unisa|victoria|swinburne|jcu|csu|scu|usc|uon|uow|acu|nd|cqu)', 'short')
    ]
    for pattern, uni_type in uni_patterns:
        uni_match = re.search(pattern, query_lower)
        if uni_match:
            parsed_filters['university'] = uni_match.group(1).title()
            break
    
    # Keyword extraction - remove known filter terms
    filter_terms = [
        'in', 'at', 'for', 'of', 'under', 'below', 'above', 'less', 'than', 'up', 'to',
        'sydney', 'melbourne', 'brisbane', 'perth', 'adelaide', 'hobart', 'canberra', 'darwin',
        'nsw', 'vic', 'qld', 'wa', 'sa', 'tas', 'act', 'nt',
        'bachelor', 'master', 'phd', 'doctorate', 'diploma', 'certificate',
        'mba', 'msba', 'ms', 'ma', 'msc', 'undergrad', 'postgrad',
        'months', 'month', 'years', 'year', 'yrs', 'yr',
        'university', 'uni', 'college', 'institute',
        'monash', 'unsw', 'uts', 'rmit', 'deakin', 'qut', 'uq', 'usyd', 'unimelb', 'anu',
        'bond', 'macquarie', 'griffith', 'latrobe', 'uwa', 'unisa', 'victoria', 'swinburne'
    ]
    words = re.findall(r'\b[a-z]{2,}\b', query_lower)
    keywords = [w for w in words if w not in filter_terms and w not in city_state_map]
    if keywords:
        parsed_filters['keyword'] = ' '.join(keywords[:3])
    
    return parsed_filters

# Test cases
test_queries = [
    "msba in sydney under 50k",
    "phd computer science monash",
    "masters engineering melbourne 20-30k",
    "bachelor nursing brisbane",
    "diploma hospitality perth less than 15000",
    "mba university of sydney",
    "data science masters 24 months",
    "artificial intelligence phd anu",
    "business analytics sydney under 40000",
    "doctor of philosophy bond university",
    "master of information technology melbourne 1-2 years",
    "bba in adelaide",
    "msc data science under 45k",
    "certificate childcare hobart",
]

print("=" * 100)
print("DYNAMIC CRICOS SEARCH - REGEX FILTER EXTRACTION (0 TOKENS)")
print("=" * 100)

for i, query in enumerate(test_queries, 1):
    filters = extract_filters_regex(query)
    print(f"\n[{i:2d}] Query: \"{query}\"")
    print(f"     Filters: {json.dumps(filters, indent=14)}")
    print(f"     Filter count: {len(filters)}")

print("\n" + "=" * 100)
print("ABBREVIATION EXPANSION TEST")
print("=" * 100)

keyword_expansions = {
    'msba': 'business analytics',
    'mba': 'business administration',
    'msc': 'science',
    'it': 'information technology',
    'cs': 'computer science',
    'ai': 'artificial intelligence',
    'ds': 'data science',
}

test_keywords = ['msba', 'mba', 'it', 'cs', 'ai ml', 'ds']
for kw in test_keywords:
    expanded = [kw]
    for abbrev, full in keyword_expansions.items():
        if abbrev in kw.lower():
            expanded.append(full)
            break
    print(f"  '{kw}' → {expanded}")

print("\n" + "=" * 100)
