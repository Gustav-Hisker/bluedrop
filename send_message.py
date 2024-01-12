import socket

OK = bytes("OK", "UTF-8")
DONE = bytes("DONE", "UTF-8")

def sendMessage(msg, mac):
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client.connect((mac, 4))
    client.send(bytes("text " + msg, "UTF-8"))
    res = client.recv(1024)
    if res != DONE:
        raise Exception("Return Code Invalid: " + str(res, "UTF-8"))
    client.close()


if __name__ == "__main__":
    with open("Target-Addr") as f:
        serverMACAddr = f.read().strip()

    sendMessage(input("Nachricht an " + serverMACAddr + ":\n"), serverMACAddr)