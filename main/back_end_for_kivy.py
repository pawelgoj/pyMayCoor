from app_back_end import AppBackEnd
from multiprocessing import Process, Queue
from multiprocessing.connection import Connection
from copy import deepcopy


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
