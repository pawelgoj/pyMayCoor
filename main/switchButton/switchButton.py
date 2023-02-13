from kivymd.uix.relativelayout import RelativeLayout
from kivy.lang.builder import Builder

Builder.load_file("switchButton/SwitchButton.kv")


class SwithButtonWidget(RelativeLayout):
    def active_button(self):
        self.children[0].active = True

    def deactive_button(self):
        self.children[0].active = False
