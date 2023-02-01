import pytest
from main.BondOrderCalculations.calculations import Histogram
from main.BondOrderCalculations.calculations import CoordinationNumbers
from main.BondOrderCalculations.calculations import QiUnits
from main.BondOrderCalculations.calculations import Connections
from main.BondOrderCalculations.calculations import Connection
from main.BondOrderCalculations.calculations import BondLength

from main.BondOrderCalculations.input_data import InputDataFromCPMD

from dataclasses import dataclass
from pprint import pprint


class TestHistogram:
    values = [2, 2.5, 3, 5, 6, 7, 6, 3, 3.75, 2.5]

    def test_calculate(self):

        result = Histogram.calculate(self.values, 3)
        assert (result.x == [2.8333333333333335, 4.5, 6.166666666666667]
                and result. y == [5, 2, 3])

    def test_to_string(self):

        string = Histogram.calculate(self.values, 3)\
            .to_string('P', 'O')

        assert string == ("P, O\n"
                          + "\n"
                          + "Interval/2 Count\n\n"
                          + "2.8333333333333335 5\n"
                          + "4.5 2\n"
                          + "6.166666666666667 3\n\n")


class MayerBondOrders:
    """Mock class."""
    mbo = {1: {1: 0.5, 2: 0.5, 3: 0.4},
           2: {1: 0.5, 2: 0.1, 3: 0.05},
           3: {1: 0.5, 2: 0.1, 3: 0.05}}

    def get_mayer_bond_order_between_atoms(self, atom_id_1: int, atom_id_2:
                                           int) -> float:
        return self.mbo.get(atom_id_1).get(atom_id_2)

    def get_atoms_ids(self, atom_symbol_1):
        return [1, 2, 3]


class TestCoordinationNumbers:
    @pytest.mark.parametrize('max_mbo', [1.7, 'INF'])
    def test_calculate(self, max_mbo):

        mock_mayer_bond_orders = MayerBondOrders()

        result = CoordinationNumbers.calculate(mock_mayer_bond_orders,
                                               'P', 'O', max_mbo, 0.2, 'P-O')

        value = result.list_coordinations_number

        values = []
        for item in value:
            values.append((item.id_atom_1, item.cn, item.bonds))

        assert (values == [(1, 2, {2: 0.5, 3: 0.4}),
                           (2, 1, {1: 0.5}),
                           (3, 1, {1: 0.5})]
                and result.id_of_bond == 'P-O'
                and result.atom_symbol == 'P'
                )

    def test_to_string(self):
        mock_mayer_bond_orders = MayerBondOrders()

        string = CoordinationNumbers.calculate(mock_mayer_bond_orders,
                                               'P', 'O', 1.7, 0.2, 'P-O')\
            .calculate_statistics()\
            .to_string()

        assert string == "CN of P bond: P-O\n\n"\
            + "id: 1 CN: 2\n"\
            + "Bond orders (id: mbo): 2: 0.5, 3: 0.4\n"\
            + "id: 2 CN: 1\n"\
            + "Bond orders (id: mbo): 1: 0.5\n"\
            + "id: 3 CN: 1\n"\
            + "Bond orders (id: mbo): 1: 0.5\n\n"\
            + "Statistics of: P\n\n"\
            + "CN %\n"\
            + "2 33.333\n"\
            + "1 66.667\n\n"

    def test__get_list_of_coordination_numbers(self):
        mock_mayer_bond_orders = MayerBondOrders()

        result = CoordinationNumbers.calculate(mock_mayer_bond_orders,
                                               'P', 'O', 1.7, 0.2, 'P-O')\
            ._get_list_of_coordination_numbers()

        assert result == [2, 1]

    def test_calculate_statistics(self):
        mock_mayer_bond_orders = MayerBondOrders()

        result = CoordinationNumbers.calculate(mock_mayer_bond_orders,
                                               'P', 'O', 1.7, 0.2, 'P-O')\
            .calculate_statistics()

        assert result.statistics == {2: pytest.approx(33.3, 0.1),
                                     1: pytest.approx(66.6, 0.1)}


class TestQiUnits:
    @pytest.mark.parametrize('max_mbo', [1.7, 'INF'])
    def test_calculate(self, max_mbo):
        mayer_bond_orders = MayerBondOrders()

        result = QiUnits.calculate(mayer_bond_orders,
                                   'P', 'O', max_mbo, 0.06, 'P-O')

        assert (result.q_i_units == {1: 3, 2: 2, 3: 2}
                and result.id_of_bond == 'P-O'
                and result.atom_symbol_1 == 'P'
                and result.atom_symbol_2 == 'O')

    def test_calculate_statistics(self):
        mayer_bond_orders = MayerBondOrders()

        result = QiUnits.calculate(mayer_bond_orders,
                                   'P', 'O', 1.7, 0.06, 'P-O')\
            .calculate_statistics()

        assert result.statistics == {2: pytest.approx(66.6, 0.1),
                                     3: pytest.approx(33.3, 0.1)}

    def test_to_string(self):
        mayer_bond_orders = MayerBondOrders()

        result = QiUnits.calculate(mayer_bond_orders,
                                   'P', 'O', 1.7, 0.06, 'P-O')\
            .calculate_statistics()\
            .to_string()

        assert result == "Q_i of P bond id: P-O\n\n"\
            + "id Q_i[i]\n"\
            + "1 3\n"\
            + "2 2\n"\
            + "3 2\n\n"\
            + "Statistics of Q_i: P, bond id: P-O\n\n"\
            + "Q_i[i] [%]\n"\
            + "3 33.333\n"\
            + "2 66.667\n\n"


