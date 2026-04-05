import asyncio
from fastapi import FastAPI
from fastmcp import FastMCP

mcp = FastMCP("Test")
mcp_app = mcp.http_app()

app = FastAPI()
app.router.routes.extend(mcp_app.routes)

print([r.path for r in app.routes])
