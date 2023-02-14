from kivymd.uix.relativelayout import RelativeLayout
from kivy.lang.builder import Builder
from kivy.properties import BooleanProperty
Builder.load_file("switchButton/SwitchButton.kv")


class SwithButtonWidget(RelativeLayout):
    active = BooleanProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.active = False

    def active_button(self):
        self.children[0].active = True

    def deactive_button(self):
        self.children[0].active = False

    def change_self_state(self, w):
        self.active = w.active
