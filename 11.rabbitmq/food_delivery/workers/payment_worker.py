import json

import pika
from celery_app import celery_app

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))

channel = connection.channel()

channel.exchange_declare(exchange="food_events", exchange_type="topic")

channel.queue_declare(queue="payment_queue")

channel.queue_bind(
    exchange="food_events", queue="payment_queue", routing_key="order.created"
)


def callback(ch, method, props, body):
    order = json.loads(body)

    process_payment.delay(order)

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue="payment_queue", on_message_callback=callback)

channel.start_consuming()


@celery_app.task
def process_payment(order):
    print(f"Processing payment for {order['order_id']}")
