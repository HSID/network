#! /usr/bin python

from socket import *

import sys

import time

serverName = sys.argv[1]

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
	
message = '%.5s' % time.time()

clientSocket.sendto(message, (serverName, serverPort))

print 'send time to %s' % serverName

clientSocket.close()
