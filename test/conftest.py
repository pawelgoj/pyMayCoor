import pytest
from main.BondOrderProcessing.bond_order_processing.input_data\
    import InputDataFromCPMD
from main.BondOrderProcessing.bond_order_processing.input_data\
    import LoadedData


@pytest.fixture()
def path_to_input_file(request):
    path_to_input_file = "egzamples_instructions/out1.txt"

    yield path_to_input_file


@pytest.fixture()
def input_data_object_with_loaded_data(request):
    input_data = InputDataFromCPMD()
    path_to_input_file = "egzamples_instructions/out1.txt"
    input_data.load_input_data(path_to_input_file,
                               LoadedData.UnitCell,
                               LoadedData.MayerBondOrders,
                               LoadedData.Populations,
                               LoadedData.CoordinatesOfAtoms)

    yield input_data


@pytest.fixture(scope="session")
def env_for_end_to_end_tests(tmp_path_factory):
    fn = tmp_path_factory.mktemp("data")

    return fn
