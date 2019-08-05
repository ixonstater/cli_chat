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

    def requestCode(self):
        request = {'intent': consts.NEW_USER_CODE}
        request = json.dumps(request).encode('utf-8')
        self.socket.send(request)

def main():
    testClients = []
    for i in range(0,10):
        testClients.append(TestClient())
    for i in range(0,10):
        testClients[i].connect()
    for i in range(0,10):
        testClients[i].requestCode()
if __name__ == '__main__':
    main()