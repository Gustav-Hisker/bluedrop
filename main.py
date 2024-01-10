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

while True:
    try:
        connection, addr = server.accept()
        initialMsg = str(connection.recv(1024), "UTF-8")
        if initialMsg.startswith("--"):
            filename, filesize = initialMsg.removeprefix("--").split("--")
            with open(filename, "wb") as f:
                f.write(connection.recv(filesize))
            print("Recieved " + filename + " from " + addr[0])
        else:
            print("Messages from " + addr[0])
            while True:
                print(connection.recv(1024))
    except:
        pass
