import pytest
from main.BondOrderCalculations.input_data import InputDataFromCPMD
from pprint import pprint


class TestInputDataFromCPMD:
    @pytest.mark.parametrize('id,response',
                             [(0, (None, None, None)),
                              (1, (('P', 1.663), ('P', 1.872), ('P', 3.636))),
                              (253, (('O', -0.456), ('O', -0.537), ('O', 1.781))),
                              (254, (None, None, None))])
    @pytest.mark.usefixtures("path_to_input_file")
    def test_load_populations_from_file(self, path_to_input_file, id,
                                          response):
        with open(path_to_input_file, "r") as file:
            data = file.read()

        input_data = InputDataFromCPMD()
        populations = input_data._load_populations_from_file(data)
        val_1 = populations.lodwin
        val_2 = populations.mulliken
        val_3 = populations.valence
        assert (val_1.get(id) == (response[0])
                and val_2.get(id) == (response[1])
                and val_3.get(id) == (response[2])
                )

    @pytest.mark.parametrize('id,response',
                             [(0, (None, None)),
                              (1, ('P', (1.9950, 13.2541, 3.2454))),
                              (253, ('O', (0.1590, 2.0245, 16.6981))),
                              (254, (None, None))])
    @pytest.mark.usefixtures("path_to_input_file")
    def test_load_coordinates_of_atoms_from_file(self, path_to_input_file,
                                                   id, response):
        with open(path_to_input_file, "r") as file:
            data = file.read()

        input_data = InputDataFromCPMD()
        atom_coordinates = input_data._load_coordinates_of_atoms_from_file(
            data)
        coordinates = atom_coordinates.get_atom_coordinates(id)
        atom_name = atom_coordinates.get_atom_symbol(id)
        
        assert coordinates == response[1] and atom_name == response[0]
        
