import json

import pika
from celery_app import celery_app

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))

channel = connection.channel()

channel.exchange_declare(exchange="food_events", exchange_type="topic")

channel.queue_declare(queue="analytics_queue")

channel.queue_bind(exchange="food_events", queue="analytics_queue", routing_key="#")


@celery_app.task
def update_analytics(event):
    print(f"Analytics Event {event}")

    def callback(ch, method, props, body):
        event = json.loads(body)

        update_analytics.delay(event)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue="analytics_queue", on_message_callback=callback)

    channel.start_consuming()
