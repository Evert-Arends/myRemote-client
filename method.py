import constants as cfg
import os
import base64
import socket
import myRemote as mrt

# defining used python version.
if cfg.PY_VERSION == 3:
    from urllib2 import urlopen
    raw_input = input
elif cfg.PY_VERSION == 2:
    from urllib import urlopen


# Returning everything that is in the key file.
def get_key_info():
    """
    :rtype: basestring
    """
    if os.path.exists(cfg.KEY_FILE):
        key = open(cfg.KEY_FILE, 'r').read()
        if len(key) == 0:
            return "None"
        else:
            return key
    else:
        return 0


def register_client():
    key = raw_input('Authentication Key?')
    api = raw_input('API key?')
    parameter = base64.b64encode(api + ',' + key)
    open(cfg.KEY_FILE, 'w+').write(parameter)
    url = '{0}{1}{2}'.format(cfg.P_BASE, cfg.P_REGISTER, parameter)
    s = urlopen(url)
    s = s.read()
    if "set" in s:
        print ('Registration successful.')
        mrt.request()
    else:
        print('There could\'ve bin a misunderstanding. myRemote can be buggy from here..')


def get_client_ip():
    url = 'https://myremote.io/user/ip.php'
    s = urlopen(url)
    ip = s.read()

    # checking if ip is a valid ip.
    try:
        socket.inet_aton(ip)
        return ip
    except socket.error:
        return '127.0.0.1'
