from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang.builder import Builder

Builder.load_file("mytextInput/MyTextInput.kv")

class MyTextInput(MDTextField):
    pass
            
