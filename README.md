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
