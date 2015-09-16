from kivy.uix.tabbedpanel import TabbedPanelItem


class OutsideTab(TabbedPanelItem):
    def __init__(self, **kwargs):
        # initialise widget
        super().__init__(**kwargs)
