import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)

channel = connection.channel()

channel.exchange_declare(exchange="notification_exchange", exchange_type="direct")

channel.queue_declare(queue="email_queue")

channel.queue_bind(
    exchange="notification_exchange", queue="email_queue", routing_key="email"
)


def callback(ch, method, properties, body):
    print(f"EMAIL: {body.decode()}")


channel.basic_consume(queue="email_queue", on_message_callback=callback, auto_ack=True)

print("Waiting for emails...")
channel.start_consuming()
