import socket
import json
import consts

class TestClient:
    def __init__(self):
        self.socket = None
        self.host = '127.0.0.1'
        self.port = 8082

        self.makeSocket()

    def makeSocket(self):
        self.socket = socket.socket()

    def connect(self):
        self.socket.connect((self.host, self.port))

    def requestExists(self):
        request = {'intent': consts.SERVER_EXISTS}
        request = json.dumps(request).encode('utf-8')
        self.socket.send(request)
        print(self.socket.recv(4096))

def main():
    testClients = []
    numClients = 1000
    for i in range(0,numClients):
        testClients.append(TestClient())
    for i in range(0,numClients):
        testClients[i].connect()
        testClients[i].requestExists()
if __name__ == '__main__':
    main()