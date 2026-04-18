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
    max_fee: Optional[float] = None
    page: int = 1
    page_size: int = 50

@app.post("/search")
async def search_cricos(req: CricosSearchRequest):
    try:
        db = get_db()
        parsed_filters = {}
        
        # 1. Parse natural language AI query if present
        if req.query and req.query.strip():
            # Use Groq for fast filter extraction
            from src.utils.groq_cascade import non_streaming_groq
            
            system = """Analyze the search query for CRICOS courses and extract any potential filters into a JSON object.
Valid fields:
- "state": string. (e.g., "NSW", "VIC", "QLD", "WA", "SA", "TAS", "ACT", "NT". If a city like 'sydney' is entered, map it to "NSW")
- "level": string. (either "undergraduate", "postgraduate", "vocational", or "doctorate")
- "max_fee": number. (if user mentions budget like 'under 40k' or '40000', return 40000)
- "keyword": string. (subject or field of study, e.g., 'nursing', 'IT', 'MBA')

If a field is not mentioned, exclude it. Return ONLY valid JSON."""
            user = f"Query: {req.query}"
            
            try:
                res = await non_streaming_groq(system, user, max_tokens=150, temperature=0.1)
                content = res.get("content", "").strip()
                content = re.sub(r'^```(?:json)?\s*', '', content)
                content = re.sub(r'\s*```$', '', content)
                parsed_filters = json.loads(content)
                log.info("cricos_ai_parsed_filters", original=req.query, parsed=parsed_filters)
            except Exception as e:
                log.warning("cricos_ai_parse_failed", error=str(e), query=req.query)
        
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
            # Standardize level
            lvl = level_filter.lower()
            if any(k in lvl for k in ('undergrad', 'bachelor', 'b.a', 'b.s')):
                query_builder = query_builder.ilike("level", "%undergrad%")
            elif any(k in lvl for k in ('postgrad', 'master', 'mba')):
                query_builder = query_builder.or_("level.ilike.%postgrad%,level.ilike.%master%")
            elif 'vocational' in lvl or 'vET' in lvl or 'diploma' in lvl or 'certificate' in lvl:
                query_builder = query_builder.ilike("level", "%vocational%")
            elif 'doctorate' in lvl or 'phd' in lvl:
                query_builder = query_builder.ilike("level", "%doctorate%")
            else:
                query_builder = query_builder.ilike("level", f"%{level_filter}%")
                
        max_fee = req.max_fee or parsed_filters.get("max_fee")
        if max_fee:
            try:
                max_fee_float = float(max_fee)
                query_builder = query_builder.lte("tuition_fee", max_fee_float)
            except ValueError:
                pass
                
        keyword = parsed_filters.get("keyword")
        if keyword:
            # Search in name or subject
            query_builder = query_builder.or_(f"name.ilike.%{keyword}%,subject.ilike.%{keyword}%")
            
        # Pagination
        offset = (req.page - 1) * req.page_size
        query_builder = query_builder.range(offset, offset + req.page_size - 1)
        
        result = query_builder.execute()
        
        return {
            "data": result.data,
            "total_count": result.count,
            "page": req.page,
            "page_size": req.page_size,
            "ai_filters_applied": parsed_filters
        }
        
    except Exception as e:
        log.error("cricos_search_failed", error=str(e))
        return {
            "error": str(e),
            "data": [],
            "total_count": 0
        }
