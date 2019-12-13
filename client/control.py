import consts
import input_validation
import user_data
import socket
import request_response

class ExitException(Exception):
    pass

class ProgramInstance:
    def __init__(self):
        self.socket = socket.socket()
        self.data = user_data.ProgramData()
        self.data.readData()
        while(self.data.ip == None):
            ip = input(consts.REQUEST_SERVER_IP)
            self.setServerIpAddress(ip)
        if(self.data.tag == None):
            self.requestTagFromServer()

    def printWelcome(self):
        print(consts.WELCOME)
        print(consts.CLEAR_CODE)
        if(not self.data.hasSeenTutorial):
            print(consts.TUTORIAL_TEXT)
            self.data.hasSeenTutorial = True

    def requestTagFromServer(self):
        request = request_response.requestTag()

    def mainLoop(self):
        while(True):
            try:
                nextCommand = input(consts.NEXT_COMMAND)
                nextCommand = input_validation.commandIsValid(nextCommand)
                self.routeCommand(nextCommand)
            except IOError:
                print(consts.INVALID_COMMAND)
                continue
            except ExitException:
                self.data.writeData()
                return
            except KeyboardInterrupt:
                self.data.writeData()
                print('\n')
                return

    def routeCommand(self, command):
        try:
            input_validation.numberOfArgs(command)
        except IndexError:
            print(consts.WRONG_NUMBER_OF_ARGS)
            return
            
        if(command[0] == 'help'):
            return self.showHelp()
        elif(command[0] == 'exit'):
            return self.exitProgram()
        elif(command[0] == 'lsconv'):
            return self.listConversations()
        elif(command[0] == 'addconv'):
            return self.addConversation(command[1], command[2])
        elif(command[0] == 'rmconv'):
            return self.deleteConversation(command[1])
        elif(command[0] == 'clear'):
            return self.clear()
        elif(command[0] == 'chat'):
            return self.startChat(command[1]) 
        elif(command[0] == 'mycode'):
            return self.printOwnCode()
        elif(command[0] == 'tutorial'):
            return self.showTutorial()
        elif(command[0] == 'getip'):
            self.getServerIpAddress()
        elif(command[0] == 'setip'):
            self.setServerIpAddress(command[1])
        elif(command[0] == 'find'):
            self.findInConversation(command[1], command[2])
        elif(command[0] == 'dispconv'):
            self.displayConversation(command[1])

    def exitProgram(self):
        raise ExitException

    def listConversations(self):
        print(consts.DISPLAY_CURRENT_CONVERSATIONS)
        for conversationName in self.data.conversations.keys():
            print(conversationName)

    def addConversation(self, userTag, conversationName):
        try:
            input_validation.validateUserTag(userTag)
        except IOError:
            print(consts.INVALID_USER_TAG)
        newConversation = user_data.Conversation()
        newConversation.conversationName = conversationName
        newConversation.tag = userTag
        self.data.conversations[conversationName] = newConversation

    def deleteConversation(self, conversationName):
        try:
            input_validation.validateConversationName(conversationName, self.data.conversations.keys())
        except IOError:
            print(consts.NON_EXISTANT_CONVERSATION_NAME)
        del self.data.conversations[conversationName]

    def displayConversation(self, conversationName):
        try:
            input_validation.validateConversationName(conversationName, self.data.conversations.keys())
        except IOError:
            print(consts.NON_EXISTANT_CONVERSATION_NAME)

    def findInConversation(self, conversationName, term):
        try:
            input_validation.validateConversationName(conversationName, self.data.conversations.keys())
        except IOError:
            print(consts.NON_EXISTANT_CONVERSATION_NAME)

    def startChat(self, targetIndentifier):
        pass

    def showHelp(self):
        print(consts.HELP_SCHPIEL)

    def clear(self):
        print(consts.CLEAR_CODE)

    def printOwnCode(self):
        print(consts.DISPLAY_USER_CODE + str(self.data.tag))

    def showTutorial(self):
        print(consts.TUTORIAL_TEXT)

    def getServerIpAddress(self):
        print(consts.DISPLAY_IP_ADDRESS + self.data.ip + ':' + str(self.data.port))

    def setServerIpAddress(self, newIp):
        try:
            port, ip = input_validation.validateIp(newIp, self.socket)
        except:
            print(consts.BAD_IP_ADDRESS)
            return
        self.data.port = port
        self.data.ip = ip