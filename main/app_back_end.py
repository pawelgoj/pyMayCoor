from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection
import yaml

from OutputStringTemplate.template import StringTemplate
from Settings.settings import Settings
from BondOrderProcessing.bond_order_processing\
    import calculations_for_atoms_lists, input_data
from BondOrderProcessing.bond_order_processing.calculations\
    import PairOfAtoms
from BondOrderProcessing.bond_order_processing.input_data\
    import CoordinatesOfAtoms, MayerBondOrders

from data_process_utils import check_atoms_symbols_in_loaded_data,\
    remove_wrong_atoms


class AppBackEnd:
    """App to run by cli interface.
    """
    settings_file_path: str
    input_file_path: str
    output_file_path: str
    _output_string: str

    def __init__(self, progress_bar: bool):

        self.progress_bar = progress_bar

    def load_data(self, input_file_path: str) -> None:
        input_data_cpmd = input_data.InputDataFromCPMD()
        input_data_cpmd.load_input_data(input_file_path,
                                        input_data.LoadedData.UnitCell,
                                        input_data.LoadedData.MayerBondOrders,
                                        input_data.LoadedData.CoordinatesOfAtoms)

        unit_cell = input_data_cpmd.return_data(input_data.LoadedData.UnitCell)

        self.mayer_bond_orders = input_data_cpmd.return_data(
            input_data.LoadedData.MayerBondOrders)

        self.coordinates_of_atoms = input_data_cpmd.return_data(
            input_data.LoadedData.CoordinatesOfAtoms)

        self.coordinates_of_atoms.convert_stored_coordinates_to_angstroms()
        unit_cell.convert_cell_data_to_angstroms()
        self.coordinates_of_atoms.add_unit_cell(unit_cell)

    def load_settings(self, settings_file_path: str) -> None:
        with open(settings_file_path, 'r') as file:
            yaml_data = file.read()

        data = yaml.safe_load(yaml_data)
        self.settings = Settings(data)

    def calculate_only_histograms(self):
        # TODO
        pass

    def perform_calculations(self, pipeline_conn: Connection | None = None)\
            -> None:
        """Perform calculations."""
        # pipeline = [done=True | False, step_done = True | False]
        if self.progress_bar and pipeline_conn is None:
            raise Exception("To progress bar pipeline is required")
        elif pipeline_conn is not None:
            pipeline_conn.send((False, True))
            pipeline_conn.close()

        wrong_atoms_names = check_atoms_symbols_in_loaded_data(self.mayer_bond_orders,
                                                               self.settings.pairs_atoms_list)

        pairs_atoms_list = remove_wrong_atoms(wrong_atoms_names,
                                              self.settings.pairs_atoms_list)

        # Calculate and generate output data:
        output_string = StringTemplate.get_report_header()
        output_string += StringTemplate.get_wrong_atoms_list(
            wrong_atoms_names)

        conn_prent_1, conn_child_1 = Pipe()
        conn_prent_2, conn_child_2 = Pipe()

        p_1 = Process(target=self._thread_1, args=(
            conn_child_1, self.settings, pairs_atoms_list,
            self.mayer_bond_orders))

        p_2 = Process(target=self._thread_2, args=(
            conn_child_2, self.settings, pairs_atoms_list,
            self.mayer_bond_orders, self.coordinates_of_atoms))

        p_1.start()
        p_2.start()
        output_string += conn_prent_1.recv()
        output_string += conn_prent_2.recv()
        p_1.join()
        p_2.join()

        self._output_string = output_string

    @ staticmethod
    def _thread_1(conn: Connection, settings: Settings,
                  pairs_atoms_list: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders) -> None:
        if settings.histogram['calc'] is True:
            output_string = StringTemplate.get_histogram_header()
            output_string += calculations_for_atoms_lists\
                .HistogramsFromPairOfAtoms.calculate(pairs_atoms_list,
                                                     mayer_bond_orders,
                                                     settings.histogram['nr_bars'])\
                .to_string()
        else:
            output_string = ""

        if settings.calculations['q_i']['calc'] is True:
            output_string += StringTemplate.get_qi_units_header()
            pairs_atoms_list_tem = [item for item in pairs_atoms_list
                                    if item.id == settings.calculations['q_i']['bond_id']]

            output_string += calculations_for_atoms_lists\
                .QiUnitsFromPairOfAtoms.calculate(pairs_atoms_list_tem,
                                                  mayer_bond_orders)\
                . calculate_statistics().to_string()

        if settings.calculations['connections'] is True:
            output_string += StringTemplate.get_connections_header()
            output_string += calculations_for_atoms_lists\
                .ConnectionsFromPairOfAtoms.calculate(pairs_atoms_list,
                                                      mayer_bond_orders)\
                .to_string()

        conn.send(output_string)
        conn.close()

    @ staticmethod
    def _thread_2(conn: Connection, settings: Settings,
                  pairs_atoms_list: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders,
                  coordinates_of_atoms: CoordinatesOfAtoms) -> None:

        if settings.calculations['bond_length'] is True:
            output_string = StringTemplate.get_bond_length()
            output_string += calculations_for_atoms_lists\
                .BondLengthFromPairOfAtoms.calculate(pairs_atoms_list,
                                                     mayer_bond_orders,
                                                     coordinates_of_atoms)\
                .to_string()
        else:
            output_string = ""

        if settings.calculations['cn'] is True:
            output_string += StringTemplate.get_covalence_header()
            output_string += calculations_for_atoms_lists\
                .CoordinationNumbersFromPairOfAtoms.calculate(pairs_atoms_list,
                                                              mayer_bond_orders)\
                .calculate_statistics().to_string()

        if settings.calculations['covalence'] is True:
            output_string += StringTemplate.get_covalence_header()
            output_string += calculations_for_atoms_lists\
                .CovalenceFromPairOfAtoms.calculate(pairs_atoms_list,
                                                    mayer_bond_orders)\
                .to_string()

        conn.send(output_string)
        conn.close()

    def get_output_string(self) -> str:
        if self._output_string is not None:
            return self._output_string
        else:
            raise Exception('No preformed calculations!!!!')

    def save_output(self, output_file_path: str):
        """Save output data to file."""
        if self._output_string is not None:
            with open(output_file_path, 'w', encoding="utf-8") as file:
                file.write(self._output_string)
        else:
            raise Exception('No preformed calculations!!!!')
