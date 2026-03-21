import asyncio
import time
from .logger import logger

class RateLimiter:
    def __init__(self, calls_per_second: float = 1.0):
        self.delay = 1.0 / calls_per_second
        self.last_call = 0.0
        self.lock = asyncio.Lock()

    async def wait(self):
        async with self.lock:
            elapsed = time.perf_counter() - self.last_call
            if elapsed < self.delay:
                await asyncio.sleep(self.delay - elapsed)
            self.last_call = time.perf_counter()
            await logger.ainfo("rate_limiter_wait_complete", delay=self.delay)
