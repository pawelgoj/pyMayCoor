
from kivymd.color_definitions import colors
from kivy.utils import platform
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivy.config import Config
from kivy.properties import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from back_end_for_kivy import MenagerAppBackEnd
from back_end_for_kivy import NoDataAndSettingsError
from NavBar import navBar
from ComponentAddPairsOfAtoms import componentAddPairsOfAtoms
from mytextInput import mytextInput
from ComponentChoseCalculations import componentChoseCalculations
from switchButton import switchButton
from NavBar.navBar import NavBar
from app_back_end import AppBackEnd


# remove red dots on right mouse click (multitouch emulation)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')


class MainFrameOfApp(MDFloatLayout):

    previous_state_of_thread: int
    progress_bar_value: int
    dialog = None
    on_wrong_histogram_input: bool = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 0.25)
        self.previous_state_of_thread = 0
        self.progress_bar_value = 0

    def update(self, dt):
        try:
            if not MenagerAppBackEnd.queue.empty():
                val = MenagerAppBackEnd.queue.get()
                self._update_progress_bar(val[1])

                if val[0] is True:
                    MenagerAppBackEnd.end_of_process()
                    MenagerAppBackEnd.add_string_output(val[2])
                    dialog_text = "Calculations completed!!!"
                    self._show_dialog(dialog_text, 'ok')
        except AttributeError:
            pass

    def _show_dialog(self, dialog_text, button_text):
        if not self.dialog:
            self.dialog = MDDialog(
                text=dialog_text,
                buttons=[
                    MDFlatButton(
                        text=button_text,
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

    def _update_progress_bar(self, value: int):

        if value == 100:
            self.ids.progress_bar.value = value
            self.ids.label_for_progrss_bar.text = "Done!"
            self.progress_bar_value = 0
        elif value != self.previous_state_of_thread:
            self.progress_bar_value += 12
            self.previous_state_of_thread = value
            self.ids.progress_bar.value = self.progress_bar_value

    def change_state_histogram_button(self, widget):
        if widget.active:
            MenagerAppBackEnd.change_settings_item(
                'histogram_bool', True)
        else:
            MenagerAppBackEnd.change_settings_item(
                'histogram_bool', False)

    def change_state_bars_input_histogram(self, widget):
        if widget.text != '':
            try:
                MenagerAppBackEnd.change_settings_item(
                    'histogram_bar', int(widget.text))
            except ValueError:
                if not self.on_wrong_histogram_input:
                    dialog_text = 'Bars must have int value!'
                    self._show_dialog(dialog_text, 'ok')
                    self.on_wrong_histogram_input = True
        else:
            self.on_wrong_histogram_input = False
            MenagerAppBackEnd.change_settings_item(
                'histogram_bar', None)


class pyMayCoorApp(MDApp):

    text_input: str = None
    hover_color: tuple[float, float, float, float] = None

    def build(self):
        self.icon = "logo.png"
        self.theme_cls.material_style = "M2"

    def on_start(self):
        # chose theme of app it must be in app object not in mainWidget
        temp = self.theme_cls.colors
        temp["Dark"] = {
            "StatusBar": "E0E0E0",
            "AppBar": "#202020",
            "Background": "#252628",
            "CardsDialogs": "#FFFFFF",
            "FlatButtonDown": "#CCCCCC",
        }

        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.primary_dark_hue = "600"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.hover_color = (0.63, 0.56, 0.76, 1)

    def switch_theme_style(self):
        if self.text_input != None:
            # This statement is because strange preserved of MDtextInput
            # Focused MDtextInput not correct change Theme
            try:
                self.text_input.focus = True
            except:
                # If ocurred: ReferenceError: weakly-referenced object no longer exists
                self.text_input = None

        self.theme_cls.primary_palette = (
            "DeepOrange" if self.theme_cls.primary_palette == "DeepPurple" else "DeepPurple"
        )

        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.hover_color = (1, 0.57, 0.43, 1)
        else:
            self.theme_cls.theme_style = "Light"
            self.theme_cls.hover_color = (0.63, 0.56, 0.76, 1)

        if self.text_input != None:
            try:
                self.text_input.focus = False
            except:
                self.text_input = None

    def change_state(self, widget):
        self.text_input = widget


def run_app():
    global myApp
    myApp = pyMayCoorApp()
    myApp.run()
