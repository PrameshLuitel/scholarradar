#!/usr/bin/env python3
"""Test script to verify multiple CRICOS filters work together."""

import asyncio
import json
from src.database.client import get_db

def test_database_filters():
    """Test filter combinations directly on database."""
    db = get_db()
    
    print("=" * 80)
    print("TESTING: Multiple CRICOS Filters")
    print("=" * 80)
    
    # Test 1: University + Level
    print("\n[Test 1] Bond University + Doctoral Level")
    result = db.table("courses").select("name", "university", "level", "cricos_code", count="exact") \
        .ilike("university", "%bond%") \
        .or_("level.ilike.%doctoral%,level.ilike.%doctorate%,level.ilike.%phd%") \
        .not_.is_("cricos_code", "null") \
        .execute()
    print(f"  Found: {result.count} courses")
    if result.data:
        for c in result.data[:3]:
            print(f"  - {c['name'][:60]} | {c['level']} | {c['cricos_code']}")
    
    # Test 2: University + Level + Keyword
    print("\n[Test 2] Bond University + Doctoral + Philosophy (keyword)")
    result = db.table("courses").select("name", "university", "level", "cricos_code", "subject", count="exact") \
        .ilike("university", "%bond%") \
        .or_("level.ilike.%doctoral%,level.ilike.%doctorate%,level.ilike.%phd%") \
        .or_("name.ilike.%philosophy%,subject.ilike.%philosophy%") \
        .not_.is_("cricos_code", "null") \
        .execute()
    print(f"  Found: {result.count} courses")
    if result.data:
        for c in result.data[:3]:
            subject = c.get('subject') or 'N/A'
            print(f"  - {c['name'][:60]} | {subject[:40]}")
    
    # Test 3: State + Level + Max Fee
    print("\n[Test 3] NSW + Master + Under $50k")
    result = db.table("courses").select("name", "university", "level", "state", "tuition_fee", "cricos_code", count="exact") \
        .ilike("state", "%NSW%") \
        .or_("level.ilike.%master%,level.ilike.%postgraduate%") \
        .lte("tuition_fee", 50000) \
        .not_.is_("cricos_code", "null") \
        .execute()
    print(f"  Found: {result.count} courses")
    if result.data:
        for c in result.data[:3]:
            print(f"  - {c['name'][:50]} | ${c.get('tuition_fee', 0):,.0f} | {c['state']}")
    
    # Test 4: Multiple filters - State + University + Duration
    print("\n[Test 4] VIC + Monash + 12-24 months duration")
    result = db.table("courses").select("name", "university", "state", "duration_months", "cricos_code", count="exact") \
        .ilike("state", "%VIC%") \
        .ilike("university", "%monash%") \
        .gte("duration_months", 12) \
        .lte("duration_months", 24) \
        .not_.is_("cricos_code", "null") \
        .execute()
    print(f"  Found: {result.count} courses")
    if result.data:
        for c in result.data[:3]:
            print(f"  - {c['name'][:50]} | {c.get('duration_months', 'N/A')} months")
    
    # Test 5: All filters combined
    print("\n[Test 5] ALL FILTERS - NSW + Master + Engineering + $30k-$60k + 12-36 months")
    result = db.table("courses").select("name", "university", "level", "state", "tuition_fee", "duration_months", "cricos_code", count="exact") \
        .ilike("state", "%NSW%") \
        .or_("level.ilike.%master%,level.ilike.%postgraduate%") \
        .or_("name.ilike.%engineering%,subject.ilike.%engineering%") \
        .gte("tuition_fee", 30000) \
        .lte("tuition_fee", 60000) \
        .gte("duration_months", 12) \
        .lte("duration_months", 36) \
        .not_.is_("cricos_code", "null") \
        .execute()
    print(f"  Found: {result.count} courses")
    if result.data:
        for c in result.data[:3]:
            print(f"  - {c['name'][:45]} | ${c.get('tuition_fee', 0):,.0f} | {c.get('duration_months', 'N/A')}mo")
    
    print("\n" + "=" * 80)
    print("All filter tests completed!")
    print("=" * 80)

if __name__ == "__main__":
    test_database_filters()
