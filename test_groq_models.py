import asyncio
import os
import httpx
from dotenv import load_dotenv
load_dotenv(".env")
api_key = os.getenv("GROQ_API_KEY")

async def test():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.groq.com/openai/v1/models",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        data = response.json()
        print(", ".join([m['id'] for m in data.get('data', [])]))

asyncio.run(test())
