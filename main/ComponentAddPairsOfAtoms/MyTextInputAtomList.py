from mytextInput.mytextInput import MyTextInput
from kivy.core.window import Window
from kivy.utils import platform


class MyTextInputAtomList(MyTextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def keyboard_on_key_down(self, keyboard, keycode, text, modifiers):
        match keycode[1]:
            case 'enter':
                self.parent.parent.go_to_the_next_text_input()
            case 'right':
                self.parent.parent.go_to_the_next_text_input()
            case 'backspace':
                if self.text != '':
                    self.do_backspace()
                else:
                    self.parent.parent.go_to_the_previous_text_input()
            case 'left':
                self.parent.parent.go_to_the_previous_text_input()
            case _:
                pass
