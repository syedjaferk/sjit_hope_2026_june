import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="header_exchange", exchange_type="headers")

channel.basic_publish(
    exchange="header_exchange",
    routing_key="",
    body="Salary Processed",
    properties=pika.BasicProperties(headers={"department": "finance"}),
)

print("Message Published")

connection.close()
