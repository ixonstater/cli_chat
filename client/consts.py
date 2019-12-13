WELCOME = 'Welcome to CLI_Chat.'
CLEAR_CODE = '\033[2J' + '\n' + '\033[H'
NEXT_COMMAND = 'Please enter your next command or "help" for a list of commands: '
INVALID_COMMAND = 'Invalid command recieved, please try again.'
INVALID_USER_TAG = 'The entered user tag does not exist on this server.'
NON_EXISTANT_CONVERSATION_NAME = 'The entered conversation name does not exist.'
WRONG_NUMBER_OF_ARGS = 'Wrong number of command arguments recieved.'
REQUEST_SERVER_IP = 'Please enter the IP address and port number of the server you wish to connect to in the form IP:PORT: '
BAD_IP_ADDRESS = 'No response recieved at given IP address.'
DISPLAY_IP_ADDRESS = 'Current IP address: '
DISPLAY_USER_CODE = 'Your user code is: '
DISPLAY_CURRENT_CONVERSATIONS = 'Your current conversations are: '
REQUEST_CONVERSATION_TARGET_NAME = None
REQUEST_CONVERSATION_TARGET_TAG = None
VALID_COMMANDS = ['exit', 'help', 'addconv', 'rmconv', 'lsconv', 'chat', 'clear', 'mycode', 'tutorial', 'getip', 'setip', 'dispconv', 'find']
NO_ARG_COMMANDS = ['exit', 'help', 'lsconv', 'clear', 'mycode', 'getip', 'tutorial']
ONE_ARG_COMMANDS = ['rmconv', 'chat', 'setip', 'dispconv']
TWO_ARG_COMMANDS = ['addconv', 'find']
LOCAL_MESSAGE = 0
REMOTE_MESSAGE = 1
LOCAL_MESSAGE_STRING_CODE = 'l'
REMOTE_MESSAGE_STRING_CODE = 'r'
HELP_SCHPIEL = '\nAvailable commands: \n' + \
'  exit: Quits the program saving conversation details.\n' + \
'  help: Lists all available commands.\n' + \
'  clear: Clears the contents of the terminal window.\n' + \
'  lsconv: Lists current known conversations.\n' + \
'  addconv: Adds a new conversation, requires a user tag and a name for the conversation eg. "addconv th5ec7 Jimmy"\n' + \
'  rmconv: Deletes the specified conversation, requires a user tag eg. rmconv th5ec7\n' + \
'  chat: Opens a chat dialogue to the specified target, requires a conversation name or a user tag.\n' + \
'  mycode: Prints your user identification code.\n' + \
'  tutorial: Prints the new user tutorial.\n' + \
'  getip: Prints the current server IP address.\n' + \
'  setip: Sets a new server IP address, requires the IP and port number in the form IP:PORT.\n' + \
'  find: Searches in a conversation for a given search term, requires a conversation name and a term.\n' + \
'  dispconv: Displays the entire contents of a conversation, requires a conversation name.'
TUTORIAL_TEXT = 'This is a simple command line chat program.  It has essentially \n' + \
'two modes: edit mode and chat mode.  In edit mode you can add, delete, \n' + \
'and view conversations.  In chat mode you can create and send messages \n' + \
'as well as view incoming messages as they are recieved. Typing help will \n' + \
'print a list of commands as well as the parameters that each command requires. \n' + \
'-----------------------------------------------------------------------------'

"""server request codes"""
NEW_USER_CODE = 100
NEW_OUTGOING_MESSAGE = 101
SERVER_EXISTS = 102
"""end server request codes"""
"""server response codes"""
SERVER_DOES_EXIST = 202
"""end server response codes"""