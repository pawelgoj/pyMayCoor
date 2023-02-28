from copy import deepcopy
from plyer import filechooser
from back_end_for_kivy import MenagerAppBackEnd
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from back_end_for_kivy import NoDataAndSettingsError


def on_touch_up_find_input_file(self):
    path = filechooser.open_file(title="Pick a CPMD file..")
    if path != []:
        try:
            MenagerAppBackEnd.update_input_data(path[0])
        except Exception:
            self.dialog = MDDialog(
                text='Wrong input file!!!!',
                buttons=[
                    MDFlatButton(
                        text='ok',
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=remove_dialog
                    ),
                ],
            )
            self.dialog.open()


def on_touch_up_save_settings(self):

    MenagerAppBackEnd\
        .del_empty_added_pair_of_atom_objects()

    if MenagerAppBackEnd.check_settings_are_correct():
        MenagerAppBackEnd.cast_values_pairs_of_atom_to_correct_values_for_calc()
        path = filechooser.save_file(title="save file..",
                                     filters=[("*.yaml"), ("*.yml")])
        if path != []:
            MenagerAppBackEnd.save_settings(path[0])
    else:
        self.dialog = MDDialog(
            text='Settings data is wrong! Correct form.',
            buttons=[
                MDFlatButton(
                    text='ok',
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_press=remove_dialog
                ),
            ],
        )
        self.dialog.open()


def on_touch_up_load_settings(self):
    path = filechooser.open_file(title="Pick a settings file..",
                                 filters=[("*.yaml"), ("*.yml")])

    if path != []:

        previous_setting = deepcopy(MenagerAppBackEnd.app_back_end.settings)
        unreadable_file = False
        try:
            MenagerAppBackEnd.update_settings(path[0])
        except ValueError:
            unreadable_file = True

        if MenagerAppBackEnd.check_settings_are_correct()\
                and not unreadable_file:

            # Side effect: reset_rows also clear settings object!!!!
            self.get_root_window().children[0].ids\
                .add_pairs_atoms.reset_rows()
            MenagerAppBackEnd.update_settings(path[0])

            settings = MenagerAppBackEnd.get_settings()

            if settings.histogram['calc']:

                self.get_root_window().children[0].ids.histogram_nr_bars.text\
                    = str(settings.histogram['nr_bars'])

                self.get_root_window().children[0].ids\
                    .histogram_swith_button.active_button()
            else:
                if settings.histogram.get('nr_bars', None) is None:
                    self.get_root_window().children[0].ids.histogram_nr_bars.text\
                        = ''
                else:
                    self.get_root_window().children[0].ids.histogram_nr_bars.text\
                        = str(settings.histogram['nr_bars'])

                self.get_root_window().children[0].ids\
                    .histogram_swith_button.deactive_button()

            if settings.calculations['q_i']['calc']:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.q_i.active_button()
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.q_i_text.text\
                    = settings.calculations['q_i']['bond_id']
            else:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.q_i.deactive_button()

                if settings.calculations['q_i'].get('bond_id', None):
                    self.get_root_window().children[0].ids\
                        .chose_calculations.ids.q_i_text.text\
                        = ''
                else:
                    self.get_root_window().children[0].ids\
                        .chose_calculations.ids.q_i_text.text\
                        = '' if settings.calculations['q_i']['bond_id']\
                        is None else settings.calculations['q_i']['bond_id']

            if settings.calculations['connections']:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.coon.active_button()
            else:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.coon.deactive_button()

            if settings.calculations['bond_length']:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.length.active_button()
            else:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.length.deactive_button()

            if settings.calculations['cn']:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.coord.active_button()
            else:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.coord.deactive_button()

            if settings.calculations['covalence']:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.cov.active_button()
            else:
                self.get_root_window().children[0].ids\
                    .chose_calculations.ids.cov.deactive_button()

            nr_pairs_of_atoms = len(settings.pairs_atoms_list)

            self.get_root_window().children[0].ids\
                .add_pairs_atoms.add_rows(nr_pairs_of_atoms - 1)

            ids_list = self.get_root_window().children[0].ids\
                .add_pairs_atoms.ids_list

            i = 0
            for pair_of_atoms in settings.pairs_atoms_list:

                self.get_root_window().children[0].ids\
                    .add_pairs_atoms.add_content_to_text_input(
                    ids_list[0], i, str(pair_of_atoms.atom_1))
                self.get_root_window().children[0].ids\
                    .add_pairs_atoms.add_content_to_text_input(
                    ids_list[1], i, str(pair_of_atoms.atom_2))
                self.get_root_window().children[0].ids\
                    .add_pairs_atoms.add_content_to_text_input(
                    ids_list[2], i, str(pair_of_atoms.MBO_min))
                self.get_root_window().children[0].ids\
                    .add_pairs_atoms.add_content_to_text_input(
                    ids_list[3], i, str(pair_of_atoms.MBO_max))
                self.get_root_window().children[0].ids\
                    .add_pairs_atoms.add_content_to_text_input(
                    ids_list[4], i, str(pair_of_atoms.id))

                i += 1

        else:
            MenagerAppBackEnd.app_back_end.settings = previous_setting
            button_text = "ok"
            dialog_text = "Incorrect setting to load!"

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


def on_touch_up_chose_export_file(self):
    if MenagerAppBackEnd.check_string_output():
        path = filechooser.save_file(title="save file..")
        if path != []:
            MenagerAppBackEnd.export_data(path[0])
    else:
        button_text = "ok"
        dialog_text = "To export results, first perform the calculations!"

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


def on_touch_up_run_program(self):

    button_text = "ok"
    dialog_text = ''

    if MenagerAppBackEnd\
            .check_thread_run():
        dialog_text = 'Calculations is running!'
    else:

        MenagerAppBackEnd\
            .del_empty_added_pair_of_atom_objects()

        try:
            if not MenagerAppBackEnd.check_calculations_chosen():
                dialog_text = "Select what you want to calculate!"
            elif not MenagerAppBackEnd.check_pairs_of_atoms():
                dialog_text = "You must enter correct data for pairs of atoms!"
            elif not MenagerAppBackEnd.check_q_i_calculations_have_correct_id():
                dialog_text = "Bond id for Qi calculations not in pairs atoms list!"
            elif MenagerAppBackEnd.check_settings_are_correct():
                MenagerAppBackEnd\
                    .cast_values_pairs_of_atom_to_correct_values_for_calc()
                MenagerAppBackEnd.make_queue()
                MenagerAppBackEnd.thread_calculations()

                self.get_root_window().children[0].ids.progress_bar\
                    .value = 0
                self.get_root_window().children[0].ids.label_for_progrss_bar\
                    .text = "Work in progress..."
            else:
                dialog_text = "Wrong settings!"
        except NoDataAndSettingsError:
            dialog_text = "To perform calculations you must load correct"\
                + " input data!"

    if dialog_text != '':
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
