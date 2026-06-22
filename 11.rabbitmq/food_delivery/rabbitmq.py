import json

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))

channel = connection.channel()

channel.exchange_declare(exchange="food_events", exchange_type="topic", durable=True)


def publish_event(routing_key, payload):
    channel.basic_publish(
        exchange="food_events", routing_key=routing_key, body=json.dumps(payload)
    )
