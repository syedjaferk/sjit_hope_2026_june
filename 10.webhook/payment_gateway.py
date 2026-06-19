import requests
from fastapi import FastAPI

app = FastAPI()


@app.post("/pay/{booking_id}")
def make_payment(booking_id: str):
    payment_event = {
        "event": "PAYMENT_SUCCESS",
        "booking_id": booking_id,
        "payment_id": "PAY12345",
        "payment_status": "SUCCESS",
        "amount": 250,
    }

    response = requests.post(
        "http://localhost:8000/webhook/payment", json=payment_event
    )

    return {"payment": "completed", "webhook_status": response.status_code}
