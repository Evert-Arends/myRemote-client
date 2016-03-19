from time import sleep
import webbrowser
import requests
import base64
import constants as cfg

from bin.screenshot import Screenshot


class Commands():
    def __init__(self):
        pass

    def system_cmd(self, cmd):
        print('system cmd called')
        print(cmd)

    def open_webbrowser(self, url):
        print('open webbrowser called')
        if 'http://' not in url:
            url = 'http://{0}'.format(url)
        webbrowser.open(url)
        print(url)
