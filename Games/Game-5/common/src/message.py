import pp_queue

MESSAGE_QUEUE = 'message'

messageConnection = 0
messageChannel = 0

def init ():
	global messageConnection
	global messageChannel

	messageConnection = pp_queue.connect()
	messageChannel = messageConnection.channel()
	messageChannel.queue_declare(queue=MESSAGE_QUEUE)

def send (component, message):
	print ("Sending message " + message + " from component " + component + " to queue " + MESSAGE_QUEUE)

	m = component + ": " + message

	messageChannel.basic_publish(exchange='',
                      routing_key=MESSAGE_QUEUE,
                      body=m)


def close ():
	messageConnection.close()

