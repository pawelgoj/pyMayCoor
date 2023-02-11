import pytest
from main.BondOrderProcessing.bond_order_processing.input_data\
    import InputDataFromCPMD
from main.BondOrderProcessing.bond_order_processing.input_data\
    import MayerBondOrders


class TestInputDataFromCPMD:
    @pytest.mark.parametrize('id,response',
                             [(0, (None, None, None)),
                              (1, (('P', 1.663), ('P', 1.872), ('P', 3.636))),
                              (253, (('O', -0.456), ('O', -0.537), ('O', 1.781))),
                              (254, (None, None, None))])
    @pytest.mark.usefixtures("path_to_input_file")
    def test_load_populations(self, path_to_input_file, id,
                              response):
        with open(path_to_input_file, "r") as file:
            data = file.read()

        input_data = InputDataFromCPMD()
        populations = input_data._load_populations(data)
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
    def test_load_coordinates_of_atoms(self, path_to_input_file,
                                       id, response):
        with open(path_to_input_file, "r") as file:
            data = file.read()

        input_data = InputDataFromCPMD()
        atom_coordinates = input_data._load_coordinates_of_atoms(
            data)
        coordinates = atom_coordinates.get_atom_coordinates(id)
        atom_name = atom_coordinates.get_atom_symbol(id)

        assert coordinates == response[1] and atom_name == response[0]

    @pytest.mark.usefixtures("path_to_input_file")
    def test_load_mayer_bond_orders(self, path_to_input_file):
        with open(path_to_input_file, "r") as file:
            data = file.read()

        input_data = InputDataFromCPMD()
        mayer_bond_order = input_data._load_mayer_bond_orders(data)
        value = mayer_bond_order.get_mayer_bond_order_between_atoms(12, 16)
        symbols = mayer_bond_order.get_atom_symbols(12, 16)
        assert value == 0.015 and symbols == ('P', 'P')

    @pytest.mark.usefixtures("path_to_input_file")
    def test_load_unit_cell(self, path_to_input_file):
        with open(path_to_input_file, "r") as file:
            data = file.read()

        input_data = InputDataFromCPMD()
        unit_cell = input_data._load_unit_cell(data)
        assert unit_cell.lattice_vectors == ([28.7812, 0.0, 0.0],
                                             [0.0, 28.7812, 0.0],
                                             [0.0, 0.0, 28.7812])

    @pytest.mark.usefixtures("path_to_input_file")
    def test_load_input_data(self, path_to_input_file):

        input_data = InputDataFromCPMD()

        from main.BondOrderProcessing.bond_order_processing.input_data\
            import LoadedData

        input_data.load_input_data(path_to_input_file,
                                   LoadedData.UnitCell,
                                   LoadedData.MayerBondOrders,
                                   LoadedData.Populations,
                                   LoadedData.CoordinatesOfAtoms)

        assert (input_data.unit_cell.lattice_vectors == ([28.7812, 0.0, 0.0],
                [0.0, 28.7812, 0.0], [0.0, 0.0, 28.7812])
                and
                input_data.mayer_bond_orders.get_mayer_bond_order_between_atoms(
                    12, 16)
                == 0.015
                and
                input_data.populations.lodwin.get(1) != None
                and
                input_data.coordinates_of_atoms.get_atom_coordinates(1)
                == (1.9950, 13.2541, 3.2454))

    @pytest.mark.usefixtures("input_data_object_with_loaded_data")
    def test_return_data(self, input_data_object_with_loaded_data):
        from main.BondOrderProcessing.bond_order_processing.input_data\
            import LoadedData

        input_data = input_data_object_with_loaded_data
        mayer_bond_orders = input_data.return_data(LoadedData.MayerBondOrders)
        value = mayer_bond_orders.get_mayer_bond_order_between_atoms(12, 16)
        assert value == 0.015


class TestMayerBondOrders:
    # Given
    test_data = [
        [0, 2, 3, 2],
        [2, 0, 1, 2],
        [3, 1, 0, 1],
        [2, 2, 1, 0]
    ]
    atom_id = [1, 2, 3, 4]
    horizontal_atom_symbol = {1: "Fe", 2: "Fe",
                              3: "O", 4: "O"}
    vertical_atom_symbol = {1: "Fe", 2: "Fe",
                            3: "O", 4: "O"}

    @pytest.mark.parametrize('symbol, result',
                             [('Fe', True),
                              ('X', False)])
    def test_check_atom_symbol_in_MBO(self, symbol, result):
        # When
        mayer_bond_order = MayerBondOrders(self.test_data, self.atom_id,
                                           self.horizontal_atom_symbol,
                                           self.vertical_atom_symbol)
        response = mayer_bond_order\
            .check_atom_symbol_in_MBO(symbol)

        assert result == response

    def test_get_mayer_bond_orders_list_between_two_atoms(self):

        # When
        mayer_bond_order = MayerBondOrders(self.test_data, self.atom_id,
                                           self.horizontal_atom_symbol,
                                           self.vertical_atom_symbol)
        result = mayer_bond_order\
            .get_mayer_bond_orders_list_between_two_atoms("Fe", "O")
        # Then
        assert result == [3, 2, 1, 2]

    def test_get_atoms_ids(self):
        # When
        mayer_bond_order = MayerBondOrders(self.test_data, self.atom_id,
                                           self.horizontal_atom_symbol,
                                           self.vertical_atom_symbol)
        result = mayer_bond_order.get_atoms_ids('Fe')
        # Then
        assert set(result) == {1, 2}


class TestCoordinatesOfAtoms:
    @pytest.mark.usefixtures("path_to_input_file")
    def test_get_distance_between_atoms(self, path_to_input_file):
        input_data = InputDataFromCPMD()

        from main.BondOrderProcessing.bond_order_processing.input_data\
            import LoadedData

        input_data.load_input_data(path_to_input_file,
                                   LoadedData.UnitCell,
                                   LoadedData.CoordinatesOfAtoms)

        unit_cell = input_data.return_data(LoadedData.UnitCell)
        coordinates_of_atoms = input_data.return_data(
            LoadedData.CoordinatesOfAtoms)

        coordinates_of_atoms.convert_stored_coordinates_to_angstroms()
        unit_cell.convert_cell_data_to_angstroms()
        coordinates_of_atoms.add_unit_cell(unit_cell)

        results = []
        for i in range(1, 8, 2):
            for j in range(1, 8, 2):
                results.append(round(coordinates_of_atoms
                               .get_distance_between_atoms(i, j), 0))

        assert results == [0.0, 8.0, 5.0, 9.0, 8.0, 0.0, 8.0, 9.0, 5.0,
                           8.0, 0.0, 7.0, 9.0, 9.0, 7.0, 0.0]
