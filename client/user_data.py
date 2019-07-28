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
    
    def readData(self):
        pass
    
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
        jsonObjectDict.encode('utf-8')
        return
        

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

