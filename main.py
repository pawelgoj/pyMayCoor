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
    pass


if __name__ == '__main__':
    BondOrderApp().run()