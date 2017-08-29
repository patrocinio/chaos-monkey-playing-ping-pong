import queue
import message

QUEUE = 'ping'
BALL = 'white'

connection = queue.connect()
message.init ()

channel = connection.channel()
channel.queue_declare(queue=QUEUE)

message.send ("Throwing ball " + BALL)

channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body=BALL)

print("Ball thrown")
message.close()
connection.close()