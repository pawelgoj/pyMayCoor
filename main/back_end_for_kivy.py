from app_back_end import AppBackEnd


class NoBackEndError(Exception):

    def __init__(self, message: str = "No instance of AppBackEnd!!!"):
        self.message = message
        super().__init__(self.message)


class MenagerAppBackEnd:

    app_back_end: AppBackEnd | None = None

    @ classmethod
    def new_app_back_end(cls):
        cls.app_back_end = AppBackEnd()

    @ classmethod
    def check_is_instance(cls) -> bool:
        if cls.app_back_end is None:
            return False
        else:
            return True

    @ classmethod
    def get_app_back_end(cls) -> AppBackEnd:
        return cls.app_back_end

    @ classmethod
    def update_settings(cls, path: str):
        if cls.app_back_end is not None:
            cls.app_back_end.load_settings(path)
        else:
            raise NoBackEndError()

    @ classmethod
    def update_input_data(cls, path: str):
        if cls.app_back_end is not None:
            cls.app_back_end.load_data(path)
        else:
            raise NoBackEndError()

    @ classmethod
    def perform_calculations(cls):
        if cls.app_back_end is not None:
            cls.app_back_end.perform_calculations()
        else:
            raise NoBackEndError()

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
