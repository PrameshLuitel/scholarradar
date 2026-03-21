import os
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastmcp import FastMCP
import uvicorn
import structlog

# Initialize logging
log = structlog.get_logger("mcp_server.server")

# 1. Create FastMCP instance
mcp = FastMCP(
    name="ScholarRadar",
    instructions="""You are ScholarRadar, a dedicated study abroad assistant. 
    You help students find scholarships, courses, and universities, and plan their entire journey 
    including visa requirements, IELTS prep, and cost of living budgeting.
    
    Always use the available tools to provide data-backed advice. 
    If a student asks for a 'plan', use the `plan_study_abroad_journey` tool first."""
)

# 2. Register all tool modules
from src.mcp_server.tools.scholarships import register_tools as register_scholarships
from src.mcp_server.tools.courses import register_tools as register_courses
from src.mcp_server.tools.universities import register_tools as register_universities
from src.mcp_server.tools.ielts import register_tools as register_ielts
from src.mcp_server.tools.visa import register_tools as register_visa
from src.mcp_server.tools.cost_of_living import register_tools as register_cost_of_living
from src.mcp_server.tools.counsellor import register_tools as register_counsellor

register_scholarships(mcp)
register_courses(mcp)
register_universities(mcp)
register_ielts(mcp)
register_visa(mcp)
register_cost_of_living(mcp)
register_counsellor(mcp)

# 3. Get MCP HTTP app (to use its lifespan)
mcp_app = mcp.http_app()

# 4. Create FastAPI app with FastMCP's lifespan
app = FastAPI(
    title="ScholarRadar MCP",
    lifespan=mcp_app.lifespan
)

# 5. CORS Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 6. Health Check
@app.get("/health")
async def health_check():
    """Health check for Render.com and monitoring."""
    return {
        "status": "ok",
        "server": "ScholarRadar MCP",
        "mcp_mounted": True,
        "tools_registered": len(mcp._tool_manager.list_tools()) if hasattr(mcp, "_tool_manager") else "unknown"
    }

# 7. Mount MCP at / (mcp_app already has /mcp route)
app.mount("/", mcp_app)

# 8. Entry Point
if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    log.info("server_start", port=port, env=os.getenv("RENDER_EXTERNAL_URL", "local"))
    uvicorn.run(app, host="0.0.0.0", port=port)
