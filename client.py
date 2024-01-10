import socket

with open("Target-Addr") as f:
    serverMACAddr = f.read().strip()

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((serverMACAddr, 7))

print("Text an den Server:")
while True:
    client.send(bytes(input(), "UTF-8"))
