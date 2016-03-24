import requests

import method
import constants as cfg


class Communication():
    def __init__(self):
        print('class communication requested.')

    def upload(self, b64encoded):
        key = method.get_key_info()

        if not isinstance(b64encoded, (str, unicode)):
            raise Exception('We can only send b64 strings!')

        userdata = {'M': key, 'base64_str': b64encoded}

        print('sending')

        try:
            resp = requests.post('%s%s' % (cfg.P_BASE, cfg.P_UPLOAD), data=userdata)

            if not resp.status_code == 200:
                raise Exception('status code not 200')
        except Exception as ex:
            print 'upload failed: %s' % str(ex)

        print('sent')

    def getdata(self, base, dir_to, end):
        url = '{0}{0}{0}'.format(base, dir_to, end)
        content = requests.get(url)

        return content