import consts
import input_validation

class ExitException(Exception):
    pass

def routeCommand(command):
    try:
        input_validation.numberOfArgs(command)
    except IndexError:
        print(consts.WRONG_NUMBER_OF_ARGS)
        return
        
    if(command[0] == 'help'):
        return showHelp()
    elif(command[0] == 'exit'):
        return exitProgram()
    elif(command[0] == 'lsconv'):
        return listConversations()
    elif(command[0] == 'addconv'):
        return addConversation(command[1], command[2])
    elif(command[0] == 'rmconv'):
        return deleteConversation(command[1])
    elif(command[0] == 'clear'):
        return clear()
    elif(command[0] == 'chat'):
        return startChat(command[1]) 
    elif(command[0] == 'mycode'):
        return printOwnCode()

def exitProgram():
    raise ExitException

def listConversations():
    pass

def addConversation(userTag, conversationName):
    pass

def deleteConversation(conversationTag):
    pass

def startChat(targetIndentifier):
    pass

def showHelp():
    print(consts.HELP_SCHPIEL)

def clear():
    print('\033[2J')
    print('\033[H')

def printOwnCode():
    pass

def showTutorial():
    print(consts.TUTORIAL_TEXT)