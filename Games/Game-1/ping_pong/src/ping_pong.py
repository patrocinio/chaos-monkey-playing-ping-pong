import pp_queue
import sys
import message
import os
import time

queue_name = os.environ['QUEUE']
other_queue = os.environ['OTHER_QUEUE']

def throw_ball(ball):
	message.send (queue_name, "Throwing ball %s" % ball)

	channel.basic_publish(exchange='',
    	                  routing_key=other_queue,
        	              body=ball)

def callback(ch, method, properties, body):
	print ("Received a message %s" % body)
	message.send (queue_name, "I received a %s ball" % body)
	sys.stdout.flush ()
	time.sleep(1)
	throw_ball(body)

print("I'm " + queue_name)

# Init message
message.init ()

message.send (queue_name, "Hello. I am " + queue_name)

# Init other queue

connection = pp_queue.connect()
channel = connection.channel()
channel.queue_declare(queue=other_queue)


# Init queue
pp_queue.consume(queue_name, callback)

