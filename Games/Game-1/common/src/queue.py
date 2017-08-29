import pika
import sys

PASSWORD = 'ping_pong'

HOST = 'queue-rabbitmq.ping-pong.svc.cluster.local'
#HOST = 'localhost'
PORT = 5672

channel = 0

def connect ():
	credentials = pika.PlainCredentials('user', PASSWORD)
	parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)

	print ("Connecting to queue at " + HOST)
	connection = pika.BlockingConnection(parameters)

	return connection

def consume(queue_name, callback):
	connection = connect ()
	channel = connection.channel()
	channel.queue_declare(queue=queue_name)

	channel.basic_consume(callback,
    		              queue=queue_name,
        		          no_ack=True)

	print(" [*] Waiting for messages in queue " + queue_name + ". To exit press CTRL+C")
	sys.stdout.flush ()
	channel.start_consuming()



