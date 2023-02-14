from app_back_end import AppBackEnd
from multiprocessing import Process, Queue
from multiprocessing.connection import Connection
from copy import deepcopy
from typing import Callable
from pprint import pprint

from Settings.settings import Settings
from BondOrderProcessing.bond_order_processing.calculations import PairOfAtoms


class NoBackEndError(Exception):

    def __init__(self, message: str = "No instance of AppBackEnd!!!"):
        self.message = message
        super().__init__(self.message)


class NoDataAndSettingsError(Exception):
    def __init__(self, message: str = "To perform calculations you must load"
                 + "correct input data and settings!"):
        self.message = message
        super().__init__(self.message)


def NoBackEndError_deco(callcable: Callable):
    def wrapper(cls, *args):
        if cls.app_back_end is not None:
            callcable(cls, *args)
        else:
            raise NoBackEndError()

    return wrapper


def NoDataAndSettingsError_deco(callcable: Callable):
    def wrapper(cls, *args):
        if (cls.app_back_end is not None)\
                and cls.input_data and cls.settings:
            callcable(cls, *args)
        else:
            raise NoDataAndSettingsError()

    return wrapper


class MenagerAppBackEnd:

    app_back_end: AppBackEnd
    queue: Connection
    conn_parent: Connection
    input_data: bool
    settings: bool
    string_output: str

    @ classmethod
    def make_queue(cls) -> Connection:
        cls.queue = Queue()

    @ classmethod
    def new_app_back_end(cls, progress_bar: bool = False):
        cls.app_back_end = AppBackEnd(progress_bar)
        cls.app_back_end.settings = Settings()
        cls.input_data = False
        cls.settings = True

    @ classmethod
    def check_is_instance(cls) -> bool:
        try:
            if cls.app_back_end is not None:
                return True
            else:
                return False

        except AttributeError:
            return False

    @ classmethod
    def get_app_back_end(cls) -> AppBackEnd:
        return cls.app_back_end

    @ classmethod
    def check_settings_is_correct(cls) -> bool:
        if cls.app_back_end.settings.histogram['calc']\
            and cls.app_back_end.settings\
                .histogram.get('nr_bars', None) is not None:
            hist_correct = True
        elif not cls.app_back_end.settings.histogram['calc']:
            hist_correct = True
        else:
            hist_correct = False

        if cls.app_back_end.settings.calculations['q_i']['calc']\
                and cls.app_back_end.settings\
                .calculations['q_i'].get('bond_id', None) is not None:

            if cls.app_back_end.settings\
                    .calculations['q_i'].get('bond_id', None) != '':
                qi_correct = True
            else:
                qi_correct = False
        elif not cls.app_back_end.settings.calculations['q_i']['calc']:
            qi_correct = True
        else:
            qi_correct = False

        if qi_correct and hist_correct:
            return True
        else:
            return False

        # TODO

    @ classmethod
    def check_correct_pairs_of_atoms(cls):
        checks = set()
        for item in cls.app_back_end.settings.pairs_atoms_list:
            try:
                value = float(item.MBO_min)
                result = True if value >= 0 else False
                checks.add(result)
            except (ValueError, TypeError):
                checks.add(False)
            try:
                value = float(item.MBO_max)
                result = True if value >= 0 else False
                checks.add(result)
            except (ValueError, TypeError):
                value = item.MBO_max
                value = value.strip()
                result = True if value == 'INF' else False
                checks.add(result)

        for true in checks:
            if not true:
                return False
        return True

    @ classmethod
    def cast_values_pairs_of_atom_to_correct_values_for_calc(cls):
        # TODO
        pass

    @ classmethod
    @ NoBackEndError_deco
    def update_settings(cls, path: str):
        cls.app_back_end.load_settings(path)
        cls.settings = True

    @ classmethod
    @ NoBackEndError_deco
    def change_settings(cls, settings: Settings):
        cls.app_back_end.settings = settings

    @ classmethod
    def change_settings_item(cls, key: str,
                             value: str | int | float | bool | None):
        if not cls.settings:
            cls.app_back_end.settings = Settings()

        length = len(cls.app_back_end.settings.pairs_atoms_list)

        if key == 'histogram_bool':
            cls.app_back_end.settings.histogram['calc'] = value
        elif key == 'histogram_bar':
            if value is not None:
                cls.app_back_end.settings.histogram['nr_bars'] = value
            else:
                try:
                    del cls.app_back_end.settings.histogram['nr_bars']
                except KeyError:
                    pass

        elif key == 'q_i_button':
            cls.app_back_end.settings.calculations['q_i']['calc'] = value
        elif key == 'q_i_bond_id':
            cls.app_back_end.settings.calculations['q_i']['bond_id'] = value
        elif key == 'connections':
            cls.app_back_end.settings.calculations['connections'] = value
        elif key == 'bond_length':
            cls.app_back_end.settings.calculations['bond_length'] = value
        elif key == 'cn':
            cls.app_back_end.settings.calculations['cn'] = value
        elif key == 'covalence':
            cls.app_back_end.settings.calculations['covalence'] = value

        elif 'atom_id_1_' in key:
            string = key.replace('atom_id_1_', '')
            nr = int(string)
            if nr < length:
                cls.app_back_end.settings.pairs_atoms_list[nr].atom_1 = value
            else:
                pair_of_atoms = PairOfAtoms()
                pair_of_atoms.atom_1 = value
                cls.app_back_end.settings.pairs_atoms_list.append(
                    pair_of_atoms)
        elif 'atom_id_2_' in key:
            string = key.replace('atom_id_2_', '')
            nr = int(string)
            if nr < length:
                cls.app_back_end.settings.pairs_atoms_list[nr].atom_2 = value
            else:
                pair_of_atoms = PairOfAtoms()
                pair_of_atoms.atom_2 = value
                cls.app_back_end.settings.pairs_atoms_list.append(
                    pair_of_atoms)
        elif 'min_mbo_' in key:
            string = key.replace('min_mbo_', '')
            nr = int(string)
            if nr < length:
                cls.app_back_end.settings.pairs_atoms_list[nr].MBO_min = value
            else:
                pair_of_atoms = PairOfAtoms()
                pair_of_atoms.MBO_min = value
                cls.app_back_end.settings.pairs_atoms_list.append(
                    pair_of_atoms)
        elif 'max_mbo_' in key:
            string = key.replace('max_mbo_', '')
            nr = int(string)
            if nr < length:
                cls.app_back_end.settings.pairs_atoms_list[nr].MBO_max = value
            else:
                pair_of_atoms = PairOfAtoms()
                pair_of_atoms.MBO_max = value
                cls.app_back_end.settings.pairs_atoms_list.append(
                    pair_of_atoms)
        elif 'bond_id_' in key:
            string = key.replace('bond_id_', '')

            nr = int(string)
            if nr < length:
                cls.app_back_end.settings.pairs_atoms_list[nr].id = value
            else:
                pair_of_atoms = PairOfAtoms()
                pair_of_atoms.id = value
                cls.app_back_end.settings.pairs_atoms_list.append(
                    pair_of_atoms)

    @ classmethod
    def get_settings(cls):
        settings = deepcopy(cls.app_back_end.settings)
        return settings

    @ classmethod
    @ NoBackEndError_deco
    def save_settings(cls, path):
        if cls.app_back_end.settings is None:
            cls.app_back_end.settings = Settings()
        cls.app_back_end.save_settings(path)

    @ classmethod
    @ NoBackEndError_deco
    def update_input_data(cls, path: str):
        cls.app_back_end.load_data(path)
        cls.input_data = True

    @ classmethod
    @ NoDataAndSettingsError_deco
    def perform_calculations(cls):

        pipeline_conn = None
        cls.app_back_end.perform_calculations(pipeline_conn)

    @ classmethod
    @ NoBackEndError_deco
    def get_output_data(cls) -> str:
        return cls.app_back_end.get_output_string()

    @ classmethod
    @ NoBackEndError_deco
    def export_data(cls, path):
        cls.app_back_end.save_output(path)

    @ classmethod
    def calculate_histograms(cls):
        # TODO
        pass

    @ classmethod
    def check_thread_run(cls):
        try:
            return cls.p.is_alive()
        except AttributeError:
            return False

    @ classmethod
    @ NoDataAndSettingsError_deco
    def thread_calculations(cls):

        app_back_end = deepcopy(cls.app_back_end)
        cls.p = Process(target=cls._thread,
                        args=(app_back_end, cls.queue,))
        cls.p.start()

    @ staticmethod
    def _thread(app_back_end, queue: Connection):
        app_back_end.perform_calculations(queue)

    @ classmethod
    def end_of_process(cls):
        cls.p.join()

    @ classmethod
    def add_string_output(cls, string: str):
        cls.app_back_end._output_string = string
