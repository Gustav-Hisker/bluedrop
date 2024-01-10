import re
import socket
import subprocess


def getBluetoothMAC():
    hciconfig = subprocess.run("hciconfig", stdout=subprocess.PIPE).stdout

    regex = r"(?:[0123456789ABCDEF]{2}:){5}[0123456789ABCDEF]{2}"

    return re.findall(regex, str(hciconfig))[0]


bluetoothMACAddr = getBluetoothMAC()

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind((bluetoothMACAddr, 4))
server.listen(1)

print("Started server on " + bluetoothMACAddr)

connection, addr = server.accept()

while True:
    print(str(connection.recv(1024), "UTF-8"))

