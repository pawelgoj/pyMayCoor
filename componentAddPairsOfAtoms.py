from kivymd.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivymd.uix.textfield.textfield import MDTextField
from kivy.properties import NumericProperty
from kivymd.uix.button.button import MDFloatingActionButton
from kivymd.uix.widget import Widget 
from kivy.animation import Animation

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
        
        widget = MDTextField()
        self.ids.grid_with_atoms.add_widget(widget)
        widget = MDTextField()
        self.ids.grid_with_atoms.add_widget(widget)
        widget = MDTextField()
        self.ids.grid_with_atoms.add_widget(widget)
        widget = MDTextField()
        self.ids.grid_with_atoms.add_widget(widget)
        widget = MDTextField()
        self.ids.grid_with_atoms.add_widget(widget)
        
        if self.number_of_add_rows_to_widget == 0:
            self.show_button_delete_row()
            
        if self.ids.Button_delete:
            Animation.cancel_all(self, "_elevation")
        self.number_of_add_rows_to_widget += 1
        
    def show_button_delete_row(self):
        if self.ids.Button_delete:
            Animation.cancel_all(self, "_elevation")
        self.ids.Button_delete.disabled = False
        self.ids.Button_delete.opacity = 1
        
    def delete_rows(self):
        print("")

        
