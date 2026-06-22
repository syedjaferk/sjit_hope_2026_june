import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="user_events", exchange_type="fanout")

channel.basic_publish(exchange="user_events", routing_key="", body="User Registered")

print("Event Published")

connection.close()
