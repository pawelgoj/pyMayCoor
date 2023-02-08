import pytest
from pprint import pprint

from main.BondOrderProcessing.bond_order_processing.calculations\
    import Covalence

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import _FromPairOfAtoms

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import PairOfAtoms

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import CoordinationNumbersFromPairOfAtoms

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import ConnectionsFromPairOfAtoms

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import HistogramsFromPairOfAtoms

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import BondLengthFromPairOfAtoms

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import CovalenceFromPairOfAtoms

from main.BondOrderProcessing.bond_order_processing.calculations\
    import PairOfAtoms

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import QiUnitsFromPairOfAtoms


from .mocks import MayerBondOrders

pairs_of_atoms = [PairOfAtoms("P", "O", 0.2, 2.0, "P-O"),
                  PairOfAtoms("P", "O", 0.2, 2.0, "P=O"),
                  PairOfAtoms("Fe", "O", 0.2, 2.0, "Fe-O"),
                  PairOfAtoms("Al", "O", 0.2, 2.0, "Al-O"),
                  PairOfAtoms("Al", "Fe", 0.2, 2.0, "Al-Fe"),
                  PairOfAtoms("Fe", "P", 1, 2.0, "Fe-P")]


class Test_FromPairOfAtoms:

    def test__get_unique_atom_symbols(self):
        results = _FromPairOfAtoms._get_unique_atom_symbols(pairs_of_atoms)
        assert set(results) == {'P', 'O', 'Fe', 'Al'}


class TestHistogramsFromPairOfAtoms:
    def test_calculate(self):
        mbos = MayerBondOrders()

        result = HistogramsFromPairOfAtoms.calculate(pairs_of_atoms, mbos, 4)
        histogram = result.histograms['P-O']

        assert len(result.histograms) == 6 and \
            result.histograms['P-O'].y == [4, 2, 2, 2]

    def test_remove_duplicates(self):
        mbos = MayerBondOrders()

        result = HistogramsFromPairOfAtoms.calculate(pairs_of_atoms, mbos, 4)\
            .remove_duplicates()

        assert 'P=O' not in result._atoms_names.keys()

    def test_to_string(self):
        mbos = MayerBondOrders()

        string = HistogramsFromPairOfAtoms.calculate(pairs_of_atoms, mbos, 4)\
            .to_string()
        assert "Atom_1_id: P, atom_2_id: O)" in string\
            and "Atom_1_id: Fe, atom_2_id: O" in string\
            and "Atom_1_id: Al, atom_2_id: O" in string\
            and "Atom_1_id: Al, atom_2_id: Fe" in string\
            and "Atom_1_id: Fe, atom_2_id: P" in string


class TestCoordinationNumbersFromPairOfAtoms:
    def test_calculate(self):
        mbos = MayerBondOrders()
        result = CoordinationNumbersFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos)

        assert 'P-O' in result.coordination_numbers.keys()\
            and 'Fe-O' in result.coordination_numbers.keys()\
            and 'Al-O' in result.coordination_numbers.keys()\
            and 'Al-Fe' in result.coordination_numbers.keys()\
            and 'Fe-P' in result.coordination_numbers.keys()

    def test_calculate_statistics(self):
        mbos = MayerBondOrders()
        result = CoordinationNumbersFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos).calculate_statistics()

        assert result.coordination_numbers['P-O'].statistics[1]\
            == pytest.approx(66.6, 0.1) and\
            result.coordination_numbers['P-O'].statistics[2]\
            == pytest.approx(33.3, 0.1)

    def test_to_string(self):
        mbos = MayerBondOrders()
        string = CoordinationNumbersFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos).calculate_statistics().to_string()

        assert 'P-O' in string\
            and 'Fe-O' in string\
            and 'Al-O' in string\
            and 'Al-Fe' in string\
            and 'Fe-P' in string


class TestConnectionsFromPairOfAtoms:
    def test_calculate(self):
        mbos = MayerBondOrders()
        result = ConnectionsFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos)

        assert 'P-O' in result.connections.keys()\
            and 'Fe-O' in result.connections.keys()\
            and 'Al-O' in result.connections.keys()\
            and 'Al-Fe' in result.connections.keys()\
            and 'Fe-P' in result.connections.keys()

    def test_to_string(self):
        mbos = MayerBondOrders()
        string = ConnectionsFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos, ).to_string()

        assert 'P-O' in string\
            and 'Fe-O' in string\
            and 'Al-O' in string\
            and 'Al-Fe' in string\
            and 'Fe-P' in string


