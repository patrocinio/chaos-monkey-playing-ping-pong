import queue
import sys
import message
import os

queue = os.environment['QUEUE']

def callback(ch, method, properties, body):
	print ("Received a message %s" % body)
	message.send ("I received a %s ball" % body)
	sys.stdout.flush ()

print("I'm Ping")
message.init ()

message.send ("Hello. I am " + queue)

queue.consume(queue, callback)

