import time

from celery import Celery
from database import SessionLocal
from models import Order

celery_app = Celery(
    "order_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)


@celery_app.task
def process_order(order_id):
    db = SessionLocal()

    try:
        order = db.query(Order).filter(Order.id == order_id).first()

        if not order:
            return

        print(f"Processing Order {order_id}")

        order.status = "PROCESSING"
        db.commit()

        time.sleep(10)

        order.status = "COMPLETED"
        db.commit()

        print(f"Order {order_id} completed")

    finally:
        db.close()
