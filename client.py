import socket

serverMACAddr = "CC:5E:F8:D7:7A:3C"

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((serverMACAddr, 4))

print("Text an den Server:")
while True:
    client.send(bytes(input(), "UTF-8"))
