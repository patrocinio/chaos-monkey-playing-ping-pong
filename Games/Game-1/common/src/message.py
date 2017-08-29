import queue

MESSAGE_QUEUE = 'message'

def init (connection):
	channel = connection.channel()
	channel.queue_declare(queue=MESSAGE_QUEUE)
	return channel

def send (channel, message):
	print ("Sending message " + message + " to queue " + MESSAGE_QUEUE)
	print ("Channel: %r " % channel)
	channel.basic_publish(exchange='',
                      routing_key=MESSAGE_QUEUE,
                      body=message)


