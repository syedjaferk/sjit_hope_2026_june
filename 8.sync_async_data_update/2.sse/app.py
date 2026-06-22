import asyncio
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse

origins = ["http://localhost:8081"]
app = FastAPI()

# Add the CORS middleware to your FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,  # Allows cookies and authentication headers
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all request headers
)


async def event_generator():
    while True:
        yield {"event": "stock-update", "data": f"Price Updated {datetime.now()}"}

        await asyncio.sleep(2)


@app.get("/events")
async def events():
    return EventSourceResponse(event_generator())
