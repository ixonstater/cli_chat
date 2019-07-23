WELCOME = 'Welcome to CLI_Chat.'
NEXT_COMMAND = 'Please enter your next command or "help" for a list of commands: '
INVALID_COMMAND = 'Invalid command recieved, please try again.'
REQUEST_OWN_USERNAME = None
REQUEST_CONVERSATION_TARGET_NAME = None
REQUEST_CONVERSATION_TARGET_TAG = None
HELP_SCHPIEL = '\nAvailable commands: \n' + \
'  exit: Quits the program saving conversation details, if this command is not given all unsaved data will be ' + \
'lost on program termination.\n' + \
'  help: Lists all available commands.\n' + \
'  clear: Clears the contents of the terminal window.\n' + \
'  lsconv: Lists current known conversations.\n' + \
'  addconv: Adds a new conversation, requires a user tag and a name for the conversation eg. "addconv th5ec7 Jimmy"\n' + \
'  rmconv: Deletes the specified conversation, requires a user tag eg. rmconv th5ec7\n' + \
'  chat: Opens a chat dialogue to the specified target, requires a conversation name or a user tag.\n'
VALID_COMMANDS = ['exit', 'help', 'addconv', 'rmconv', 'lsconv', 'chat', 'clear', 'mycode']