from kivy.uix.textinput import TextInput
from .button_copy import ButtonCopy
from kivy.properties import StringProperty
from kivy.core.text import markup


class ReportSegment(TextInput):
    button_copy: ButtonCopy | None = None
    name: StringProperty = StringProperty()
    selection: str = ''
    selection_range: tuple | None = None
    start_selection: bool = False

    def on_selection_text(self, instance, value):

        if value != '':
            self.selection = self.selection_text
            if self.selection_to >= self.selection_from:
                self.selection_range = (self.selection_from, self.selection_to)
            else:
                self.selection_range = (self.selection_to, self.selection_from)
            super().on_selection_text(instance, value)

    def on_touch_down(self, touch):
        if touch.button == 'right':
            if self.button_copy is None\
                    and self.collide_point(*touch.pos)\
                    and self.selection != '':
                self.button_copy = ButtonCopy()
                self.button_copy.pos = touch.pos
                self.parent.add_widget(self.button_copy)
                if self.selection_range is not None:
                    self.select_text(*self.selection_range)
                    self.selection_range = None
        else:
            super().on_touch_down(touch)

    def on_cursor(self, instance, value):

        try:
            height_in_scroll = self.parent.parent.parent.height
            scroll_height = self.parent.parent.parent.parent.height

            if (((self.cursor_pos[1] - scroll_height + 30)
                    / (height_in_scroll - scroll_height))
                > self.parent.parent.parent.parent.scroll_y)\
                    and height_in_scroll > scroll_height:

                self.parent.parent.parent.parent.scroll_y\
                    = ((self.cursor_pos[1] - scroll_height + 30)
                        / (height_in_scroll - scroll_height))

            elif (((self.cursor_pos[1] - 60)
                    / (height_in_scroll - scroll_height))
                    < self.parent.parent.parent.parent.scroll_y)\
                    and height_in_scroll > scroll_height:

                self.parent.parent.parent.parent.scroll_y\
                    = ((self.cursor_pos[1] - 60)
                        / (height_in_scroll
                            - scroll_height))
        except (ZeroDivisionError, AttributeError):
            pass

        super().on_cursor(instance, value)

    def remove_reference_to_button_copy(self):
        self.button_copy = None

    def on_text(self, widget, text):
        number_of_rows = text.count('\n')
        self.height = self.line_height * (4 + number_of_rows)
