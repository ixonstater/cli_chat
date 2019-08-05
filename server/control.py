import socket
import threading
import time

class ServerInstance:
    def __init__(self, serverData):
        self.portNumber = 8082
        self.socket = None
        self.activeConnections = []
        self.serverData = serverData
        self.daemonWorker = None

        self.makeDaemon()
        self.makeSocket()

    def makeSocket(self):
        self.socket = socket.socket()
        self.socket.bind(('', self.portNumber))
        self.socket.listen(100)

    def makeDaemon(self):
        self.daemonWorker = threading.Thread(target = self.threadLoop, args = ())

    def threadLoop(self):
        while(True):
            while(len(self.activeConnections) != 0):
                data = self.activeConnections[0][1].recv(4096)
                print(data)
                self.activeConnections[0][1].close()
                self.activeConnections.pop(0)
            time.sleep(1)

    def mainLoop(self):
        self.daemonWorker.start()
        while (True):
            connection, address = self.socket.accept()
            connection.settimeout(2)
            self.activeConnections.append([address, connection])
