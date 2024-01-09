import socket

serverMACAddr = ""

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((serverMACAddr, 4))


while True:
    client.send(bytes(input(),"UTF-8"))