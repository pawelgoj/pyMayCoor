
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivy.config import Config
from kivy.properties import Clock, mainthread
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd_extensions.title_bar import MDTitleBar
from switchButton.switchButton import SwithButtonWidget
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.tab import MDTabs
from copy import deepcopy


from back_end_for_kivy import MenagerAppBackEnd
from back_end_for_kivy import NoDataAndSettingsError
from NavBar import navBar
from ComponentAddPairsOfAtoms import componentAddPairsOfAtoms
from mytextInput import mytextInput
from ComponentChoseCalculations import componentChoseCalculations
from switchButton import switchButton
from NavBar.navBar import NavBar
from report_viewer.report_viewer import ReportViewer


# remove red dots on right mouse click (multitouch emulation)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'multisamples', '3')
Config.set('graphics', 'vsync', '2')
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'custom_titlebar', '0')
# Config.set('graphics', 'min_state_time', '0.005')


class MyTabs(MDTabs):
    pass


class Tab(MDFloatLayout, MDTabsBase):
    pass


class MainFrameOfApp(MDFloatLayout):

    previous_state_of_thread: int
    progress_bar_value: int
    dialog = None
    on_wrong_histogram_input: bool = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 0.1)
        self.previous_state_of_thread = 0
        self.progress_bar_value = 0

    def update(self, dt):

        try:
            if not MenagerAppBackEnd.queue.empty():
                val = MenagerAppBackEnd.queue.get()
                self._update_progress_bar(val[1])

                if val[0] is True:
                    MenagerAppBackEnd.end_of_process()

                    dialog_text = "Calculations completed!!!"

                    if len(val[2]) == 2:
                        if val[2] != (None, None):

                            MenagerAppBackEnd.add_string_output(deepcopy(val[2][1]))

                            settings = MenagerAppBackEnd.get_settings()

                            bins = settings.histogram['nr_bars']

                            list_of_mbos = val[2][0]

                            for mbos in list_of_mbos:

                                self.ids.show_histograms.make_hists(
                                    mbos[0], mbos[1], bins)

                    else:
                        MenagerAppBackEnd.add_string_output(val[2])
                        self.ids.raport_viever.remove_report()
                        self.ids.raport_viever.show_report(
                            MenagerAppBackEnd.get_string_output())

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

    def calculate_histograms(self, widget):

        if MenagerAppBackEnd.check_thread_run():
            dialog_text = 'Calculations is running!'
            self._show_dialog(dialog_text, 'ok')
        else:
            MenagerAppBackEnd\
                .del_empty_added_pair_of_atom_objects()
            try:
                if MenagerAppBackEnd.check_settings_is_correct():
                    MenagerAppBackEnd\
                        .cast_values_pairs_of_atom_to_correct_values_for_calc()
                    MenagerAppBackEnd.make_queue()
                    MenagerAppBackEnd.calculate_histograms_thread()

                    self.ids.progress_bar\
                        .value = 0
                    self.ids.label_for_progrss_bar\
                        .text = "Work in progress..."

            except NoDataAndSettingsError:
                dialog_text = "To perform calculations you must load correct"\
                    + " input data!"
                self._show_dialog(dialog_text, 'ok')

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
                MenagerAppBackEnd.change_settings_item(
                    'histogram_bar', widget.text)
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
    hover_color: tuple[float, float, float, float] | None = None
    icon: str = "logo.png"
    progress_bar_color: tuple[float, float, float, float] | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.progress_bar_color = (0.1, 0.1, 0.1, 0.4)

    def build(self):
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
