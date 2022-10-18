import time
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')

from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder


Builder.load_file("ComponentAddPairsOfAtoms.kv")
Builder.load_file("ComponentChoseCalculations.kv")
Builder.load_file("SwitchButton.kv")

class MainFrameOfApp(FloatLayout):
    pass


class BondOrderApp(MDApp):

    text_input = None
    count = 0 
    
    def on_start(self):
        #chose theme of app
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"
        
    def switch_theme_style(self): 
        if self.text_input != None:
            self.text_input.focus = True

        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Purple" else "Purple"
        )

        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        if self.text_input != None:
            self.text_input.focus = False
            
    def change_state(self, widget):
        self.text_input = widget

        



if __name__ == '__main__':
    BondOrderApp().run()