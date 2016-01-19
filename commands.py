from time import sleep
import webbrowser
import requests
import gtk.gdk
import wx
import base64
import constants as cfg


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

    def test(self):
        with open("zijn.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            print encoded_string

    def take_screenshot(self):
        print(cfg.G_OSNAME)
        if cfg.G_OSNAME == "Linux" or cfg.G_OSNAME == "Linux2":
            print('Screenshot requested.')
            w = gtk.gdk.get_default_root_window()
            sz = w.get_size()
            print "The size of the window is %d x %d" % sz
            pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
            pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])

            filename = "screenshot"
            filename += ".png"

            if (pb != None):
                pb.save(filename,"png")
                print "Screenshot saved to "+filename
                sleep(0.50)
                self.encode_image()
            else:
                print "Unable to get the screenshot."
        else:
            wx.App()  # Need to create an App instance before doing anything
            screen = wx.ScreenDC()
            size = screen.GetSize()
            bmp = wx.Bitmap(size[0], size[1])
            mem = wx.MemoryDC(bmp)
            mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
            mem.SelectObject(wx.NullBitmap)
            bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_JPEG)
            print('Bitmap saved')
            sleep(0.50)
            self.encode_image()


    def encode_image(self):
        with open("tux.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            full_encoded_string = "data:image/png;base64,{0}".format(encoded_string)
        encoded_string_file = '{0}/img.kb'.format(cfg.CONFIG_DIR)
        try:
            open(encoded_string_file, 'w+').write(full_encoded_string)
            sleep(0.50)
            print('Saved succesfully.')
            self.upload_image()
        except:
            print('pr0bz brother.. No base64 image string for you :3')


    def upload_image(self):
        key_file = '{0}/user.kb'.format(cfg.CONFIG_DIR)
        encoded_string_file = '{0}/img.kb'.format(cfg.CONFIG_DIR)
        data = open(encoded_string_file, 'r').readline()
        key = open(key_file, 'r').read()
        print('key = {0}').format(key)
        sleep(0.50)
        print(data)
        userdata = {'M':key, 'base64_str': data}
        resp = requests.post('%s%s'% (cfg.P_BASE, cfg.P_UPLOAD), data=userdata)
        print(resp.status_code)
        print('send')




