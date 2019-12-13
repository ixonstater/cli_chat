
class ServerData:
    def __init__(self):
        self.lastAssignedCode = 0
        self.users = []
        self.outgoingMessages = {}
    
    def generateCode(self):
        self.lastAssignedCode += 1
        return self.lastAssignedCode - 1

    def addOutgoingMessage(self, sender, target, messageText):
        newMessage = {'sender': sender, 'messageText': messageText}
        if(self.outgoingMessages[target]):
            self.outgoingMessages[target].append(newMessage)
        else:
            self.outgoingMessages[target] = [newMessage]

    def removeOutgoingMessage(self, target):
        return self.outgoingMessages.pop(target)

    def readData(self):
        pass

    def writeData(self):
        pass