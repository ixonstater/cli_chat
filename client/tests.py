from user_data import *
import consts
import json

def makeTestConversationList():
    amy = Conversation()
    amy.tag = 'fh2n4'
    amy.conversationName = 'amy'
    amy1 = Message()
    amy1.messageOrigin = consts.REMOTE_MESSAGE
    amy1.messageText = 'Hi girl'
    amy2 = Message()
    amy2.messageOrigin = consts.REMOTE_MESSAGE
    amy2.messageText = 'Hows it goin?'
    amy3 = Message()
    amy3.messageOrigin = consts.LOCAL_MESSAGE
    amy3.messageText = 'Not so bad'
    amy3.messageOrigin
    amy.addMessage(amy1)
    amy.addMessage(amy2)
    amy.addMessage(amy3)

    mike = Conversation()
    mike.tag = 'thnda2'
    mike.conversationName = 'mike'
    mike1 = Message()
    mike1.messageOrigin = consts.LOCAL_MESSAGE
    mike1.messageText = 'Sup dogg?'
    mike2 = Message()
    mike2.messageOrigin = consts.REMOTE_MESSAGE
    mike2.messageText = 'Nothin much, you?'
    mike3 = Message()
    mike3.messageOrigin = consts.LOCAL_MESSAGE
    mike3.messageText = 'Same'
    mike.addMessage(mike1)
    mike.addMessage(mike2)
    mike.addMessage(mike3)
    return {mike.conversationName:mike, amy.conversationName:amy}


def main():
    os.chdir('/home/ixonstater/stuff/code/python/cli_chat/client')# debugging line
    progData = ProgramData()
    # progData.conversations = makeTestConversationList()
    progData.readData()
    

main()