#import libraries
import selectors
from socket import *

#create a select instance
sel = selectors.DefaultSelector()

#server info
serverName = 'cpsc3600.computing.clemson.edu'
serverPort = 3607

#create 3 sockets and connect to server
send = socket(AF_INET, SOCK_DGRAM)
send.connect((serverName, serverPort))
socket1 = socket(AF_INET, SOCK_DGRAM)
socket1.connect((serverName, serverPort))
socket2 = socket(AF_INET, SOCK_DGRAM)
socket2.connect((serverName, serverPort))
socket3 = socket(AF_INET, SOCK_DGRAM)
socket3.connect((serverName, serverPort))

#
events = selectors.EVENT_READ

#register each socket with selector
sel.register(socket1, events, 0)
sel.register(socket2, events, 1)
sel.register(socket3, events, 2)

while True:
    message = input('input something user: ')
    send.send(message.encode())
    events = sel.select(timeout=10)

    for key, mask in events:
        sock = key.fileobj
        data = key.data

        if mask & selectors.EVENT_READ:
            print("inside READ")

        if mask & selectors.EVENT_WRITE:
            print("inside WRITE")


    