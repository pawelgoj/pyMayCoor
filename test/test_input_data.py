import pytest
from main.BondOrderCalculations.input_data import InputDataFromCPMD
import pprint


class TestInputDataFromCPMD:
    @pytest.mark.usefixtures("path_to_input_file")
    def test_return_populations_from_file(self, path_to_input_file):
        with open(path_to_input_file, "r") as file:
            data = file.read()

        row = InputDataFromCPMD._return_populations_from_file(data)

        print(row[2])
        assert True
