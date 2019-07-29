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
    print(consts.CLEAR_CODE)
    if(not progData.hasSeenTutorial):
        print(consts.TUTORIAL_TEXT)
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

def main():
    os.chdir('/home/ixonstater/stuff/code/python/cli_chat/client')# debugging line, remove before shipping
    progData = initialize()
    progInstance = control.ProgramInstance(progData)
    progInstance.mainLoop()


if __name__ == '__main__':
    main()