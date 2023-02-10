import yaml
from OutputStringTemplate.template import StringTemplate
from Settings.settings import Settings
from BondOrderProcessing.bond_order_processing\
    import calculations_for_atoms_lists, input_data
from BondOrderProcessing.bond_order_processing.calculations\
    import PairOfAtoms


def check_atoms_symbols_in_loaded_data(mayer_bond_orders, pairs_atoms_list)\
        -> list[str]:

    wrong_atoms_list = []
    for item in pairs_atoms_list:
        if not mayer_bond_orders.check_atom_symbol_in_MBO(item.atom_1):
            wrong_atoms_list.append(item.atom_1)
        if not mayer_bond_orders.check_atom_symbol_in_MBO(item.atom_2):
            wrong_atoms_list.append(item.atom_2)

    return wrong_atoms_list


def remove_wrong_atoms(wrong_atoms_list: list[str],
                       pairs_atoms_list: list[PairOfAtoms])\
        -> list[PairOfAtoms]:

    new = []
    for item in pairs_atoms_list:
        if item.atom_1 in wrong_atoms_list:
            continue
        elif item.atom_2 in wrong_atoms_list:
            continue
        else:
            new.append(item)

    return new


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

    wrong_atoms_names = check_atoms_symbols_in_loaded_data(mayer_bond_orders,
                                                           settings.pairs_atoms_list)

    pairs_atoms_list = remove_wrong_atoms(wrong_atoms_names,
                                          settings.pairs_atoms_list)

    output_string = StringTemplate.get_report_header()
    output_string += StringTemplate.get_wrong_atoms_list(wrong_atoms_names)
    if settings.histogram['calc'] is True:
        output_string += StringTemplate.get_histogram_header()
        output_string += calculations_for_atoms_lists\
            .HistogramsFromPairOfAtoms.calculate(pairs_atoms_list,
                                                 mayer_bond_orders,
                                                 settings.histogram['nr_bars'])\
            .to_string()

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
    if settings.calculations['bond_length'] is True:
        output_string += StringTemplate.get_bond_length()
        output_string += calculations_for_atoms_lists\
            .BondLengthFromPairOfAtoms.calculate(pairs_atoms_list,
                                                 mayer_bond_orders,
                                                 coordinates_of_atoms)\
            .to_string()

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

    with open(output_file_path, 'w', encoding="utf-8") as file:
        file.write(output_string)
