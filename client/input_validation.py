import consts
def validateCommand(command):
    command.lower()
    command = command.split(' ')
    if(command[0] in consts.VALID_COMMANDS):
        return command
    else:
        raise IOError('Bad command recieved: ' + str(command))