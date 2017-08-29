import queue
import logging

QUEUE = 'message'

def callback(ch, method, properties, body):
	print ("Received a message " + body)

def consume():

	logging.basicConfig(level=logging.DEBUG)

	connection = queue.connect ()

	channel = connection.channel()

	channel.queue_declare(queue=QUEUE)

	channel.basic_consume(callback,
    		              queue=QUEUE,
        		          no_ack=True)

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()

print("Welcome to the Ping Pong solution")

consume()

