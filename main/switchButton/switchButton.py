from kivymd.uix.relativelayout import RelativeLayout
from kivymd.uix.selectioncontrol.selectioncontrol import MDSwitch
from kivy.lang.builder import Builder
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
Builder.load_file("switchButton/SwitchButton.kv")


class SwithButtonWidget(RelativeLayout):
    active = BooleanProperty()
    name_of_widget = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.active = False

    def active_button(self):
        self.children[0].active = True

    def deactive_button(self):
        self.children[0].active = False

    def change_self_state(self, w):
        self.active = w.active


class MySwitch(MDSwitch):

    def on_touch_down(self, touch):
        if touch.button == 'left':
            if self.collide_point(*touch.pos):
                if self.active:
                    self.active = False
                else:
                    self.active = True

    def on_touch_up(self, touch):
        pass
