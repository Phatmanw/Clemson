#import libraries
import selectors
from socket import *

#create a select instance
sel = selectors.DefaultSelector()

#server info
serverName = 'cpsc3600.computing.clemson.edu'
serverPort = 3607

#create 3 sockets and connect to server
socket1 = socket(AF_INET, SOCK_STREAM)
socket1.connect((serverName, serverPort))
socket2 = socket(AF_INET, SOCK_STREAM)
socket2.connect((serverName, serverPort))
socket3 = socket(AF_INET, SOCK_STREAM)
socket3.connect((serverName, serverPort))

#
events = selectors.EVENT_WRITE | selectors.EVENT_READ

#register each socket with selector
sel.register(socket1, events, 1)
sel.register(socket2, events, 2)
sel.register(socket3, events, 3)

while True:
    message = input('input something user: ')
    socket1.send(message.encode())
    events = sel.select(timeout=5)

    for key, mask in events:
        sock = key.fileobj
        data = key.data

        #if mask & selectors.EVENT_READ:
        echo = sock.recv(2048).decode()
        print(echo + ": " + str(data))
            
        #if mask & selectors.EVENT_WRITE:
        #    print("foo")
                    