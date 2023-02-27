from kivymd.uix.textfield import MDTextField
from kivy.lang.builder import Builder
from kivy.properties import StringProperty


Builder.load_file("my_text_input/mytextInput.kv")


class MyTextInput(MDTextField):
    name_of_widget: StringProperty = StringProperty()

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
