import queue

QUEUE = 'message'

def init (connection):
	channel = connection.channel()

	channel.queue_declare(queue=QUEUE)

	return channel

def send (channel, message):
	channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body=message)


