import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="notification_exchange", exchange_type="direct")

channel.basic_publish(
    exchange="notification_exchange", routing_key="email", body="Welcome User"
)

print("Email notification sent")

connection.close()
