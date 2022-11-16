import pprint
from kivymd.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from kivymd.uix.widget import Widget 
from mytextInput import MyTextInput



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
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
        self.grid_height = self.label_height \
            + self.text_field_height + self.spacing_padding + 2 * dp(10)
            
    def add_row_of_text_input(self):
        """ Function adding rows of MDTextField into widget
        """
        self.ids.grid_with_atoms.height += (self.ids.text_field.height + dp(10))
        
        for _ in range(5):
            widget = MyTextInput()
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
        self.ids.grid_with_atoms.height -= (self.ids.text_field.height + dp(10))
        self.number_of_add_rows_to_widget -= 1
        
        if self.number_of_add_rows_to_widget == 0:
            self.hide_button_delete_row()
            
    def jump_to_the_next_text_field(self):
        #TODO
        '''bind-keybord with this function
            check, that text field is clicked and active
            app.chenck_state_function have information of clicked text_field
            how check next text field in list'''
        pass
    