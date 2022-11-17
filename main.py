from kivymd.color_definitions import colors
from kivy.utils import platform
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from pprint import pprint
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')


Builder.load_file("ComponentAddPairsOfAtoms.kv")
Builder.load_file("ComponentChoseCalculations.kv")
Builder.load_file("SwitchButton.kv")
Builder.load_file("MyRectangleButton.kv")
Builder.load_file("MytextInput.kv")


class MainFrameOfApp(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BondOrderApp(MDApp):

    text_input = None

    def on_start(self):
        # chose theme of app it must be in app object not in mainWidget
        temp = self.theme_cls.colors
        temp["Dark"] = {
            "StatusBar": "E0E0E0",
            "AppBar": "#202020",
            "Background": "#252628",
            "CardsDialogs": "#FFFFFF",
            "FlatButtonDown": "#CCCCCC",
        }

        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.primary_dark_hue = "600"
        self.theme_cls.theme_style = "Light"

    def switch_theme_style(self):
        if self.text_input != None:
            # This statement is because strange preserved of MDtextInput
            # Focused MDtextInput not correct change Theme
            try:
                self.text_input.focus = True
            except:
                # If ocurred: ReferenceError: weakly-referenced object no longer exists
                self.text_input = None

        self.theme_cls.primary_palette = (
            "DeepOrange" if self.theme_cls.primary_palette == "DeepPurple" else "DeepPurple"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

        if self.text_input != None:
            try:
                self.text_input.focus = False
            except:
                self.text_input = None

    def change_state(self, widget):
        self.text_input = widget


if __name__ == '__main__':
    myApp = BondOrderApp()
    myApp.run()
