from kivymd.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivymd.uix.textfield.textfield import MDTextField
from kivy.properties import NumericProperty


class ComponentAddPairsOfAtoms(RelativeLayout):
    label_height = dp(20)
    spacing_padding = dp(0)
    radius = dp(20)
    width_of_line = dp(2)
    text_field_height = dp(0)
    grid_height = dp(0)
    widget = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.grid_height = self.label_height \
            + self.text_field_height + self.spacing_padding + 2 * dp(10)
            
    def add_row_of_text_input(self):
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
        
        print(self.ids.grid_with_atoms.height)
        print(self.grid_height)
        print("Add")
        self.ids.Button_x.md_bg_color = [0, 0, 1, 1]

        
