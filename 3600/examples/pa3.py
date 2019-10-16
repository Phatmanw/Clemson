#import libraries
import selectors
from socket import *

#create a select instance
sel = selectors.DefaultSelector()

#server info
serverName = 'cpsc3600.computing.clemson.edu'
serverPort = 3607

#create sockets and register them with selector
sock1 = socket(AF_INET, SOCK_STREAM)
sock1.connect_ex((serverName, serverPort))
sock1.setblocking(False)
sock2 = socket(AF_INET, SOCK_STREAM)
sock2.connect_ex((serverName, serverPort))
sock2.setblocking(False)
sock3 = socket(AF_INET, SOCK_STREAM)
sock3.connect_ex((serverName, serverPort))
sock3.setblocking(False)

events = selectors.EVENT_READ     

sel.register(sock1, events, 0)
sel.register(sock2, events, 1)
sel.register(sock3, events, 2)

#
while True:
	message = input('input something user: ')	
	sock1.send(message.encode())
	sock2.send(message.encode())
	sock3.send(message.encode())

	events = sel.select(timeout=10)

	for key, mask in events:
		sock = key.fileobj
		data = key.data
		response = sock.recv(2048).decode()
		print(response + ": " + str(data))