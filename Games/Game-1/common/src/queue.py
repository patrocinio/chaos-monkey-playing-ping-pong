import pika

PASSWORD = 'ping_pong'

HOST = 'queue-rabbitmq.default.svc.cluster.local'
#HOST = 'localhost'
PORT = 5672

def connect ():
	credentials = pika.PlainCredentials('user', PASSWORD)
	parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)

	print ("Connecting to queue at " + HOST)
	connection = pika.BlockingConnection(parameters)

	return connection