@dataclass
class PairOfAtoms:
    """Mock of Pair of atoms"""

    atom_1: str
    atom_2: str
    MBO_min: float
    MBO_max: float | str
    id: str


class TestConnections:
    def test_calculate(self):
        list_of_pair_of_atoms = [
            PairOfAtoms('P', 'O', 0, 1.7, 'P-O'),
            PairOfAtoms('P', 'Fe', 0, 'INF', 'P-Fe'),
            PairOfAtoms('Fe', 'O', 0, 'INF', 'Fe-O')
        ]
        mayer_bond_orders = MayerBondOrders()
        result = Connections.calculate(mayer_bond_orders, 'P',
                                       list_of_pair_of_atoms)

        assert (result.atom_symbol_1 == "P"
                and result.connections == {1: [Connection(atom_symbol_2='O',
                                                          bond_id='P-O',
                                                          quantity=3,
                                                          bonds={1: 0.5,
                                                                 2: 0.5,
                                                                 3: 0.4}),
                                               Connection(atom_symbol_2='Fe',
                                                          bond_id='P-Fe',
                                                          quantity=3,
                                                          bonds={1: 0.5,
                                                                 2: 0.5,
                                                                 3: 0.4})],
                                           2: [Connection(atom_symbol_2='O',
                                                          bond_id='P-O',
                                                          quantity=3,
                                                          bonds={1: 0.5,
                                                                 2: 0.1,
                                                                 3: 0.05}),
                                               Connection(atom_symbol_2='Fe',
                                                          bond_id='P-Fe',
                                                          quantity=3,
                                                          bonds={1: 0.5,
                                                                 2: 0.1,
                                                                 3: 0.05})],
                                           3: [Connection(atom_symbol_2='O',
                                                          bond_id='P-O',
                                                          quantity=3,
                                                          bonds={1: 0.5,
                                                                 2: 0.1,
                                                                 3: 0.05}),
                                               Connection(atom_symbol_2='Fe',
                                                          bond_id='P-Fe',
                                                          quantity=3,
                                                          bonds={1: 0.5,
                                                                 2: 0.1,
                                                                 3: 0.05})]})

    def test_to_string(self):
        list_of_pair_of_atoms = [
            PairOfAtoms('P', 'O', 0, 1.7, 'P-O'),
            PairOfAtoms('P', 'Fe', 0, 'INF', 'P-Fe'),
            PairOfAtoms('Fe', 'O', 0, 'INF', 'Fe-O')
        ]
        mayer_bond_orders = MayerBondOrders()
        string = Connections.calculate(mayer_bond_orders, 'P',
                                       list_of_pair_of_atoms)\
            .to_string()

        assert string == "Connections of: P\n\n"\
            + "Central atom id: 1\n"\
            + "Bond id: P-O (second atom: O)\n"\
            + "quantity: 3\n"\
            + "Bonds:\n"\
            + "id: 1 2 3 \n"\
            + "mbo: 0.5 0.5 0.4 \n\n"\
            + "Bond id: P-Fe (second atom: Fe)\n"\
            + "quantity: 3\n"\
            + "Bonds:\n"\
            + "id: 1 2 3 \n"\
            + "mbo: 0.5 0.5 0.4 \n\n"\
            + "Central atom id: 2\n"\
            + "Bond id: P-O (second atom: O)\n"\
            + "quantity: 3\n"\
            + "Bonds:\n"\
            + "id: 1 2 3 \n"\
            + "mbo: 0.5 0.1 0.05 \n\n"\
            + "Bond id: P-Fe (second atom: Fe)\n"\
            + "quantity: 3\n"\
            + "Bonds:\n"\
            + "id: 1 2 3 \n"\
            + "mbo: 0.5 0.1 0.05 \n\n"\
            + "Central atom id: 3\n"\
            + "Bond id: P-O (second atom: O)\n"\
            + "quantity: 3\n"\
            + "Bonds:\n"\
            + "id: 1 2 3 \n"\
            + "mbo: 0.5 0.1 0.05 \n\n"\
            + "Bond id: P-Fe (second atom: Fe)\n"\
            + "quantity: 3\n"\
            + "Bonds:\n"\
            + "id: 1 2 3 \n"\
            + "mbo: 0.5 0.1 0.05 \n\n"\



class TestBondLength:

    @pytest.mark.usefixtures("path_to_input_file")
    def test_calculate(self, path_to_input_file):
        input_data = InputDataFromCPMD()

        from main.BondOrderCalculations.input_data import LoadedData

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

        result = BondLength.calculate(mayer_bond_orders,
                                      coordinates_of_atoms, 'P', 'O',
                                      1.7, 0.2, 'P-O')

        assert (len(result.lengths) == 56 and len(result.mbos) == 56
                and len(result.lengths[4]) == 4 and len(result.lengths[4]) == 4)
