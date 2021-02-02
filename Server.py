#importar libreria Socket
import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "Hello UDP Client"
byteToSend = str.encode(msgFromServer)

#Crea un socket de datagrama
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Vincular a direccion IP
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

#Escuchando para los datagramas entrantes
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from clien:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    #Enviando respuesta al cliente
    UDPServerSocket.sendto(byteToSend, address)