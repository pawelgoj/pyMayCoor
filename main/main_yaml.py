import yaml
from pprint import pprint

from Settings.settings import Settings
from BondOrderProcessing.bond_order_processing import calculations, input_data


def perform_calculations(settings_file_path: str, input_file_path: str)\
        -> None:
    """Perform calculations function

    Args:
        file_path (str): Path to file in ymal format with settings of calculations 
    """
    with open(settings_file_path, 'r') as file:
        yaml_data = file.read()

    with open(input_file_path, 'r') as file:
        input_file = file.read()

    data = yaml.safe_load(yaml_data)
    settings = Settings(data)

    # Reading data:
    input_data_cpmd = input_data.InputDataFromCPMD()
    input_data_cpmd.load_input_data(input_file)
    unit_cell = input_data_cpmd.return_data(input_data.LoadedData.UnitCell)

    mayer_bond_orders = input_data_cpmd.return_data(
        input_data.LoadedData.MayerBondOrders)

    coordinates_of_atoms = input_data_cpmd.return_data(
        input_data.LoadedData.CoordinatesOfAtoms)

    if settings.histogram['calc'] == True:
        calculations.Histogram.calculate()

    pprint(settings.histogram)

    # TODO

    pass
