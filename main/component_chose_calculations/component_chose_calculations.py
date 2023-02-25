from kivymd.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder

from back_end_for_kivy import MenagerAppBackEnd


Builder.load_file("component_chose_calculations/componentchosecalculations.kv")


class ComponentChoseCalculations(GridLayout):
    def change_settings_calc(self, button):
        MenagerAppBackEnd.change_settings_item(button.name_of_widget,
                                               button.active)

    def change_qi_id_in_settings(self, input_text):
        MenagerAppBackEnd.change_settings_item(
            'q_i_bond_id', str(input_text.text))
