import json
import os

class ProgramData:
    def __init__(self):
        self.tag = None
        self.knownTargetUsers = None
        self.conversations = None
        self.hasSeenTutorial = None
    
    def readKnownTargetUsers(self):
        pass

    def readConversations(self):
        pass

    def readOwnData(self):
        pass
    
    def writeData(self):
        pass