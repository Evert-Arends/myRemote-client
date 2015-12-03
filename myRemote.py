#!/usr/bin/env python

#File written by Evert Arends, all rights reserverd. First run: Thursday November 26 in 2015 around 3 PM.#
import os, os.path
import platform
import urllib2
import base64
import sys

CONFIG_DIR = os.path.expanduser('~/.myRemote') # Path where data is stored
IP = 'http://programmeerbazen.nl/ip.php' # Returns IP
P_GET = 'get.php?M=' # Returns key if positive
P_DATA = 'data.php?data=' # Inserts information
P_BASE = 'PATH_TO_API' # Base URL, every url that needs this gets included (baseurl + var)
P_MESSAGE = 'msg.php?M=' # Check if there is a message availible (Url var)
P_COMMAND = 'cmd.php?M=' # Gets the command from DB(Urls var)
P_REGISTER = 'reg.php?K=' # Registers inserted key(Urls var)

# Global most used vars

G_OSNAME = platform.system() # Operating system's name
G_PCNAME = platform.uname()[1] # Computername

# Global functions

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# !Global functions

def filecheck():
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)
        print('Created {0}'.format(CONFIG_DIR))

    key_file = '{0}/user.kb'.format(CONFIG_DIR)
    if os.path.exists(key_file):
        key = open(key_file, 'r').read()
        if len(key) == 0:
            print('Key is empty, please delete ~/.myRemote and try again')
            sys.exit(1)
        request_me()
    else:
        key = raw_input("Key?")
        open(key_file, 'w+').write(key)
        url = '{0}{1}{2}'.format(P_BASE, P_REGISTER, key)
        s = urlopen(url)
        request()
        print('Succesvol geregistreerd. (32 - 44)')
def request():
    key = '{0}/user.kb'.format(CONFIG_DIR)
    f = open(key)
    data = f.readline()
    f.close()
    print data
    s = urlopen(IP)
    pip = s.read()

    # Encoding sData into a base64 string, so I can post spaces and weird characters.

    sData = base64.b64encode(data + ',' + G_PCNAME + ',' + G_OSNAME + ',' + pip)

    # Request URL with a get parameter, which makes it easier to store the data on the serverself.

    P_URL = '{0}{1}{2}'.format(P_BASE, P_DATA, sData)
    s = urlopen(P_URL)
    s = s.read()
    print(s)
    request_me()
def request_me():
    data = '{0}/user.kb'.format(CONFIG_DIR)
    f = open(data)
    key = f.readline()
    f.close()
    import threading
    threading.Timer(5.0, request_me).start()
    c = urlopen(P_BASE + P_GET + key)
    str = c.read()
    if key in str:
        c = urlopen(P_BASE + P_MESSAGE + key)
        c = c.read()
        if "1" in c:
            print('Het werkt :D :D :D')
if __name__ == '__main__':
    filecheck()
