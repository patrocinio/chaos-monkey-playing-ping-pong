#!/usr/bin/env python
import pika

PASSWORD = 'ping_pong'

# HOST = 'queue-rabbitmq.default.svc.cluster.local'
HOST = 'localhost'
PORT = 5672
QUEUE = 'ping'
BALL = 'white'

credentials = pika.PlainCredentials('user', PASSWORD)
parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)

print ("Connecting to queue at " + HOST)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.queue_declare(queue=QUEUE)

channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body=BALL)
print("Ping")
connection.close()
