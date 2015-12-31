import webbrowser
import gtk.gdk
from imgurpython import ImgurClient


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

    def take_screenshot(self):
        # w = gtk.gdk.get_default_root_window()
        # sz = w.get_size()
        # print "The size of the window is %d x %d" % sz
        # pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, sz[0], sz[1])
        # pb = pb.get_from_drawable(w, w.get_colormap(), 0, 0, 0, 0, sz[0], sz[1])
        #
        # ts = time.time()
        # filename = "screenshot"
        # filename += str(ts)
        # filename += ".png"
        #
        # if (pb != None):
        #     pb.save(filename, "png")
        #     print "Screenshot saved to " + filename
        # else:
        #     print "Unable to get the screenshot."

#testen van IMGUR API deze details kloppen wel!
        client_id = '893455c3af30d48'
        client_secret = '8e6f8b5e5f23288e0c6e9dcc65407b31c68c79b1'

        client = ImgurClient(client_id, client_secret)

        # Example request
        items = client.gallery()
        for item in items:
            print(item.link)



