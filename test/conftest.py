import pytest



@pytest.fixture()
def path_to_input_file(request):
    path_to_input_file = "egzamples_instructions\out1.txt"

    yield path_to_input_file
