#! /usr/bin python

import time

from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print "The server is ready to receive"

while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	print 'Received:', message
	print 'Own: %.5f' % time.time()


