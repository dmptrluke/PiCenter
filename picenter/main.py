# set config before importing
from kivy.config import Config
Config.set('graphics', 'resizable', 0)

# continue importing
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

from kivy.properties import ObjectProperty


class StatusTab(TabbedPanelItem):
    pass


class WeatherTab(TabbedPanelItem):
    pass


class MainPanel(TabbedPanel):
    tab_status = ObjectProperty(None)
    tab_weather = ObjectProperty(None)


class PiCenterApp(App):
    title = 'PiCenter'

    def build(self):
        Window.size = (800, 400)
        gui = MainPanel()
        return gui

if __name__ == '__main__':
    PiCenterApp().run()
