#!/usr/bin/env python

#File written by Evert Arends, all rights reserverd. First run: Thursday November 26 in 2015 around 3 PM.#
import os, os.path
import platform
import urllib2
import base64
import sys

CONFIG_DIR = os.path.expanduser('~/.myRemote')
IP = 'http://programmeerbazen.nl/ip.php' #Returns IP
P_GET = 'get.php?M=' #Returns key if positive
P_DATA = 'data.php?data=' #Inserts information
P_BASE = 'https://myremote.io/panel/stub/' #Base URL, every url that needs this gets included (baseurl + var)
P_MESSAGE = 'msg.php?M=' #Check if there is a message availible (Url var)
P_COMMAND = 'cmd.php?M=' #Gets the command from DB(Urls var)
P_REGISTER = 'reg.php?K=' #Registers inserted key(Urls var)

def request():
    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)
        print('Created {0}'.format(CONFIG_DIR))

    key_file = '{0}/user.kb'.format(CONFIG_DIR)
    if os.path.exists(key_file):
        key = open(key_file, 'r').read()
        if len(key) == 0:
            print('Key is empty, please delete ~/.myRemote and try again')
            sys.exit(1)
    else:
        key = raw_input("Key?")
        open(key_file, 'w+').write(key)
        url = '{0}{1}{2}'.format(P_BASE, P_REGISTER, key)
        s = urlopen(url)
        print(url)
        print('Success!')

    s = urlopen(IP)
    pcName = platform.uname()[1]
    osName = platform.system()
    pip = s.read()
    #Encoding sData into a base64 string, so I can post spaces and weird characters.
    sData = base64.b64encode(key + ',' + pcName + ',' + osName + ',' + pip)
    #Request URL with a get parameter, which makes it easier to store the data on the serverself.
    P_URL = '{0}{1}{2}'.format(P_BASE, P_DATA, sData)
    s = urlopen(P_URL)
    s = s.read()
    print(s)

if __name__ == '__main__':
    request()

