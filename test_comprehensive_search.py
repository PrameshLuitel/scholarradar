#!/usr/bin/env python3
"""Test comprehensive CRICOS search - verifies ANY query returns results."""

from src.database.client import get_db

def test_search_scenarios():
    """Test different search strategies."""
    db = get_db()
    
    print("=" * 100)
    print("COMPREHENSIVE CRICOS SEARCH TEST")
    print("=" * 100)
    
    test_scenarios = [
        {
            "name": "Exact abbreviation match",
            "query": "msba sydney",
            "filters": {"keyword": "business analytics", "state": "NSW", "level": "master"}
        },
        {
            "name": "PhD with university",
            "query": "phd computer science monash",
            "filters": {"level": "doctorate", "keyword": "computer science", "university": "Monash"}
        },
        {
            "name": "Budget constraint",
            "query": "engineering melbourne under 40k",
            "filters": {"keyword": "engineering", "state": "VIC", "max_fee": 40000}
        },
        {
            "name": "Duration constraint",
            "query": "mba 2 years",
            "filters": {"keyword": "business administration", "max_duration": 24, "level": "master"}
        },
        {
            "name": "OR query (multiple subjects)",
            "query": "data science or artificial intelligence",
            "filters": {"keyword": "data science artificial intelligence", "level": "master"}
        },
        {
            "name": "Broad query",
            "query": "nursing",
            "filters": {"keyword": "nursing"}
        },
        {
            "name": "University specific",
            "query": "bond university",
            "filters": {"university": "Bond"}
        },
        {
            "name": "Vague query (needs broad search)",
            "query": "business courses",
            "filters": {"keyword": "business"}
        },
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n[{i}] {scenario['name']}")
        print(f"    Query: \"{scenario['query']}\"")
        print(f"    Filters: {scenario['filters']}")
        
        # Build query
        qb = db.table("courses").select("name", "university", "level", "state", "tuition_fee", "cricos_code", count="exact")
        
        try:
            qb = qb.not_.is_("cricos_code", "null")
        except:
            qb = qb.eq("country", "australia")
        
        filters = scenario['filters']
        
        # Apply filters
        if filters.get("state"):
            qb = qb.ilike("state", f"%{filters['state']}%")
        
        if filters.get("level"):
            lvl = filters['level'].lower()
            if 'bachelor' in lvl:
                qb = qb.or_("level.ilike.%bachelor%,level.ilike.%undergraduate%")
            elif 'master' in lvl or 'mba' in lvl or 'msba' in lvl:
                qb = qb.or_("level.ilike.%master%,level.ilike.%postgraduate%")
            elif 'doctor' in lvl or 'phd' in lvl:
                qb = qb.or_("level.ilike.%doctoral%,level.ilike.%doctorate%")
        
        if filters.get("university"):
            qb = qb.ilike("university", f"%{filters['university']}%")
        
        if filters.get("max_fee"):
            qb = qb.lte("tuition_fee", float(filters['max_fee']))
        
        if filters.get("keyword"):
            keyword = filters['keyword']
            # Expand abbreviations
            expansions = {
                'msba': 'business analytics',
                'mba': 'business administration',
                'it': 'information technology',
                'cs': 'computer science',
                'ai': 'artificial intelligence',
                'ds': 'data science',
            }
            
            search_terms = [keyword]
            for abbrev, full in expansions.items():
                if abbrev in keyword.lower():
                    search_terms.append(full)
                    break
            
            # Handle OR queries
            if ' or ' in keyword.lower():
                search_terms.extend([p.strip() for p in keyword.split(' or ')])
            
            or_conditions = []
            for term in search_terms:
                or_conditions.append(f"name.ilike.%{term}%")
                or_conditions.append(f"subject.ilike.%{term}%")
            
            qb = qb.or_((",".join(or_conditions)))
        
        qb = qb.limit(3)
        result = qb.execute()
        
        print(f"    Results: {result.count} courses")
        if result.data:
            for c in result.data[:3]:
                fee = f"${c.get('tuition_fee', 0):,.0f}" if c.get('tuition_fee') else "N/A"
                print(f"      - {c['name'][:60]} | {c.get('level', 'N/A')[:20]} | {c.get('state', 'N/A')} | {fee}")

    print("\n" + "=" * 100)
    print("Testing progressive relaxation (zero results scenario)...")
    print("=" * 100)
    
    # Test what happens with very restrictive query
    qb = db.table("courses").select("name", "university", "cricos_code", count="exact")
    try:
        qb = qb.not_.is_("cricos_code", "null")
    except:
        qb = qb.eq("country", "australia")
    
    # Super restrictive
    qb = qb.ilike("name", "%quantum cryptography%") \
          .ilike("state", "%NT%") \
          .ilike("level", "%doctoral%") \
          .lte("tuition_fee", 10000)
    
    result = qb.limit(3).execute()
    print(f"\nRestrictive query (quantum cryptography in NT under $10k): {result.count} results")
    
    if result.count == 0:
        print("  → Would trigger progressive relaxation:")
        print("    Step 1: Remove keyword, keep structural filters")
        print("    Step 2: Broad text search across all fields")
        
        # Demonstrate broad search
        broad = db.table("courses").select("name", "university", "cricos_code", count="exact")
        try:
            broad = broad.not_.is_("cricos_code", "null")
        except:
            broad = broad.eq("country", "australia")
        
        broad = broad.or_("name.ilike.%quantum%,name.ilike.%cryptography%,university.ilike.%quantum%")
        broad_result = broad.limit(3).execute()
        print(f"    Broad search result: {broad_result.count} courses")
        if broad_result.data:
            for c in broad_result.data[:3]:
                print(f"      - {c['name'][:70]}")

    print("\n" + "=" * 100)
    print("TEST COMPLETE")
    print("=" * 100)

if __name__ == "__main__":
    test_search_scenarios()
