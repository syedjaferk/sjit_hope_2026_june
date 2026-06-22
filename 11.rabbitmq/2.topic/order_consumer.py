import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="ecommerce_events", exchange_type="topic")

channel.queue_declare(queue="order_queue")

channel.queue_bind(
    exchange="ecommerce_events", queue="order_queue", routing_key="order.*"
)


def callback(ch, method, properties, body):
    print("ORDER SERVICE:", body.decode())


channel.basic_consume(queue="order_queue", on_message_callback=callback, auto_ack=True)

channel.start_consuming()
