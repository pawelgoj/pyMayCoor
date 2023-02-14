from .myRectangelButton import MyRectangleButton
from .MyTextInputAtomList import MyTextInputAtomList
from kivymd.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from kivymd.uix.widget import Widget
from kivymd.uix.scrollview import ScrollView
from kivy.lang.builder import Builder
from enum import Enum

Builder.load_file("ComponentAddPairsOfAtoms/ComponentAddPairsOfAtoms.kv")
Builder.load_file("ComponentAddPairsOfAtoms/MyRectangleButton.kv")


class Direction(Enum):
    FOREWARD = 1
    BACKWORD = 2


class ComponentAddPairsOfAtoms(RelativeLayout):
    ids_list: tuple[str] = ('atom_id_1_', 'atom_id_2_',  'min_mbo_',
                            'max_mbo_', 'bond_id_')
    added_widgets: dict[str, Widget] = {}
    label_height: dp = dp(20)
    spacing_padding: dp = dp(0)
    radius: dp = dp(20)
    position_of_circle: dp = dp(20)
    width_of_line: dp = dp(2)
    text_field_height: dp = dp(0)
    grid_height: dp = dp(0)
    number_of_add_rows_to_widget: int = 0
    NUMBER_OF_COLUMNS: int = 5
    content_in_MDScrollView_height: float = None
    content_outside_MDScrollView_height: float = None
    scroll_view: ScrollView = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.grid_height = self.label_height \
            + self.text_field_height + self.spacing_padding + 2 * dp(10)

    def add_row_of_text_input(self):
        """ Function adding rows of MDTextField into widget
        """
        self.ids.grid_with_atoms.height += (
            self.ids.atom_id_1_0.height + dp(10))

        for i in range(5):
            widget = MyTextInputAtomList()
            widget.name_of_widget = self.ids_list[i]\
                + str(self.number_of_add_rows_to_widget + 1)
            id = self.ids_list[i] + str(self.number_of_add_rows_to_widget + 1)
            self.added_widgets.update({id: widget})
            widget.parent_widget = self
            self.ids.grid_with_atoms.add_widget(widget)

        if self.number_of_add_rows_to_widget == 0:
            self.show_button_delete_row()

        self.number_of_add_rows_to_widget += 1

    def add_content_to_text_input(self, id: str, nr: int, content: str):
        id = id + str(nr)
        if nr > 0:
            self.added_widgets[id].text = content
        elif nr == 0:
            self.ids[id].text = content
        else:
            raise ValueError("Wrong nr!!!!!")

    def show_button_delete_row(self):
        self.ids.Button_delete.disabled = False
        self.ids.Button_delete.opacity = 1

    def hide_button_delete_row(self):
        self.ids.Button_delete.disabled = True
        self.ids.Button_delete.opacity = 0

    def delete_rows(self):
        if self.number_of_add_rows_to_widget > 0:
            for i in range(5):
                id = self.ids_list[i] + str(self.number_of_add_rows_to_widget)

                self.ids.grid_with_atoms.remove_widget(
                    self.ids.grid_with_atoms.children[0]
                )
            del self.added_widgets[id]

            self.ids.grid_with_atoms.height -= (
                self.ids.atom_id_1_0.height + dp(10))

            self.number_of_add_rows_to_widget -= 1

        if self.number_of_add_rows_to_widget == 0:
            self.hide_button_delete_row()

    def reset_rows(self):
        for _ in range(self.number_of_add_rows_to_widget):
            self.delete_rows()
        self.hide_button_delete_row()

    def add_rows(self, number: int):
        if number > 0:
            for _ in range(number):
                self.add_row_of_text_input()
            self.show_button_delete_row()

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
