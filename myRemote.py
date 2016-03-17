#!/usr/bin/env python
# File written by Evert Arends, all rights reserverd. First run: Thursday November 26 in 2015 around 3 PM.#

from __future__ import print_function
import os
import sys
import base64
import os.path
import datetime
import threading
import method as mtd
import constants as cfg
from commands import Commands

# defining used python version.
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
    key_file = mtd.get_key_info()
    print("Keyfile:", key_file)
    if key_file == 0:
        if key_file == 0:
            mtd.register_client()
    elif key_file == "None":
        print('key file seems to be empty, please delete ~/.myRemote and try again')
        sys.exit()
    else:
        get_cmd()


def request():
    """
        Requests data from the server, it gets the base64 encoded string from a file.
        This string contains API and KEY authentication.
    """
    data = mtd.get_key_info()
    client_ip = mtd.get_client_ip()

    # The Encoded data in a base64 string, so I can post spaces and weird characters.
    # Decode they key, so its not double encoded.
    data = base64.b64decode(data)
    server_data = base64.b64encode(data + ',' + cfg.G_PCNAME + ',' + cfg.G_OSNAME + ',' + client_ip)

    print("server data = " + server_data)
    # Request URL with a get parameter, which makes it easier to store the data on the server self.
    full_url = '{0}{1}{2}'.format(cfg.P_BASE, cfg.P_DATA, server_data)
    s = urlopen(full_url).read()
    print(s)

    # Starting loop to get a server reply.
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
    cfg.COUNT += 1  # Count the total requests this session.
    key = mtd.get_key_info()

    threading.Timer(cfg.INTERVAL, get_cmd).start()  # Starts the timer loop to request data from the server.

    logging = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Request: #" + str(cfg.COUNT) +
               " With a set interval of: " + str(cfg.INTERVAL))  # Sets string for logbook.
    print(logging)  # To see the result in the terminal.
    mtd.error_logging(logging)  # Function to put data into the log.

    content = urlopen('%s%s%s' % (cfg.P_BASE, cfg.P_GET, key))
    imported_content = content.read().strip()

    if key == imported_content:
        content = urlopen('%s%s%s' % (cfg.P_BASE, cfg.P_MESSAGE, key)).read().strip()
        print('Key is in imported_content', content)
        parse_cmd(content, key)


if __name__ == '__main__':
    filecheck()
