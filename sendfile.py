import socket
import sys
from os.path import getsize


def sendFile(mac, path: str):
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client.connect((serverMACAddr, 4))
    client.send(bytes("--" + path.split("/")[-1] + "--" + str(getsize(path)), "UTF-8"))
    response = client.recv(1024)
    if int.from_bytes(response, "big") != 200:
        return False
    with open(path, "rb") as f:
        client.send(f.read())
    client.close()
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Enter path name:\n")

    with open("Target-Addr") as f:
        serverMACAddr = f.read().strip()

    sendFile(serverMACAddr, path)
