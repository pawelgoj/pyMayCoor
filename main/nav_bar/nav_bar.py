from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.lang.builder import Builder
from back_end_for_kivy import MenagerAppBackEnd
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
import webbrowser

Builder.load_file("nav_bar/navbar.kv")


class MyDropdownMenu(MDDropdownMenu):
    def check_position_caller(self, instance_window, width, height):
        self.dismiss()


class NavBar(MDRelativeLayout, CommonElevationBehavior):
    from .user_actions import on_touch_up_find_input_file, \
        on_touch_up_chose_export_file, on_touch_up_load_settings,\
        on_touch_up_save_settings, on_enters, on_touch_up_run_program,\
        remove_dialog

    dialog = None
    menu: MyDropdownMenu

    MenagerAppBackEnd: type

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.MenagerAppBackEnd = MenagerAppBackEnd

        if self.MenagerAppBackEnd.check_is_instance() is False:
            self.MenagerAppBackEnd.new_app_back_end(progress_bar=True)

        self.menu = MyDropdownMenu(
            background_color=(0.6, 0.6, 0.6),
            items=[{'viewclass': 'OneLineListItem',
                   'text': 'Project github repository',
                    'height': dp(40),
                    'on_release': lambda x="Project github repository": self.got_to_repo(x)},
                   {'viewclass': 'OneLineListItem',
                   'text': 'Project website',
                    'height': dp(40),
                    'on_release': lambda x="Project website": self.got_to_website(x)}
                   ],

            width_mult=4
        )

    def show_menu_bar(self, button):
        self.menu.caller = button
        self.menu.open()

    def got_to_repo(self, button):
        webbrowser.open('https://github.com/pawelgoj/pyMayCoor')
        self.menu.dismiss()

    def got_to_website(self, button):
        webbrowser.open('https://pawelgoj.github.io/pyMayCoor/bond_order_processing')
        self.menu.dismiss()
