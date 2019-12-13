import os
import json
import consts

def decodeResponse(response):
        return json.loads(response)

def requestTag():
        request = {'intent': consts.NEW_USER_CODE}
        request = json.dumps(request).encode('utf-8')
        return request

def getServerExistsVerification():
        request = {'intent': consts.SERVER_EXISTS}
        request = json.dumps(request).encode('utf-8')
        return request

def sendMessage():
        pass