import asyncio
import os
import httpx
from dotenv import load_dotenv
load_dotenv(".env")
api_key = os.getenv("GROQ_API_KEY")

async def test():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": "deepseek-r1-distill-llama-70b", # Let's try deepseek on Groq!
                "messages": [{"role": "user", "content": "Hello"}],
                "max_tokens": 100,
            }
        )
        print(response.status_code, response.text)

asyncio.run(test())
