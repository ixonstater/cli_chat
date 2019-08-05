
class ServerData:
    def __init__(self):
        lastAssignedCode = 0
    
    def generateCode(self):
        self.lastAssignedCode += 1
        return self.lastAssignedCode - 1

    def readData(self):
        pass

    def writeData(self):
        pass