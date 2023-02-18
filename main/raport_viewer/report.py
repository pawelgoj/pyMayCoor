from kivy.uix.textinput import TextInput
from .button_copy import ButtonCopy
from kivy.properties import StringProperty


class Report(TextInput):
    button_copy: ButtonCopy | None = None
    name: StringProperty = StringProperty()
    selection: str = ''
    selection_range: tuple | None = None
    

    def on_selection_text(self, instance, value):
        # print(instance)
        if value != '':
            self.selection = self.selection_text
            self.selection_range = (self.selection_from, self.selection_to)
            super().on_selection_text(instance, value)

    def on_touch_down(self, touch):
        if touch.button == 'right':
            if self.button_copy is None\
                    and self.collide_point(*touch.pos):
                self.button_copy = ButtonCopy()
                self.button_copy.pos = touch.pos
                self.parent.add_widget(self.button_copy)
                if self.selection_range is not None:
                    self.select_text(*self.selection_range)
                    self.selection_range = None
        else:
            super().on_touch_down(touch)

    def remove_reference_to_button_copy(self):
        self.button_copy = None

    def on_touch_up(self, touch):
        if touch.button == 'right':
            pass
        else:
            super().on_touch_up(touch)
