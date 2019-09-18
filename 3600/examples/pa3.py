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
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(sock, events, i+1)

#
while True:
    message = input('input something user: ')
    sock.send(message.encode())
    events = sel.select(timeout=10)

    for key, mask in events:
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_WRITE:
            response = sock.recv(2048).decode()
            print(response + ": " + str(data))
        else:
            pass