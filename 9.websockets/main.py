import asyncio
import random
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse


class ConnectionManager:
    def __init__(self):
        self.connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.connections:
            self.connections.remove(websocket)

    async def broadcast(self, message: str):
        dead_connections = []

        for connection in self.connections:
            try:
                await connection.send_text(message)
            except Exception:
                dead_connections.append(connection)

        for connection in dead_connections:
            self.disconnect(connection)


manager = ConnectionManager()

stocks = {
    "AAPL": 190.00,
    "GOOG": 150.00,
    "MSFT": 430.00,
    "TSLA": 220.00,
    "NVDA": 1200.00,
}


async def stock_generator():
    while True:
        for symbol in stocks:
            change = random.uniform(-5, 5)

            stocks[symbol] = round(stocks[symbol] + change, 2)

            await manager.broadcast(f"{symbol}|{stocks[symbol]}")

        await asyncio.sleep(1)


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(stock_generator())

    yield

    task.cancel()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def home():
    with open("static/index.html", "r") as f:
        return HTMLResponse(f.read())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()

    except Exception:
        manager.disconnect(websocket)
