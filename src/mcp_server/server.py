import os
import asyncio
import base64
from mcp.types import Icon
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastmcp import FastMCP
import uvicorn
from datetime import datetime
import structlog

# Initialize logging
log = structlog.get_logger("mcp_server.server")

# Load Icon
icon_data = None
try:
    # server.py is in src/mcp_server/, so root is ../../
    icon_path = os.path.join(os.path.dirname(__file__), "../../frontend/public/favicon.svg")
    with open(icon_path, "rb") as f:
        bint = f.read()
        b64 = base64.b64encode(bint).decode("utf-8")
        icon_data = f"data:image/svg+xml;base64,{b64}"
except Exception as e:
    log.warning("failed_to_load_icon", error=str(e))

# 1. Create FastMCP instance
mcp = FastMCP(
    name="ScholarRadar",
    instructions="""You are ScholarRadar, a dedicated study abroad assistant. 
    You help students find scholarships, courses, and universities, and plan their entire journey 
    including visa requirements, IELTS prep, and cost of living budgeting.
    
    Always use the available tools to provide data-backed advice. 
    When providing links, always show direct university, program, or government website links instead of IDP or other middleman links.
    If a student asks for a 'plan', use the `plan_study_abroad_journey` tool first.""",
    icons=[Icon(src=icon_data, mimeType="image/svg+xml")] if icon_data else None
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

import contextlib

@contextlib.asynccontextmanager
async def combined_lifespan(app: FastAPI):
    # Start the weekly report background scheduler
    from src.jobs.weekly_report import start_scheduler
    start_scheduler()
    
    # Enter FastMCP's lifespan
    async with mcp_app.lifespan(app) as state:
        yield state

# 4. Create FastAPI app with FastMCP's lifespan
app = FastAPI(
    title="ScholarRadar MCP",
    lifespan=combined_lifespan
)

# 4.5 Include Analytics and Dashboard Endpoints directly to app
from src.api.analytics import app as analytics_app
from src.api.dashboard import app as dashboard_app

app.mount("/analytics", analytics_app)
app.mount("/dashboard", dashboard_app)

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
    tools = await mcp.list_tools()
    return {
        "status": "healthy",
        "service": "ScholarRadar MCP",
        "timestamp": datetime.now().isoformat(),
        "database": "connected",
        "tools_registered": len(tools)
    }

# 7. Add FastMCP routes to the main app directly
app.router.routes.extend(mcp_app.routes)

# 8. Serve Frontend Static Files
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi import Request
import os

frontend_dist = os.path.join(os.path.dirname(__file__), "../../frontend/dist")

try:
    app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dist, "assets")), name="assets")
except Exception as e:
    log.warning("frontend_assets_missing", error=str(e))
    
# Catch-all route to serve the SPA index.html for unknown paths (e.g. React Router)
@app.api_route("/{full_path:path}", methods=["GET"])
async def serve_frontend(request: Request, full_path: str):
    # Allow API routes to 404 naturally if they don't exist
    if full_path.startswith("mcp/") or full_path.startswith("health") or full_path.startswith("analytics/") or full_path.startswith("dashboard/"):
        from starlette.exceptions import HTTPException
        raise HTTPException(status_code=404, detail="Not Found")
        
    if not os.path.exists(frontend_dist):
         return JSONResponse(status_code=500, content={"error": "Frontend build directory not found. Ensure 'npm run build' was executed."})

    file_path = os.path.join(frontend_dist, full_path)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    
    return FileResponse(os.path.join(frontend_dist, "index.html"))

# 8. Entry Point
if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    log.info("server_start", port=port, env=os.getenv("RENDER_EXTERNAL_URL", "local"))
    uvicorn.run(app, host="0.0.0.0", port=port)
