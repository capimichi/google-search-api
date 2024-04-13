import os
import asyncio
from fastapi import FastAPI
import uvicorn
from googlesearch import search
from googlesearchapi.model.SearchResultResponse import SearchResultResponse

hostname = os.getenv("HOSTNAME", "0.0.0.0")
port = int(os.getenv("PORT", 8736))

app = FastAPI()

@app.get("/search-results")
async def search_results(query: str, per_page: int = 10, start: int = 0, stop: int = 10):

    results = search(query, num=per_page, start=start, stop=stop)

    response = SearchResultResponse(query=query, results=results)
    return response

async def main():
    config = uvicorn.Config("server:main", host=hostname, port=port)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())