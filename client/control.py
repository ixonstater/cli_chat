import consts

def routeCommand(command):
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
    return('exit')

def listConversations():
    pass

def addConversation():
    pass

def deleteConversation():
    pass

def enterConversationMode():
    pass

def showHelp():
    print(consts.HELP_SCHPIEL)

def clear():
    print('\033[2J')
    print('\033[H')

def startChat():
    pass

def printOwnCode():
    pass