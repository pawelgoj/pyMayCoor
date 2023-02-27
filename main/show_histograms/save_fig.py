from kivymd.uix.floatlayout import MDFloatLayout
from plyer import filechooser
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from main_kivy import myApp

Builder.load_file("show_histograms/savefig.kv")

class SaveFig(MDFloatLayout):
    id_widget: StringProperty = StringProperty()
    dialog = None

    def on_cancel(self, widget):
        to_remove = widget.parent.parent.parent
        node = widget.parent.parent.parent.parent
        node.remove_widget(to_remove)
        node.parent.parent.parent.set_on_save(False)

    def on_ok(self, widget):
        to_remove = widget.parent.parent.parent
        try:
            width = float(to_remove.ids.save_fig_text_input_1.text)
            height = float(to_remove.ids.save_fig_text_input_2.text)
        except ValueError:
            width = None
            height = None

        if width is not None and height is not None:
            node = widget.parent.parent.parent.parent
            path = filechooser.save_file(title="save file..")
            if path != []:
                to_save = widget.parent.parent.parent.parent

                node.parent.parent.parent.save_fig(to_save.fig_id, path[0],
                                                   width, height)
            node.remove_widget(to_remove)
            node.parent.parent.parent.set_on_save(False)
        else:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Size must be number!",
                    buttons=[
                        MDFlatButton(
                            text='ok',
                            theme_text_color="Custom",
                            text_color=myApp.theme_cls.primary_color,
                            on_press=self.remove_dialog
                        ),
                    ],
                )
                self.dialog.open()

    def remove_dialog(self, widget):
        widget.parent.parent.parent.parent.parent.remove_widget(
            widget.parent.parent.parent.parent)
        self.dialog = None
