# ScholarRadar

Production-grade Python project for scraping and serving scholarship data via MCP.

## Features
- Scalable scrapers for IDP and Government scholarships.
- Supabase integration for reliable data storage.
- MCP Server with specialized research tools.
- Async architecture with robust logging and rate limiting.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Configure environment: `cp .env.example .env`.
4. Run scrapers: `python src/scheduler/jobs.py`.
5. Start MCP server: `python src/mcp_server/server.py`.

## Deploy on Render
For Render, use the existing `Procfile` to run both the web app and scheduler worker:
- `web`: `uvicorn src.mcp_server.server:app --host 0.0.0.0 --port ${PORT:-10000}`
- `worker`: `python -m src.scheduler.jobs`

This worker runs the live daily scraper via `scrape_all_databases()` and keeps Supabase updated every 24 hours from startup.

## Analytics System
The server includes a comprehensive analytics system that tracks all MCP tool usage. 
You can access the analytics via the REST API endpoints:
- `GET /analytics/overview`: High-level summary
- `GET /analytics/gaps`: Identify searches with zero results
- `GET /analytics/trends`: Identify top requested destinations
- `GET /analytics/nationality/{nationality}`: Deep dive into a specific student profile

These endpoints are protected. Include the `X-Analytics-Key` header in your requests matching the `ANALYTICS_API_KEY` environment variable.
A weekly scheduled job also automatically generates and sends an analytics report to the compiled `IDP_REPORT_WEBHOOK`.
