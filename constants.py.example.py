import os
import sys
import platform

# All Paths to use API
CONFIG_DIR = os.path.expanduser('~/.myRemote') # Path where data is stored
PY_VERSION = sys.version_info[0]
MY_IP = ' 127.0.0.1' # Returns IP
P_GET = 'get.php?M=' # Returns key if positive
P_DATA = 'data.php?data=' # Inserts information
P_BASE = 'https://example.com/API/' # Base URL, every url that needs this gets included (baseurl + var)
P_MESSAGE = 'msg.php?M=' # Check if there is a message availible (Url var)
P_COMMAND = 'cmd.php?M=' # Gets the command from DB(Urls var)
P_REGISTER = 'reg.php?K=' # Registers inserted key(Urls var)
P_UPLOAD = 'upload.php'

# Global most used vars
G_OSNAME = platform.system() # Operating system's name
G_PCNAME = platform.uname()[1] # Computername