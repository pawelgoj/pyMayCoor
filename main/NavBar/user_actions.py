from plyer import filechooser
from back_end_for_kivy import MenagerAppBackEnd
from multiprocessing import Process, Pipe
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from back_end_for_kivy import NoDataAndSettingsError


def on_touch_up_find_input_file(self):
    path = filechooser.open_file(title="Pick a CPMD file..")
    if path != []:
        MenagerAppBackEnd.update_input_data(path[0])


def on_touch_up_save_settings(self):
    path = filechooser.save_file(title="save file..",
                                 filters=[("*.yaml"), ("*.yml")])
    # TODO

def on_touch_up_load_settings(self):
    path = filechooser.open_file(title="Pick a settings file..",
                                 filters=[("*.yaml"), ("*.yml")])

    if path != []:
        MenagerAppBackEnd.update_settings(path[0])


def on_touch_up_chose_export_file(self):
    path = filechooser.save_file(title="save file..")
    if path != []:
        MenagerAppBackEnd.export_data(path[0])


def on_touch_up_run_program(self):
    try:
        MenagerAppBackEnd.make_queue()
        MenagerAppBackEnd.thread_calculations()
        button_text = "ok"
        dialog_text = "Calculations completed."

        self.get_root_window().children[0].ids.progress_bar\
            .value = 0

    except NoDataAndSettingsError:
        button_text = "ok"
        dialog_text = "To perform calculations you must load correct"\
            + " input data and settings!."

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
        self.dialog.open()


def remove_dialog(self):
    self.parent.parent.parent.parent.parent.remove_widget(
        self.parent.parent.parent.parent)


def on_enters(self):
    self.md_bg_color = (1, 1, 1, 1)
