import queue
import sys

QUEUE = 'message'

def callback(ch, method, properties, body):
	print ("Received a message %r" % body)
	sys.stdout.flush ()

def consume():
	connection = queue.connect ()
	channel = connection.channel()
	channel.queue_declare(queue=QUEUE)

	channel.basic_consume(callback,
    		              queue=QUEUE,
        		          no_ack=True)

	print(" [*] Waiting for messages in queue " + QUEUE + ". To exit press CTRL+C")
	sys.stdout.flush ()
	channel.start_consuming()

print("Welcome to the Ping Pong solution")
consume()

