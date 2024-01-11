import re
import socket
import subprocess
import threading
import time


def getBluetoothMAC():
    hciconfig = subprocess.run("hciconfig", stdout=subprocess.PIPE).stdout

    regex = r"(?:[0123456789ABCDEF]{2}:){5}[0123456789ABCDEF]{2}"

    return re.findall(regex, str(hciconfig))[0]


class ConnectionHandleThread(threading.Thread):
    def __init__(self, connection, addr):
        super().__init__()
        self.connection = connection
        self.addr = addr


    def run(self):
        try:
            initialMsg = str(self.connection.recv(1024), "UTF-8")
            if initialMsg.startswith("--"):
                filename, filesize = initialMsg.removeprefix("--").split("--")
                print("Recieved " + filename + " from " + self.addr[0])
                with open(filename, "wb") as f:
                    self.connection.send((200).to_bytes(1, "big"))
                    data = self.connection.recv(1024)
                    while data:
                        f.write(data)
                        data = self.connection.recv(1024)
            else:
                print("Message from " + self.addr[0] + ":")
                print(initialMsg)
                while True:
                    msg = str(self.connection.recv(1024), "UTF-8")
                    print("Message from " + self.addr[0] + ":")
                    print(msg)
        except OSError as err:
            if err.errno == 104:
                print(self.addr[0] + " disconnected")
            else:
                print(err)
        



bluetoothMACAddr = getBluetoothMAC()

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind((bluetoothMACAddr, 4))
server.listen(10)

print("Started server on " + bluetoothMACAddr)

while True:
    try:
        connection, addr = server.accept()
        handler = ConnectionHandleThread(connection, addr)
        handler.start()
    except OSError as err:
        print(err)
        pass
