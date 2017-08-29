import queue
import sys

MESSAGE_QUEUE = 'message'

def callback(ch, method, properties, body):
	print ("Message: %s" % body)
	sys.stdout.flush ()

print("Welcome to the Ping Pong solution")
queue.consume(MESSAGE_QUEUE, callback)

