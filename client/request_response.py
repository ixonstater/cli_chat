import os
def getCodeFromServer():
    pass

def getServerExistsVerification(ip):
    if(os.system('ping -c 1 ' + ip + ' > /dev/null 2>&1') != 0):
        raise IOError('No response from server')