from control import ServerInstance
from server_data import ServerData

def main():
    serverData = ServerData()
    serverData.readData()
    server = ServerInstance(serverData)
    server.mainLoop()
    # try:
    #     server.mainLoop()
    # except :
    #     serverData.writeData()

if __name__ == '__main__':
    main()