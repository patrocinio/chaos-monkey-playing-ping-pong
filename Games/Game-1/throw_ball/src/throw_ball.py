import queue
import message

QUEUE = 'ping'
BALL = 'white'
COMPONENT = 'throw_ball'

message.init ()

connection = queue.connect()
channel = connection.channel()
channel.queue_declare(queue=QUEUE)

message.send (COMPONENT, "Throwing ball " + BALL)

channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body=BALL)

print("Ball thrown")
message.close()
connection.close()