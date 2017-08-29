import queue

MESSAGE_QUEUE = 'message'

messageConnection = 0
messageChannel = 0

def init ():
	global messageConnection
	global messageChannel

	messageConnection = queue.connect()
	messageChannel = messageConnection.channel()
	messageChannel.queue_declare(queue=MESSAGE_QUEUE)

def send (message):
	print ("Sending message " + message + " to queue " + MESSAGE_QUEUE)
	messageChannel.basic_publish(exchange='',
                      routing_key=MESSAGE_QUEUE,
                      body=message)


def close ():
	messageConnection.close()