class TestBondLengthFromPairOfAtoms:
    @staticmethod
    def prepare_objects(path_to_input_file):
        from main.BondOrderProcessing.bond_order_processing.input_data\
            import InputDataFromCPMD
        from main.BondOrderProcessing.bond_order_processing.input_data\
            import LoadedData

        input_data = InputDataFromCPMD()
        input_data.load_input_data(path_to_input_file,
                                   LoadedData.UnitCell,
                                   LoadedData.CoordinatesOfAtoms,
                                   LoadedData.MayerBondOrders)

        unit_cell = input_data.return_data(LoadedData.UnitCell)
        coordinates_of_atoms = input_data.return_data(
            LoadedData.CoordinatesOfAtoms)

        mayer_bond_orders = input_data.return_data(
            LoadedData.MayerBondOrders)

        coordinates_of_atoms.convert_stored_coordinates_to_angstroms()
        unit_cell.convert_cell_data_to_angstroms()
        coordinates_of_atoms.add_unit_cell(unit_cell)

        return pairs_of_atoms,  mayer_bond_orders, coordinates_of_atoms

    @pytest.mark.usefixtures("path_to_input_file")
    @pytest.mark.slow
    def test_calculate(self, path_to_input_file):
        pairs_of_atoms,  mayer_bond_orders, coordinates_of_atoms =\
            TestBondLengthFromPairOfAtoms.prepare_objects(path_to_input_file)
        result = BondLengthFromPairOfAtoms.calculate(
            pairs_of_atoms,  mayer_bond_orders, coordinates_of_atoms)

        assert 'P-O' in result.bond_lengths.keys()\
            and 'Fe-O' in result.bond_lengths.keys()\
            and 'Al-O' in result.bond_lengths.keys()\
            and 'Al-Fe' in result.bond_lengths.keys()\
            and 'Fe-P' in result.bond_lengths.keys()

    @pytest.mark.usefixtures("path_to_input_file")
    @pytest.mark.slow
    def test_to_string(self, path_to_input_file):
        pairs_of_atoms,  mayer_bond_orders, coordinates_of_atoms =\
            TestBondLengthFromPairOfAtoms.prepare_objects(path_to_input_file)
        string = BondLengthFromPairOfAtoms.calculate(
            pairs_of_atoms,  mayer_bond_orders, coordinates_of_atoms
        ).to_string()
        assert 'P-O' in string\
            and 'Fe-O' in string\
            and 'Al-O' in string\
            and 'Al-Fe' in string\
            and 'Fe-P' in string


class TestCovalenceFromPairOfAtoms:
    def test_calculate(self):
        mbos = MayerBondOrders()
        result = CovalenceFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos)

        assert 'P' in result.covalence.keys()\
            and 'Fe' in result.covalence.keys()\
            and 'Al' in result.covalence.keys()\
            and 'O' in result.covalence.keys()

    def test_to_string(self):
        mbos = MayerBondOrders()
        string = CovalenceFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos, ).to_string()

        assert 'P' in string\
            and 'Fe' in string\
            and 'Al' in string\
            and 'O' in string


class TestQiUnitsFromPairOfAtoms:
    def test_calculate(self):
        mbos = MayerBondOrders()
        result = QiUnitsFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos)

        assert 'P-O' in result.qi_units.keys()\
            and 'Fe-O' in result.qi_units.keys()\
            and 'Al-O' in result.qi_units.keys()\
            and 'Al-Fe' in result.qi_units.keys()\
            and 'Fe-P' in result.qi_units.keys()

    def test_calculate_statistics(self):
        mbos = MayerBondOrders()
        result = QiUnitsFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos).calculate_statistics()

        assert 1 in result.qi_units['P-O'].statistics.keys()

    def test_to_string(self):
        mbos = MayerBondOrders()
        string = QiUnitsFromPairOfAtoms.calculate(
            pairs_of_atoms, mbos, ).calculate_statistics().to_string()
        assert 'P' in string\
            and 'Fe' in string\
            and 'Al' in string\
            and 'O' in string
