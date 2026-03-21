web: uvicorn src.mcp_server.server:app --host 0.0.0.0 --port ${PORT:-8000}
worker: python -m src.scheduler.jobs
