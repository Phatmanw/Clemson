from socket import *
from struct import pack, unpack

serverName = 'cpsc3600.computing.clemson.edu'
serverPort = 3601

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = input('How long you want yo password to be? (between 3 and 64 characters) ')
    packed_data = pack('!i', int(message))
    clientSocket.send(packed_data)
    modifiedMessage = clientSocket.recv(2048)
    unpackedData = unpack('!sd', modifiedMessage)
    print(unpackedData)