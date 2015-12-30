import webbrowser
import gtk.gdk
import time


class Commands():
    def __init__(self):
        pass

    def system_cmd(self, cmd):
        print('system cmd called')
        print(cmd)

    def open_webbrowser(self, url):
        print('open webbrowser called')
        webbrowser.open(url)
        print(url)

    def take_screenshot(self):
        w = gtk.gdk.get_default_root_window()
        sz = w.get_size()
        print "The size of the window is %d x %d" % sz
        pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, sz[0], sz[1])
        pb = pb.get_from_drawable(w, w.get_colormap(), 0, 0, 0, 0, sz[0], sz[1])

        ts = time.time()
        filename = "screenshot"
        filename += str(ts)
        filename += ".png"

        if (pb != None):
            pb.save(filename, "png")
            print "Screenshot saved to " + filename
        else:
            print "Unable to get the screenshot."
