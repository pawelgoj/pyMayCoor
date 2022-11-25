from plyer import filechooser

def on_touch_up_find_input_file(self):
    path = filechooser.open_file(title="Pick a CPMD file..")
    print(path)

def on_touch_up_save_settings(self):
    path = filechooser.save_file(title="save file..", 
                          filters=[("*.yaml"), ("*.yml")])
    print(path)
def on_touch_up_load_settings(self):
    path = filechooser.open_file(title="Pick a settings file..", 
                             filters=[("*.yaml"), ("*.yml")])
    print(path)

def on_touch_up_chose_export_file(self):
    path = filechooser.save_file(title="save file..")
    print(path)
    
def on_enters(self):
    self.md_bg_color = (1, 1, 1, 1)