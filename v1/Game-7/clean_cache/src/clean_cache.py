import pp_queue
import sys
import message
import os
import time
import redis

CACHE='cache-redis.ping-pong.svc.cluster.local'
#CACHE='localhost'

welcome_message = "==> Cleaning caches"

red = 0

def cleanCache(key):
	message.send ("Deleting key " + key)
	red.delete(key)

def initCache():
	print ("Initializing cache")
	global red
	red = redis.StrictRedis(host=CACHE, password='ping_pong')

print(welcome_message)

# Init message
message.init ()

message.send (welcome_message)

# Init cache
initCache()

# Check cache
cleanCache('ping')
cleanCache('pong')


