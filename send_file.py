import socket
import sys
from os.path import getsize


OK = bytes("OK", "UTF-8")
DONE = bytes("DONE", "UTF-8")


def sendFile(mac, path: str):
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client.connect((serverMACAddr, 4))
    client.send(bytes("file " + path.split("/")[-1] + " " + str(getsize(path)), "UTF-8"))
    res = client.recv(1024)
    if res != OK:
        raise Exception("Return Code Invalid: " + str(res, "UTF-8"))
    with open(path, "rb") as f:
        client.send(f.read())

    res = client.recv(1024)
    if res != DONE:
        raise Exception("Return Code Invalid: " + str(res, "UTF-8"))
    client.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Enter path name:\n")

    with open("Target-Addr") as f:
        serverMACAddr = f.read().strip()

    sendFile(serverMACAddr, path)
