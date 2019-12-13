import socket
import threading
import time
import json
import consts

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

    def makeResponse(self):
        pass

    def handleRequest(self, data):
        response = None
        if(data['intent'] == consts.NEW_USER_CODE):
            pass
        elif(data['intent'] == consts.NEW_OUTGOING_MESSAGE):
            pass
        elif(data['intent'] == consts.SERVER_EXISTS):
            response = json.dumps({'serverResponse': consts.SERVER_DOES_EXIST})
        return response.encode('utf-8')

    def threadLoop(self):
        while(True):
            while(len(self.activeConnections) != 0):
                data = json.loads(self.activeConnections[0][1].recv(16384))
                response = self.handleRequest(data)
                self.activeConnections[0][1].sendall(response)
                self.activeConnections[0][1].close()
                self.activeConnections.pop(0)
            time.sleep(0.2)

    def mainLoop(self):
        self.daemonWorker.start()
        while (True):
            connection, address = self.socket.accept()
            connection.settimeout(4)
            self.activeConnections.append([address, connection])
