from Settings.globals import VERSION
from Settings.globals import OUTPUT_FILE_CODING


class StringTemplate:
    @staticmethod
    def get_report_header() -> str:
        return f"\n# pyMayCoor {VERSION}\n Character"\
            + f" encoding: {OUTPUT_FILE_CODING}\n\n"

    @staticmethod
    def get_histogram_header() -> str:
        return f"\n # Histograms \n\n"

    @staticmethod
    def get_coordination_numbers_header() -> str:
        return f"\n # Coordination numbers \n\n"

    @staticmethod
    def get_qi_units_header() -> str:
        return f"\n # Qⁱ numbers \n\n"

    @staticmethod
    def get_connections_header() -> str:
        return f"\n # Connections \n\n"

    @staticmethod
    def get_covalence_header() -> str:
        return f"\n # Covalence (valence) from Mayer bond orders \n\n"