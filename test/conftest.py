import pytest
from main.BondOrderProcessing.bond_order_processing.input_data\
    import InputDataFromCPMD
from main.BondOrderProcessing.bond_order_processing.input_data\
    import LoadedData
import os


@pytest.fixture()
def path_to_input_file(request):
    path_to_input_file = "egzamples_instructions/cpmd_out1.txt"

    yield path_to_input_file


@pytest.fixture()
def input_data_object_with_loaded_data(request):
    input_data = InputDataFromCPMD()
    path_to_input_file = "egzamples_instructions/cpmd_out1.txt"
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


def pytest_addoption(parser):
    parser.addoption("--python_command", action="store",
                     default="python",
                     help="Python command eg. python or py")


def pytest_generate_tests(metafunc):
    if "python_command" in metafunc.fixturenames:
        python_command = str(metafunc.config.getoption("--python_command"))
        metafunc.parametrize("python_command", [python_command])


@pytest.fixture()
def env_for_end_to_end_tests_2(request):
    file_name = "test_output.txt"
    yield file_name
    os.remove(f'./{file_name}')
    
@pytest.fixture()
def env_for_settings_tests(request):
    file_name = "test_output.yaml"
    yield file_name
    os.remove(f'./{file_name}')
