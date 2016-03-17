import os
import sys
import platform

# All Paths to use API
P_GET = 'get.php?M='  # Returns key if positive
P_DATA = 'data.php?data='  # Inserts information
P_BASE = 'https://myremote.io/stub/'  # Base URL, every url that needs this gets included (baseurl + var)
P_MESSAGE = 'msg.php?M='  # Check if there is a message available (Url var)
P_COMMAND = 'cmd.php?M='  # Gets the command from DB(Urls var)
P_REGISTER = 'reg.php?K='  # Registers inserted key(Urls var)
P_UPLOAD = 'upload.php'

# Global most used vars
G_OSNAME = platform.system()  # Operating system's name
G_PCNAME = platform.uname()[1]  # Computer name
CONFIG_DIR = os.path.expanduser('~/.myRemote')  # Path where data is stored
KEY_FILE = '{0}/user.kb'.format(CONFIG_DIR)
PY_VERSION = sys.version_info[0]
COUNT = 0
INTERVAL = 1  # Interval for the timer.
