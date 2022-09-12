from screens.rootscreen.rootscreen import rootscreen

from kivymd.app import MDApp

class tunniplaan(MDApp):
    def build(self):
        self.load_all_kv_files(self.directory)
        return rootscreen()

    def on_start(self):
        self.root.update()
        pass

if __name__ == '__main__':
    tunniplaan().run()
