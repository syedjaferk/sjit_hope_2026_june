from fastapi import FastAPI
import asyncio

app = FastAPI()

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

            return {
                "message": data
            }

        await asyncio.sleep(1)

    return {
        "message": None
    }
