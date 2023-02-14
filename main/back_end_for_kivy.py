from app_back_end import AppBackEnd
from multiprocessing import Process, Queue
from multiprocessing.connection import Connection
from copy import deepcopy

from Settings.settings import Settings


class NoBackEndError(Exception):

    def __init__(self, message: str = "No instance of AppBackEnd!!!"):
        self.message = message
        super().__init__(self.message)


class NoDataAndSettingsError(Exception):
    def __init__(self, message: str = "To perform calculations you must load"
                 + "correct input data and settings!"):
        self.message = message
        super().__init__(self.message)


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
        cls.input_data = False
        cls.settings = False

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
    def update_settings(cls, path: str):
        if cls.app_back_end is not None:
            cls.app_back_end.load_settings(path)
            cls.settings = True
        else:
            raise NoBackEndError()

    @ classmethod
    def change_settings(cls, settings: Settings):
        if cls.app_back_end is not None:
            cls.app_back_end.settings = settings
        else:
            raise NoBackEndError()

    @ classmethod
    def change_settings_item(cls, key: str,
                             value: str | int | float | bool):
        if not cls.settings:
            cls.app_back_end.settings = Settings()

        if key == 'histogram_bool':
            cls.app_back_end.settings.histogram['calc'] = value
        elif key == 'histogram_bar':
            cls.app_back_end.settings.histogram['nr_bars'] = value

        elif key == 'q_i':
            cls.app_back_end.settings.calculations['q_i'] = value
        elif key == 'connections':
            cls.app_back_end.settings.calculations['connections'] = value
        elif key == 'bond_length':
            cls.app_back_end.settings.calculations['bond_length'] = value
        elif key == 'cn':
            cls.app_back_end.settings.calculations['cn'] = value
        elif key == 'covalence':
            cls.app_back_end.settings.calculations['covalence'] = value
        elif key == 'pair_of_atoms':
            cls.app_back_end.settings.pairs_atoms_list = value
            # TODO
            pass

    @ classmethod
    def get_settings(cls):
        settings = deepcopy(cls.app_back_end.settings)
        return settings
    
    @ classmethod
    def save_settings(cls, path):
        cls.app_back_end.settings.save_data(path)


    @ classmethod
    def update_input_data(cls, path: str):
        if cls.app_back_end is not None:
            cls.app_back_end.load_data(path)
            cls.input_data = True
        else:
            raise NoBackEndError()

    @ classmethod
    def perform_calculations(cls):
        if (cls.app_back_end is not None)\
                and cls.input_data and cls.settings:
            pipeline_conn = None
            cls.app_back_end.perform_calculations(pipeline_conn)
        else:
            raise NoDataAndSettingsError()

    @ classmethod
    def get_output_data(cls) -> str:
        if cls.app_back_end is not None:
            return cls.app_back_end.get_output_string()
        else:
            raise NoBackEndError()

    @ classmethod
    def export_data(cls, path):
        if cls.app_back_end is not None:
            cls.app_back_end.save_output(path)
        else:
            raise NoBackEndError()

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
    def thread_calculations(cls):
        if cls.input_data and cls.settings:
            app_back_end = deepcopy(cls.app_back_end)
            cls.p = Process(target=cls._thread,
                            args=(app_back_end, cls.queue,))
            cls.p.start()
        else:
            raise NoDataAndSettingsError()

    @ staticmethod
    def _thread(app_back_end, queue: Connection):
        app_back_end.perform_calculations(queue)

    @ classmethod
    def end_of_process(cls):
        cls.p.join()

    @ classmethod
    def add_string_output(cls, string: str):
        cls.app_back_end._output_string = string
