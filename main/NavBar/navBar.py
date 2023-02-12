from .navButton import NavButton
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.lang.builder import Builder
from back_end_for_kivy import MenagerAppBackEnd

from app_back_end import AppBackEnd
Builder.load_file("NavBar/NavButton.kv")
Builder.load_file("NavBar/NavBar.kv")


class NavBar(MDRelativeLayout, CommonElevationBehavior):
    from NavBar.user_actions import on_touch_up_find_input_file, \
        on_touch_up_chose_export_file, on_touch_up_load_settings,\
        on_touch_up_save_settings, on_enters, on_touch_up_run_program,\
        remove_dialog

    MenagerAppBackEnd: type

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.MenagerAppBackEnd = MenagerAppBackEnd

        if self.MenagerAppBackEnd.check_is_instance() is False:
            self.MenagerAppBackEnd.new_app_back_end()

        # Here must be imported module after inicializtion
        # of main_kivy
