from back_end_for_kivy import MenagerAppBackEnd
from mytextInput.mytextInput import MyTextInput
import re
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang.builder import Builder
Builder.load_file("ComponentAddPairsOfAtoms/MyTextInputAtomList.kv")


class MyTextInputAtomList(MyTextInput):

    self_change_color: bool = False
    iteration: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def keyboard_on_key_down(self, keyboard, keycode, text, modifiers):
        match keycode[1]:
            case 'enter':
                self.parent.parent.go_to_the_next_text_input()
                self._add_red_color_if_wrong_input_key_action('min_mbo_')
                self._add_red_color_if_wrong_input_key_action('max_mbo_')
            case 'right':
                self.parent.parent.go_to_the_next_text_input()
                self._add_red_color_if_wrong_input_key_action('min_mbo_')
                self._add_red_color_if_wrong_input_key_action('max_mbo_')
            case 'backspace':
                if self.text != '':
                    self.do_backspace()
                else:
                    self.parent.parent.go_to_the_previous_text_input()
            case 'left':
                self.parent.parent.go_to_the_previous_text_input()
                self._add_red_color_if_wrong_input_key_action('min_mbo_')
                self._add_red_color_if_wrong_input_key_action('max_mbo_')
            case _:
                pass

    def _add_red_color_if_wrong_input_key_action(self, key: str):
        if key in self.name_of_widget \
                and (re.fullmatch(r'[0-9]+[\.,]{1}', self.text) is not None):

            self.self_change_color = True
            self.text_color_normal = 'red'
            self.text_color_focus = 'red'

    def get_data_to_settings(self, widget):

        if 'min_mbo_' in widget.name_of_widget \
            and (re.fullmatch(r'[0-9]+[\.,]{1}[0-9]+|[0-9]+|[0-9]+[\.,]{1}',
                              widget.text) is None):

            self.self_change_color = True
            widget.text_color_normal = 'red'
            widget.text_color_focus = 'red'

        elif 'max_mbo_' in widget.name_of_widget \
            and (re.fullmatch(r'[0-9]+[\.,]{1}[0-9]+|[0-9]+|[0-9]+[\.,]{1}|INF',
                 widget.text) is None):

            self.self_change_color = True
            widget.text_color_normal = 'red'
            widget.text_color_focus = 'red'

        else:
            from main_kivy import myApp
            self.self_change_color = False

            widget.text_color_normal = myApp.theme_cls.text_color
            widget.text_color_focus = myApp.theme_cls.primary_color

        MenagerAppBackEnd.change_settings_item(
            widget.name_of_widget,
            widget.text
        )

    def on_text_color_normal_check(self, widget):

        if self.self_change_color is True:
            widget.text_color_normal = 'red'

    def on_text_color_focus_check(self, widget):
        if self.self_change_color is True:
            widget.text_color_focus = 'red'
