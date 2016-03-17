import constants as cfg
import os


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
