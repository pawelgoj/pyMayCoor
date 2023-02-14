from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from back_end_for_kivy import MenagerAppBackEnd

Builder.load_file("mytextInput/MyTextInput.kv")


class MyTextInput(MDTextField):
    name_of_widget = StringProperty()

    def get_data_to_settings(self, widget):
        MenagerAppBackEnd.change_settings_item(
            widget.name_of_widget,
            widget.text
        )
