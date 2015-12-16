import webbrowser


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