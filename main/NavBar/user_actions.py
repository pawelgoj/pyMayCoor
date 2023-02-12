from plyer import filechooser
from back_end_for_kivy import MenagerAppBackEnd
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


def on_touch_up_find_input_file(self):
    path = filechooser.open_file(title="Pick a CPMD file..")
    if path != []:
        MenagerAppBackEnd.update_input_data(path[0])

    # remember to delete print !!!
    # TODO
    # Add comunicat to user!!!
    print(path)


def on_touch_up_save_settings(self):
    path = filechooser.save_file(title="save file..",
                                 filters=[("*.yaml"), ("*.yml")])

    # TODO
    # remember to delete print !!!
    print(path)


def on_touch_up_load_settings(self):
    path = filechooser.open_file(title="Pick a settings file..",
                                 filters=[("*.yaml"), ("*.yml")])

    if path != []:
        MenagerAppBackEnd.update_settings(path[0])
    # TODO
    # User must be informad that data was loaded!!!!
    # remember to delete print !!!
    print(path)


def on_touch_up_chose_export_file(self):
    path = filechooser.save_file(title="save file..")
    if path != []:
        MenagerAppBackEnd.export_data(path[0])
    # self.app_back_end.save_output(path)
    # remember to delete print !!!
    print(path)


def on_touch_up_run_program(self):
    try:
        MenagerAppBackEnd.perform_calculations()
        button_text = "ok"
        dialog_text = "Calculations completed."
    except AttributeError:
        button_text = "ok"
        dialog_text = "To perform calculations you must load correct"\
            + " input data."

    self.dialog = MDDialog(
        text=dialog_text,
        buttons=[
            MDFlatButton(
                text=button_text,
                theme_text_color="Custom",
                text_color=self.theme_cls.primary_color,
                on_press=remove_dialog
            ),
        ],
    )
    # on_press=remove_dialog(self)
    self.dialog.open()
    print(self)
    # remember to delete print !!!
    print("Calculations done!!!!!")


def remove_dialog(self):
    self.parent.parent.parent.parent.parent.remove_widget(
        self.parent.parent.parent.parent)


def on_enters(self):
    self.md_bg_color = (1, 1, 1, 1)
