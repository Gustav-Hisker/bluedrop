import socket


def sendMessage(msg, mac):
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client.connect((mac, 4))
    client.send(bytes(msg, "UTF-8"))
    client.close()


if __name__ == "__main__":
    with open("Target-Addr") as f:
        serverMACAddr = f.read().strip()

    sendMessage(input("Nachricht an " + serverMACAddr + ":\n"), serverMACAddr)