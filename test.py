
import httpx
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

async def test():
    async with httpx.AsyncClient(verify=False,trust_env=False) as client:
        response = await client.get(
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": TMDB_API_KEY,
                "query": "inception"
            }
        )
        print(response.status_code)
        print(response.json())

asyncio.run(test())