from database import SessionLocal, engine
from fastapi import FastAPI
from models import Base, Order
from pydantic import BaseModel
from worker import process_order

Base.metadata.create_all(bind=engine)

app = FastAPI()


class OrderRequest(BaseModel):
    item_name: str
    quantity: int


@app.post("/orders")
def create_order(req: OrderRequest):
    db = SessionLocal()

    try:
        order = Order(item_name=req.item_name, quantity=req.quantity, status="PENDING")

        db.add(order)
        db.commit()
        db.refresh(order)

        process_order.delay(order.id)

        return {"order_id": order.id, "status": order.status}

    finally:
        db.close()


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    db = SessionLocal()

    try:
        order = db.query(Order).filter(Order.id == order_id).first()

        if not order:
            return {"message": "Order not found"}

        return {
            "id": order.id,
            "item": order.item_name,
            "quantity": order.quantity,
            "status": order.status,
        }

    finally:
        db.close()
