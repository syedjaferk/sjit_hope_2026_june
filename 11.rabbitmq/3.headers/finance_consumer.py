import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="header_exchange", exchange_type="headers")

channel.queue_declare(queue="finance_queue")

channel.queue_bind(
    exchange="header_exchange",
    queue="finance_queue",
    arguments={"x-match": "all", "department": "finance"},
)


def callback(ch, method, properties, body):
    print("FINANCE:", body.decode())


channel.basic_consume(
    queue="finance_queue", on_message_callback=callback, auto_ack=True
)

channel.start_consuming()
