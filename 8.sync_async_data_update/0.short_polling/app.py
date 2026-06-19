from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/updates")
async def get_updates():
    return {
        "message": "Current Stock Price",
        "price": 100,
        "time": datetime.now()
    }
