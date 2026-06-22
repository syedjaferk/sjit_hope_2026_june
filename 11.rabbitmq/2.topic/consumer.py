import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="ecommerce_events", exchange_type="topic")

channel.basic_publish(
    exchange="ecommerce_events", routing_key="order.created", body="Order #1001 Created"
)

print("Event Sent")

connection.close()
