import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:8081"]

# Add the CORS middleware to your FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,  # Allows cookies and authentication headers
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all request headers
)

latest_message = None


@app.post("/publish")
async def publish(msg: str):
    global latest_message
    latest_message = msg
    return {"status": "published"}


@app.get("/long-poll")
async def long_poll():
    global latest_message

    timeout = 30

    for _ in range(timeout):
        if latest_message:
            data = latest_message
            latest_message = None

            return {"message": data}

        await asyncio.sleep(1)

    return {"message": None}
