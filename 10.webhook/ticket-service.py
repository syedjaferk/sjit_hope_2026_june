from fastapi import FastAPI, Request

app = FastAPI()

# Fake database
bookings = {"BOOK001": {"movie": "Coolie", "amount": 250, "status": "PENDING"}}


@app.get("/bookings")
def get_bookings():
    return bookings


@app.post("/webhook/payment")
async def payment_webhook(request: Request):
    payload = await request.json()

    booking_id = payload["booking_id"]
    payment_status = payload["payment_status"]

    print("Webhook received:", payload)

    if booking_id in bookings:
        if payment_status == "SUCCESS":
            bookings[booking_id]["status"] = "CONFIRMED"

        elif payment_status == "FAILED":
            bookings[booking_id]["status"] = "FAILED"

    return {"message": "Webhook Processed"}
