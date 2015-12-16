#!/usr/bin/env python

# File written by Evert Arends, all rights reserverd. First run: Thursday November 26 in 2015 around 3 PM.#
import os, os.path
import webbrowser
import base64
import sys
import threading
import constants as cfg
from commands import Commands

if cfg.PY_VERSION == 3:
    from urllib import urlopen
    raw_input = input
elif cfg.PY_VERSION == 2:
    from urllib.request import urlopen
    from __future__ import print_function


# Global functions
def filecheck():
    if not os.path.exists(cfg.CONFIG_DIR):
        os.mkdir(cfg.CONFIG_DIR)
        print('Created {0}'.format(cfg.CONFIG_DIR))

    key_file = '{0}/user.kb'.format(cfg.CONFIG_DIR)
    if os.path.exists(key_file):
        key = open(key_file, 'r').read()
        if len(key) == 0:
            print('Key is empty, please delete ~/.myRemote and try again')
            sys.exit(1)
        get_cmd()
    else:
        key = raw_input("Key?")
        open(key_file, 'w+').write(key)
        url = '{0}{1}{2}'.format(cfg.P_BASE, cfg.P_REGISTER, key)
        s = urlopen(url)
        request()
        print('Succesvol geregistreerd. (32 - 44)')


def request():
    key = '{0}/user.kb'.format(cfg.CONFIG_DIR)
    f = open(key)
    data = f.readline()
    f.close()
    print(data)
    s = urlopen(cfg.MY_IP)
    pip = s.read()

    # Encoding sData into a base64 string, so I can post spaces and weird characters.
    sData = base64.b64encode(data + ',' + cfg.G_PCNAME + ',' + cfg.G_OSNAME + ',' + pip)

    # Request URL with a get parameter, which makes it easier to store the data on the serverself.
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
    except:
        print('Input was not an integer :)')
        return

    # check if we recieved a valid command
    if not cfg.P_COMMAND:
        print('bleh')
        return

    commands = Commands()

    if inp == 1:
        commands.system_cmd(cfg.P_BASE + cfg.P_COMMAND + key)
    elif inp == 2:
        commands.open_webbrowser(cfg.P_BASE + cfg.P_COMMAND + key)

def get_cmd():
    data = '{0}/user.kb'.format(cfg.CONFIG_DIR)
    key = open(data, 'r').readline().strip()

    threading.Timer(2.0, get_cmd).start()
    content = urlopen('%s%s%s' % (cfg.P_BASE, cfg.P_GET, key))
    str = content.read()

    if key in str:
        content = urlopen('%s%s%s' % (cfg.P_BASE, cfg.P_MESSAGE, key)).read().strip()

        parse_cmd(content, key)


if __name__ == '__main__':
    filecheck()