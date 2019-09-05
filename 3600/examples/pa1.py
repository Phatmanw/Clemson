#import socket module
from socket import *

#set server name and port
serverName = 'cspc3600.computing.clemson.edu'
serverPort = 3600

#create socket and connect to server
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('input something user ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddr = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    clientSocket.close()

