import control
import os

def main():
    os.chdir('/home/ixonstater/code/cli_chat/client')# debugging line, remove before shipping
    progInstance = control.ProgramInstance()
    progInstance.mainLoop()


if __name__ == '__main__':
    main()