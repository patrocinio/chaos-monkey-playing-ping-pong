import queue
import message

QUEUE = 'ping'
BALL = 'white'

connection = queue.connect()

messageChannel = message.init (connection)

channel = connection.channel()

channel.queue_declare(queue=QUEUE)

message.send (messageChannel, "Throwing ball " + BALL)

channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body=BALL)
print("Ping")
connection.close()
