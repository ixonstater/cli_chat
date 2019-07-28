import consts
import os

def commandIsValid(command):
    command.lower()
    command = command.split(' ')
    if(command[0] in consts.VALID_COMMANDS):
        return command
    else:
        raise IOError('Bad command recieved: ' + str(command))

def numberOfArgs(command):
    if(command[0] in consts.NO_ARG_COMMANDS and len(command) != 1):
        raise IndexError('Command should have no args.')
    elif(command[0] in consts.ONE_ARG_COMMANDS and len(command) != 2):
        raise IndexError('Command should have only one arg.')
    elif(command[0] in consts.TWO_ARG_COMMANDS and len(command) != 3):
        raise IndexError('Command should have two args.')

def validateIp(ip):
    if(os.system('ping -c 1 ' + ip + ' > /dev/null 2>&1') != 0):
        raise IOError('No response from server')
    return
