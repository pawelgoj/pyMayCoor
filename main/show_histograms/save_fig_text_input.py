from kivymd.uix.textfield import MDTextField
from kivy.lang.builder import Builder

Builder.load_file("show_histograms/savefigtextinput.kv")

class SaveFigTextInput(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_up(self, touch):
        if touch.button == 'left':
            try:
                return super().on_touch_up(touch)
            except IndexError:
                pass

    def on_touch_down(self, touch):
        if touch.button == 'left':
            try:
                return super().on_touch_down(touch)
            except IndexError:
                pass
