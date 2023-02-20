from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang.builder import Builder
from kivy.properties import StringProperty


Builder.load_file("mytextInput/MyTextInput.kv")


class MyTextInput(MDTextField):
    name_of_widget: StringProperty = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_up(self, touch):
        if touch.button == 'left':
            return super().on_touch_up(touch)

    def on_touch_down(self, touch):
        if touch.button == 'left':
            return super().on_touch_down(touch)
