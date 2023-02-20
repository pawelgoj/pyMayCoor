from kivy.uix.textinput import TextInput
from .button_copy import ButtonCopy
from kivy.properties import StringProperty
from kivy.core.text import markup


class ReportSegment(TextInput):
    button_copy: ButtonCopy | None = None
    name: StringProperty = StringProperty()
    selection: str = ''
    selection_range: tuple | None = None
    from_select: tuple[int, int] | None = None

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
                    self.from_select = None
        else:
            if touch.button == 'left'\
                    and self.collide_point(*touch.pos):
                self.from_select = self.cursor_index()

            super().on_touch_down(touch)

    def keyboard_on_key_down(self, keyboard, keycode, text, modifiers):

        if keycode[1] in ('right', 'down', 'left', 'up'):

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

        super().keyboard_on_key_down(keyboard, keycode, text, modifiers)

    def remove_reference_to_button_copy(self):
        self.button_copy = None
        self.from_select = None

    def on_touch_up(self, touch):
        if touch.button == 'right':
            self.from_select = None
        else:
            super().on_touch_up(touch)

    def on_focus(self, instance, value):
        self.from_select = None

    # def on_touch_move(self, touch):
    #     if self.collide_point(*touch.pos):
    #         if self.from_select is None:
    #             self._selection_to = self.cursor_index()
    #         else:
    #             self._selection_from = self.from_select
    #             self.cursor = self.get_cursor_from_xy(touch.x, touch.y)
    #             self._selection_to = self.cursor_index()
    #             self._update_selection()

    def on_text(self, widget, text):
        number_of_rows = text.count('\n')
        self.height = self.line_height * (4 + number_of_rows)
