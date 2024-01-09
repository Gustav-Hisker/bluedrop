import socket

bluetoothMACAddr = ""

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind((bluetoothMACAddr, 4))
server.listen(1)

connection, addr = server.accept()

while True:
    print(str(connection.recv(1024), "UTF-8"))

