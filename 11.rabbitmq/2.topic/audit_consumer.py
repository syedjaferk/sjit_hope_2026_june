import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="ecommerce_events", exchange_type="topic")

channel.queue_declare(queue="audit_queue")

channel.queue_bind(exchange="ecommerce_events", queue="audit_queue", routing_key="#")


def callback(ch, method, properties, body):
    print("AUDIT:", body.decode())


channel.basic_consume(queue="audit_queue", on_message_callback=callback, auto_ack=True)

channel.start_consuming()
