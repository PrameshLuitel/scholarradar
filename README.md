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

## Analytics System
The server includes a comprehensive analytics system that tracks all MCP tool usage. 
You can access the analytics via the REST API endpoints:
- `GET /analytics/overview`: High-level summary
- `GET /analytics/gaps`: Identify searches with zero results
- `GET /analytics/trends`: Identify top requested destinations
- `GET /analytics/nationality/{nationality}`: Deep dive into a specific student profile

These endpoints are protected. Include the `X-Analytics-Key` header in your requests matching the `ANALYTICS_API_KEY` environment variable.
A weekly scheduled job also automatically generates and sends an analytics report to the compiled `IDP_REPORT_WEBHOOK`.
