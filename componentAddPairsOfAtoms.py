from pprint import pprint
from kivymd.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from kivymd.uix.widget import Widget
from MyTextInputAtomList import MyTextInputAtomList
from kivymd.uix.scrollview import ScrollView
from enum import Enum


class Direction(Enum):
    FOREWARD = 1
    BACKWORD = 2


class ComponentAddPairsOfAtoms(RelativeLayout):
    label_height: dp = dp(20)
    spacing_padding: dp = dp(0)
    radius: dp = dp(20)
    position_of_circle: dp = dp(20)
    width_of_line: dp = dp(2)
    text_field_height: dp = dp(0)
    grid_height: dp = dp(0)
    widget: Widget = None
    number_of_add_rows_to_widget: int = 0
    NUMBER_OF_COLUMNS: int = 5
    content_in_MDScrollView_height: float = None
    content_outside_MDScrollView_height: float = None
    scroll_view: ScrollView = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        widget = MyTextInputAtomList()

        pprint(dir(widget))
        self.grid_height = self.label_height \
            + self.text_field_height + self.spacing_padding + 2 * dp(10)

    def add_row_of_text_input(self):
        """ Function adding rows of MDTextField into widget
        """
        self.ids.grid_with_atoms.height += (
            self.ids.text_field.height + dp(10))

        for _ in range(5):
            widget = MyTextInputAtomList()
            widget.parent_widget = self
            self.ids.grid_with_atoms.add_widget(widget)

        if self.number_of_add_rows_to_widget == 0:
            self.show_button_delete_row()

        self.number_of_add_rows_to_widget += 1

    def show_button_delete_row(self):
        self.ids.Button_delete.disabled = False
        self.ids.Button_delete.opacity = 1

    def hide_button_delete_row(self):
        self.ids.Button_delete.disabled = True
        self.ids.Button_delete.opacity = 0

    def delete_rows(self):
        for _ in range(5):
            self.ids.grid_with_atoms.remove_widget(
                self.ids.grid_with_atoms.children[0]
            )
        self.ids.grid_with_atoms.height -= (
            self.ids.text_field.height + dp(10))
        self.number_of_add_rows_to_widget -= 1

        if self.number_of_add_rows_to_widget == 0:
            self.hide_button_delete_row()

    def go_to_the_next_text_input(self) -> None:
        self._change_cursor_position_in_text_input_list(Direction.FOREWARD)

    def go_to_the_previous_text_input(self) -> None:
        self._change_cursor_position_in_text_input_list(Direction.BACKWORD)

    def _change_cursor_position_in_text_input_list(self, direction: Direction):

        length = (self.number_of_add_rows_to_widget + 1) * \
            self.NUMBER_OF_COLUMNS

        if direction == Direction.BACKWORD:
            last_element = length - 1
            j = 1
        elif direction == Direction.FOREWARD:
            last_element = 0
            j = -1

        for i in range(length):

            if self.ids.grid_with_atoms.children[i].focus and i == last_element:
                self.ids.grid_with_atoms.children[i].focus = False
                break

            elif self.ids.grid_with_atoms.children[i].focus:

                self.ids.grid_with_atoms.children[i].focus = False
                self.ids.grid_with_atoms.children[i+j].focus = True
                break

            else:
                continue
