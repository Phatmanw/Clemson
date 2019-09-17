from socket import *
from struct import *
from time import *

#server info
serverName = 'cpsc3600.computing.clemson.edu'
serverPort = 3601

#creat socket and connect to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

#get pw size from user, send to server and receive pw and time to break, print results
while True:
    before = time()
    message = input('How long you want your password to be? (between 3 and 64 characters): ')
    packed_data = pack('!i', int(message))
    clientSocket.send(packed_data)
    modifiedMessage = clientSocket.recv(2048)
    format = '!' + message + 'sd'
    unpackedMsg = unpack(format, modifiedMessage)
    print(unpackedMsg)
    after = time()
    elapsed = after - before
    print(elapsed)