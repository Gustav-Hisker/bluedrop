import re
import socket
import subprocess
import threading

OK = bytes("OK", "UTF-8")
DONE = bytes("DONE", "UTF-8")

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
            args = str(self.connection.recv(1024), "UTF-8").split()
            msgType = args[0]
            if msgType == "file":
                filename = args[1]
                filesize = int(args[2])

                with open(filename, "wb") as f:
                    self.connection.send(OK)

                    for _ in range(filesize//1024+1):
                        data = self.connection.recv(1024)
                        f.write(data)

                connection.send(DONE)
                print("Recieved " + filename + " from " + self.addr[0])

            elif msgType == "text":
                print("Message" + ("s" if len(args) > 2 else "") + " from " + self.addr[0] + ":")
                for msg in args[1:]:
                    print(msg)
                connection.send(DONE)


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
