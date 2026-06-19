from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse
import asyncio
from datetime import datetime

app = FastAPI()

async def event_generator():

    while True:

        yield {
            "event": "stock-update",
            "data": f"Price Updated {datetime.now()}"
        }

        await asyncio.sleep(2)

@app.get("/events")
async def events():

    return EventSourceResponse(
        event_generator()
    )


