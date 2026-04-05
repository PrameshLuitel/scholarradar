from pathlib import Path
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

# 0. Setup Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_DIST = BASE_DIR / "frontend" / "dist"
log.info("server_setup", base_dir=str(BASE_DIR), frontend_dist=str(FRONTEND_DIST))

# Load Icon from frontend/public/favicon.svg
icon_data = None
try:
    icon_path = BASE_DIR / "frontend" / "public" / "favicon.svg"
    if icon_path.exists():
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

# 7. Mount FastMCP at /mcp — Claude connects to https://skolr.xyz/mcp
app.mount("/mcp", mcp_app)

# 8. Redirect Dashboard Root (no slash) to Dashboard /
from fastapi.responses import RedirectResponse
@app.get("/dashboard", include_in_schema=False)
async def redirect_dashboard():
    return RedirectResponse(url="/dashboard/")

# 9. Serve Frontend Static Files
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi import Request

# Mount assets explicitly
assets_dir = FRONTEND_DIST / "assets"
if assets_dir.exists() and assets_dir.is_dir():
    app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")

# Catch-all route to serve the SPA index.html
@app.get("/{full_path:path}")
async def serve_frontend(request: Request, full_path: str):
    # Exclude known backend prefixes from the frontend catch-all
    backend_prefixes = ["health", "analytics", "dashboard", "mcp"]
    if any(full_path.startswith(p) for p in backend_prefixes):
        from starlette.exceptions import HTTPException
        raise HTTPException(status_code=404, detail="Backend route not found")

    # If the path looks like an asset (has an extension), never serve index.html
    # This prevents the browser from getting HTML when it expects JS/CSS (MIME Type error)
    asset_extensions = {".js", ".css", ".png", ".jpg", ".jpeg", ".svg", ".ico", ".json", ".woff2", ".mp3"}
    path_obj = Path(full_path)
    is_asset = path_obj.suffix.lower() in asset_extensions

    if not FRONTEND_DIST.exists():
        log.error("frontend_dist_missing", path=str(FRONTEND_DIST))
        return JSONResponse(status_code=500, content={"error": "Frontend build directory not found."})

    # Serve the requested file if it exists
    file_path = FRONTEND_DIST / full_path
    if full_path and file_path.exists() and file_path.is_file():
        return FileResponse(str(file_path))
    
    # If it's a missing asset, 404 instead of returning index.html
    if is_asset:
        from starlette.exceptions import HTTPException
        raise HTTPException(status_code=404, detail=f"Asset '{full_path}' not found")

    # Final fallback to index.html for SPA routing (only for extension-less paths or non-assets)
    index_path = FRONTEND_DIST / "index.html"
    if index_path.exists():
        return FileResponse(str(index_path))
    
    return JSONResponse(status_code=404, content={"error": "Frontend entry point missing."})

# 10. Entry Point
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5173))
    log.info("server_start", port=port, env=os.getenv("RENDER_EXTERNAL_URL", "local"))
    uvicorn.run(app, host="0.0.0.0", port=port)
