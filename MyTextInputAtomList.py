from mytextInput import MyTextInput
from kivy.core.window import Window
from kivy.utils import platform

class MyTextInputAtomList(MyTextInput):
    def keyboard_on_key_down(self, keyboard, keycode, text, modifiers):
        match keycode[1]:
            case 'enter':
                print("In text field!!!!")
            case _:
                pass