from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.lang.builder import Builder

Builder.load_file("NavBar/NavButton.kv")
Builder.load_file("NavBar/NavBar.kv")

from .navButton import NavButton

class NavBar(MDRelativeLayout, CommonElevationBehavior):
    from NavBar.user_actions import on_touch_up_find_input_file, on_touch_up_chose_output_file_directory,\
        on_touch_up_load_settings, on_touch_up_save_settings, on_enters