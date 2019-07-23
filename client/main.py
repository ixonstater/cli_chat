import user_data
import control
import input_validation
import consts

def mainLoop(data):
    print(consts.WELCOME)
    control.routeCommand(['clear'])
    while(True):
        nextCommand = input(consts.NEXT_COMMAND)
        try:
            nextCommand = input_validation.validateCommand(nextCommand)
        except IOError:
            print(consts.INVALID_COMMAND)
            continue
        retval = control.routeCommand(nextCommand)
        if(retval == 'exit'):
            break
    data.writeData()
    return

def showTutorial():
    pass

def main():
    progData = user_data.ProgramData()
    progData.readOwnData()
    progData.readKnownTargetUsers()
    progData.readConversations()
    if(not progData.hasSeenTutorial):
        showTutorial()
    mainLoop(progData)


if __name__ == '__main__':
    main()