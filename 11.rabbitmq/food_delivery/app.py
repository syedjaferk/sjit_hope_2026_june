from db import SessionLocal, engine
from fastapi import FastAPI
from models import Base, Order
from rabbitmq import publish_event

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/orders")
def create_order():
    db = SessionLocal()
    order = Order(customer="Syed", item="Chicken Biryani", amount=250, status="CREATED")
    db.add(order)
    db.commit()
    db.refresh(order)
    publish_event("order.created", {"order_id": order.id, "amount": order.amount})
    return {"order_id": order.id}
