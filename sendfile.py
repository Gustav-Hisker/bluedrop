import socket
import sys
from os.path import getsize


def sendFile(mac, path: str):
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client.connect((serverMACAddr, 4))
    client.send(bytes("--" + path.split("/")[-1] + "--" + str(getsize(path)), "UTF-8"))
    with open(path, "wb", encoding="utf-8") as f:
        client.send(f.read())
    client.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Enter path name:\n")

    with open("Target-Addr") as f:
        serverMACAddr = f.read().strip()

    sendFile(serverMACAddr, path)
