import socket

bluetoothMACAddr = "CC:5E:F8:D7:7A:3C"

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind((bluetoothMACAddr, 4))
server.listen(1)

print("Started server")

connection, addr = server.accept()

while True:
    print(str(connection.recv(1024), "UTF-8"))

