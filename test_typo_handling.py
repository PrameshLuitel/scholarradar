#!/usr/bin/env python3
"""Test typo handling in CRICOS search."""

import asyncio
import json
import re
from src.utils.groq_cascade import non_streaming_groq

async def test_typo_handling():
    system = """You are a search query analyzer for Australian CRICOS courses. Extract ALL possible filters from the query.

IMPORTANT: Fix typos and misspellings automatically!
- "sceince" → "science", "data sceince" → "data science"
- "engeneering" → "engineering", "nursng" → "nursing"
- ANY misspelled field of study should be corrected to the proper term

Available fields: state, level, max_fee, min_duration, max_duration, university, keyword

Rules:
1. ALWAYS fix typos/misspellings in the query before extracting
2. Handle "OR" queries: "data science or engineering" → keyword:"data science engineering"
3. Return ONLY valid JSON

Examples:
- "DATA SCEINCE OR engineering" → {"keyword": "data science engineering"} (typo fixed)
- "computr sceince masters" → {"keyword": "computer science", "level": "master"} (typos fixed)
"""
    
    test_queries = [
        'DATA SCEINCE OR engineering',
        'computr sceince masters sydney',
        'busines analytcs under 50k',
        'nursng courses melbourne',
    ]
    
    print("=" * 100)
    print("TYPO HANDLING TEST")
    print("=" * 100)
    
    for query in test_queries:
        user = f'Query: {query}'
        try:
            res = await non_streaming_groq(system, user, max_tokens=100, temperature=0.1)
            content = res.get('content', '{}').strip()
            content = re.sub(r'^```(?:json)?\s*', '', content)
            content = re.sub(r'\s*```$', '', content)
            filters = json.loads(content)
            print(f'\nQuery: "{query}"')
            print(f'  Extracted: {json.dumps(filters)}')
        except Exception as e:
            print(f'\nQuery: "{query}" - ERROR: {e}')
    
    print("\n" + "=" * 100)

asyncio.run(test_typo_handling())
