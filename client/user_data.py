import json
import os
import consts

class ProgramData:
    def __init__(self):
        self.tag = None
        self.knownTargetUsers = []
        self.conversations = {}
        self.hasSeenTutorial = False
        self.serverIp = None

    def initialWrite(self):
        self.writeData()
        self.ifile.close()
        self.ifile = open('./prog_files/data', 'r+')
        self.fileString = self.ifile.read()
    
    def readData(self):
        self.ifile = open('./prog_files/data', 'r+')
        self.fileString = self.ifile.read()
        if(self.fileString == ''):
            self.initialWrite()
        objectDict = json.loads(self.fileString)
        self.tag = objectDict['tag']
        self.knownTargetUsers = objectDict['knownTargetUsers']
        self.hasSeenTutorial = objectDict['hasSeenTutorial']
        self.serverIp = objectDict['serverIp']
        for name, conversation in objectDict['conversations'].items():
            conversationObject = Conversation()
            conversationObject.conversationName = name
            for message in conversation:
                messageObject = Message()
                if(message[0] == 'r'):
                    messageObject.messageOrigin = consts.REMOTE_MESSAGE
                elif(message[0] == 'l'):
                    messageObject.messageOrigin = consts.LOCAL_MESSAGE
                messageObject.messageText = message[1:]
                conversationObject.addMessage(messageObject)
            self.conversations[name] = conversationObject
    
    def writeData(self):
        objectDict = {
            'tag': self.tag,
            'knownTargetUsers' : self.knownTargetUsers,
            'hasSeenTutorial' : self.hasSeenTutorial,
            'serverIp' : self.serverIp,
            'conversations': {}
        }
        conversationsDict = {}
        for name, conversation in self.conversations.items():
            nameString = name
            messagesList = []
            for message in conversation.messages:
                if(message.messageOrigin == consts.REMOTE_MESSAGE):
                    messagesList.append(consts.REMOTE_MESSAGE_STRING_CODE + message.messageText)
                elif(message.messageOrigin == consts.LOCAL_MESSAGE):
                    messagesList.append(consts.LOCAL_MESSAGE_STRING_CODE + message.messageText)
            conversationsDict[name] = messagesList
        objectDict['conversations'] = conversationsDict
        jsonObjectDict = json.dumps(objectDict)
        ofile = open('./prog_files/data', 'w+')
        print(jsonObjectDict, file = ofile)
        
class Conversation:
    def __init__(self):
        self.conversationName = None
        self.messages = []
    
    def addMessage(self, message):
        self.messages.append(message)
        pass


class Message:
    def __init__(self):
        self.messageText = None
        self.messageOrigin = None

