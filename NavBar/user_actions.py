from plyer import filechooser

def on_touch_up_find_input_file(self):
    path = filechooser.open_file(title="Pick a CPMD file..", 
                             filters=[("Comma-separated Values", "*.csv")])
    print(path)

def on_touch_up_save_settings(self):
    pass

def on_touch_up_load_settings(self):
    path = filechooser.open_file(title="Pick a settings file..", 
                             filters=[("Comma-separated Values", "*.csv")])
    print(path)

def on_touch_up_chose_output_file_directory(self):
    pass

def on_enters(self):
    self.md_bg_color = (1, 1, 1, 1)