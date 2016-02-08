#!/usr/bin/env python
# File written by Evert Arends, all rights reserverd. First run: Thursday November 26 in 2015 around 3 PM.#
from __future__ import print_function
import os, os.path
import webbrowser
import base64
import sys
import threading
import constants as cfg
from commands import Commands

if cfg.PY_VERSION == 3:
    from urllib2 import urlopen
    raw_input = input
elif cfg.PY_VERSION == 2:
    from urllib import urlopen


# Global functions
def filecheck():
    if not os.path.exists(cfg.CONFIG_DIR):
        os.mkdir(cfg.CONFIG_DIR)
        print('Created {0}'.format(cfg.CONFIG_DIR))

    key_file = '{0}/user.kb'.format(cfg.CONFIG_DIR)
    if os.path.exists(key_file):
        key = open(key_file, 'r').read()
        if len(key) == 0:
            print('Keyfile is empty, please delete ~/.myRemote and try again')
            sys.exit(1)
        get_cmd()
    else:
        key = raw_input('Authentication Key?')
        API = raw_input('API key?')
        parameter = base64.b64encode(API + ',' + key)
        open(key_file, 'w+').write(parameter)
        url = '{0}{1}{2}'.format(cfg.P_BASE, cfg.P_REGISTER, parameter)
        s = urlopen(url)
        s = s.read()
        if "set" in s:
            print ('Registration successful.')
            request()
        else:
            print('There could\'ve bin a misunderstanding. myRemote can be buggy from here..')
            print (s)


def request():
    """
        Requests data from the server, it gets the base64 encoded string from a file.
        This string contains API and KEY authentication.
    """
    key = '{0}/user.kb'.format(cfg.CONFIG_DIR)
    f = open(key)
    data = f.readline()
    f.close()
    print(data)
    # s = urlopen(cfg.MY_IP)
    # pip = s.read()
    pip = cfg.MY_IP
    # Encoding sData into a base64 string, so I can post spaces and weird characters.
    # decode they key, so its not double encoded.
    data = base64.b64decode(data)
    str = base64.b64encode(data + ',' + cfg.G_PCNAME + ',' + cfg.G_OSNAME + ',' + pip)
    sData = str
    print("sData = " + sData)
    # Request URL with a get parameter, which makes it easier to store the data on the server self.
    P_URL = '{0}{1}{2}'.format(cfg.P_BASE, cfg.P_DATA, sData)
    s = urlopen(P_URL).read()
    print(s)
    get_cmd()


def parse_cmd(inp, key):
    """
    This function validates the data we received from the API
    and delegates the appropriate responses to that data.
    """

    # First check if inp can be parsed as an integer
    try:
        int(inp)
        print(inp)
    except:
        print('Input was not an integer :)')
        return

    commands = Commands()

    if inp == '1':
        print('input 1')
        message = urlopen('%s%s%s' % (cfg.P_BASE, cfg.P_COMMAND, key))
        message = message.read().strip()
        commands.system_cmd(message)
    elif inp == '2':
        url_to_open = urlopen('%s%s%s' % (cfg.P_BASE, cfg.P_COMMAND, key))
        url_to_open = url_to_open.read().strip()
        commands.open_webbrowser(url_to_open)
    elif inp == '3':
        url_to_open = urlopen('%s%s%s' % (cfg.P_BASE, cfg.P_COMMAND, key))
        commands.take_screenshot()

def get_cmd():
    data = '{0}/user.kb'.format(cfg.CONFIG_DIR)
    key = open(data, 'r').readline().strip()
    threading.Timer(2.0, get_cmd).start()
    content = urlopen('%s%s%s' % (cfg.P_BASE, cfg.P_GET, key))
    str = content.read().strip()
    if key == str:
        content = urlopen('%s%s%s' % (cfg.P_BASE, cfg.P_MESSAGE, key)).read().strip()
        print('Key is in str', content)
        parse_cmd(content, key)


if __name__ == '__main__':
    filecheck()