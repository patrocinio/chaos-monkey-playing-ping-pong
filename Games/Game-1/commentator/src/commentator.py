import queue
import sys

MESSAGE_QUEUE = 'message'

def callback(ch, method, properties, body):
	print ("Received a message %r" % body)
	sys.stdout.flush ()

def consume():
	connection = queue.connect ()
	channel = connection.channel()
	channel.queue_declare(queue=MESSAGE_QUEUE)

	channel.basic_consume(callback,
    		              queue=MESSAGE_QUEUE,
        		          no_ack=True)

	print(" [*] Waiting for messages in queue " + MESSAGE_QUEUE + ". To exit press CTRL+C")
	sys.stdout.flush ()
	channel.start_consuming()

print("Welcome to the Ping Pong solution")
consume()

