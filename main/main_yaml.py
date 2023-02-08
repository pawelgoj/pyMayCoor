import yaml
from pprint import pprint
from OutputStringTemplate.template import StringTemplate
from Settings.settings import Settings
from BondOrderProcessing.bond_order_processing\
    import calculations_for_atoms_lists, input_data


def perform_calculations(settings_file_path: str, input_file_path: str,
                         output_file_path: str) -> None:
    """Perform calculations function

    Args:
        file_path (str): Path to file in ymal format with settings of calculations
    """
    with open(settings_file_path, 'r') as file:
        yaml_data = file.read()

    data = yaml.safe_load(yaml_data)
    settings = Settings(data)

    output_string = StringTemplate.get_report_header()

    # Reading data:
    input_data_cpmd = input_data.InputDataFromCPMD()
    input_data_cpmd.load_input_data(input_file_path,
                                    input_data.LoadedData.UnitCell,
                                    input_data.LoadedData.MayerBondOrders,
                                    input_data.LoadedData.CoordinatesOfAtoms)

    unit_cell = input_data_cpmd.return_data(input_data.LoadedData.UnitCell)

    mayer_bond_orders = input_data_cpmd.return_data(
        input_data.LoadedData.MayerBondOrders)

    coordinates_of_atoms = input_data_cpmd.return_data(
        input_data.LoadedData.CoordinatesOfAtoms)

    coordinates_of_atoms.convert_stored_coordinates_to_angstroms()
    unit_cell.convert_cell_data_to_angstroms()
    coordinates_of_atoms.add_unit_cell(unit_cell)

    if settings.histogram['calc'] is True:
        output_string += StringTemplate.get_histogram_header()
        output_string += calculations_for_atoms_lists\
            .HistogramsFromPairOfAtoms.calculate(settings.pairs_atoms_list,
                                                 mayer_bond_orders,
                                                 settings.histogram['nr_bars'])\
            .to_string()

    if settings.calculations['q_i']['calc'] is True:
        output_string += StringTemplate.get_qi_units_header()
        pairs_atoms_list = [item for item in settings.pairs_atoms_list
                            if item.id == settings.calculations['q_i']['bond_id']]

        output_string += calculations_for_atoms_lists\
            .QiUnitsFromPairOfAtoms.calculate(pairs_atoms_list,
                                              mayer_bond_orders)\
            .to_string()
    if settings.calculations['connections'] is True:
        output_string += StringTemplate.get_connections_header()
        output_string += calculations_for_atoms_lists\
            .ConnectionsFromPairOfAtoms.calculate(settings.pairs_atoms_list,
                                                  mayer_bond_orders)\
            .to_string()
    if settings.calculations['bond_length'] is True:
        output_string += StringTemplate.get_bond_length()
        output_string += calculations_for_atoms_lists\
            .BondLengthFromPairOfAtoms.calculate(settings.pairs_atoms_list,
                                                 mayer_bond_orders,
                                                 coordinates_of_atoms)\
            .to_string()

    if settings.calculations['cn'] is True:
        output_string += StringTemplate.get_covalence_header()
        output_string += calculations_for_atoms_lists\
            .CovalenceFromPairOfAtoms.calculate(settings.pairs_atoms_list,
                                                mayer_bond_orders)\
            .to_string()

    if settings.calculations['covalence'] is True:
        output_string += StringTemplate.get_covalence_header()
        output_string += calculations_for_atoms_lists\
            .CovalenceFromPairOfAtoms.calculate(settings.pairs_atoms_list,
                                                mayer_bond_orders)\
            .to_string()

    with open(output_file_path, 'w', encoding="utf-8") as file:
        file.write(output_string)
