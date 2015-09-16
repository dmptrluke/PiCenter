# generic imports
from time import localtime, strftime
from socket import gethostname
import json

# set config before importing
from kivy.config import Config
Config.set('graphics', 'resizable', 0)

# kivy imports
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

# picenter imports
from picenter.tabs.status import *
from picenter.tabs.outside import *


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
        Window.size = (800, 480)
        return MainFrame()

    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })

    def build_settings(self, settings):
        with open('config_template.json') as template:
            settings.add_json_panel('PiCenter', self.config, data=template.read())

if __name__ == '__main__':
    PiCenterApp().run()
