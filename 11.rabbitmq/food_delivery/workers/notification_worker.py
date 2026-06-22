import json

import pika
from celery_app import celery_app

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))

channel = connection.channel()

channel.exchange_declare(exchange="food_events", exchange_type="topic")

channel.queue_declare(queue="notification_queue")

channel.queue_bind(
    exchange="food_events", queue="notification_queue", routing_key="order.*"
)


def callback(ch, method, props, body):
    order = json.loads(body)

    send_notification.delay(order)

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue="notification_queue", on_message_callback=callback)

channel.start_consuming()


@celery_app.task
def send_notification(order):
    print(f"Sending SMS for {order['order_id']}")
