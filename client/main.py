import user_data
import control
import input_validation
import consts
import request_response
import os

def initialize():
    progData = user_data.ProgramData()
    progData.readData()

    print(consts.WELCOME)
    control.routeCommand(['clear'])
    if(not progData.hasSeenTutorial):
        control.showTutorial()
        progData.hasSeenTutorial = True
    if(progData.serverIp == None):
        while(True):
            ip = input(consts.REQUEST_SERVER_IP)
            try:
                input_validation.validateIp(ip)
                break
            except IOError:
                print(consts.BAD_IP_ADDRESS)
        progData.serverIp = ip
    if(progData.tag == None):
        progData.tag = request_response.getCodeFromServer()
    return progData

def mainLoop(data):
    while(True):
        try:
            nextCommand = input(consts.NEXT_COMMAND)
            nextCommand = input_validation.commandIsValid(nextCommand)
            control.routeCommand(nextCommand)
        except IOError:
            print(consts.INVALID_COMMAND)
            continue
        except control.ExitException:
            data.writeData()
            return
        except KeyboardInterrupt:
            data.writeData()
            print('\n')
            return

def main():
    os.chdir('/home/ixonstater/stuff/code/python/cli_chat/client')# debugging line, remove before shipping
    progData = initialize()
    mainLoop(progData)


if __name__ == '__main__':
    main()