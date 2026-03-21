"""
Supabase client with lazy initialization, retry logic, and connection pooling.

The client is only created when get_db() is first called — NOT at import time.
This prevents crashes when supabase is not installed or env vars are missing.
"""

import os
from typing import Optional

# All heavy imports are deferred to avoid import-time crashes
_client_instance = None


def get_db():
    """
    Get the Supabase client instance (lazy singleton).
    Only imports supabase and reads env vars on first call.
    """
    global _client_instance
    if _client_instance is not None:
        return _client_instance

    # Import dependencies only when actually needed
    try:
        from supabase import create_client, Client
    except ImportError:
        raise ImportError(
            "supabase package not installed. Run: pip install supabase\n"
            "The scrapers work without it (save_to_db=False), but DB writes need it."
        )

    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass  # dotenv is optional, env vars can be set directly

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError(
            "SUPABASE_URL and SUPABASE_KEY must be set in environment variables.\n"
            "Copy .env.example to .env and fill in your Supabase credentials."
        )

    try:
        from tenacity import retry, stop_after_attempt, wait_exponential

        @retry(
            stop=stop_after_attempt(5),
            wait=wait_exponential(multiplier=1, min=2, max=10),
        )
        def _create_with_retry():
            return create_client(url, key)

        _client_instance = _create_with_retry()
    except ImportError:
        # tenacity not installed — create without retry
        _client_instance = create_client(url, key)

    try:
        from src.utils.logger import logger
        logger.info("supabase_client_initialized")
    except (ImportError, Exception):
        pass

    return _client_instance
