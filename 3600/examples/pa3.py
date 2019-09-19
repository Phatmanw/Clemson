#import libraries
import selectors
from socket import *

#create a select instance
sel = selectors.DefaultSelector()

#server info
serverName = 'cpsc3600.computing.clemson.edu'
serverPort = 3607

#create sockets and register them with selector
for i in range(0,3):
	connectID = i + 1
   print('starting connection', connectID, 'to', serverName)
   sock = socket(AF_INET, SOCK_STREAM)
   sock.setblocking(False)
   sock.connect_ex((serverName, serverPort))
   events = selectors.EVENT_READ     
	sel.register(sock, events, i)


#
while True:
	message = input('input something user: ')

	for i in range(0,3):
		events = sel.select(timeout=10)
		sock.send(message.encode())


	for key, mask in events:
		sock = key.fileobj
		data = key.data
		response = sock.recv(2048).decode()
		print(response + ": " + str(data))
