# generic imports
from time import localtime, strftime
from socket import gethostname

# set config before importing
from kivy.config import Config
Config.set('graphics', 'resizable', 0)

# kivy imports
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.storage.jsonstore import JsonStore

# picenter imports
from picenter.tabs.status import StatusTab
from picenter.tabs.outside import OutsideTab


class MainFrame(FloatLayout):
    def __init__(self, **kwargs):
        # initialise widget
        super().__init__(**kwargs)

        # set dynamic variables
        self.ids.status_host.text = gethostname()
        Clock.schedule_interval(self.update, 1)

        # initial update
        self.update()

    def update(self, *args):
        self.ids.status_time.text = strftime("%I:%M %p", localtime())


class PiCenterApp(App):
    title = 'PiCenter'

    def build(self):
        # set window size
        Window.size = (800, 480)

        # initialise main panel and start updates
        application = MainFrame()

        return application

if __name__ == '__main__':
    PiCenterApp().run()
