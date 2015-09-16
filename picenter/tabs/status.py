from kivy.uix.tabbedpanel import TabbedPanelItem


class StatusTab(TabbedPanelItem):
    def __init__(self, **kwargs):
        # initialise widget
        super().__init__(**kwargs)
