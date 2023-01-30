import pytest
from main.BondOrderCalculations.calculations import Histogram
from main.BondOrderCalculations.calculations import CoordinationNumbers

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
    """Mock class"""
    mbo = {1: {1: 0.5, 2: 0.5, 3: 0.4},
           2: {1: 0.5, 2: 0.1, 3: 0.05},
           3: {1: 0.5, 2: 0.1, 3: 0.05}}

    def get_mayer_bond_order_between_atoms(self, atom_id_1: int, atom_id_2:
                                           int) -> float:
        return self.mbo.get(atom_id_1).get(atom_id_2)

    def get_atoms_ids(self, atom_symbol_1):
        return [1, 2, 3]


class TestCoordinationNumbers:
    def test_calculate(self):

        mock_mayer_bond_orders = MayerBondOrders()

        result = CoordinationNumbers.calculate(mock_mayer_bond_orders,
                                               'P', 'O', 1.7, 0.2, 'P-O')

        value = result.list_coordinations_number

        values = []
        for item in value:
            values.append((item.id_atom_1, item.cn, item.bonds))

        print(result.to_string())
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
            .to_string()

        assert string == "CN of P bond: P-O\n\n"\
            + "id: 1 CN: 2\n"\
            + "Bond orders: 2 0.53 0.4\n"\
            + "id: 2 CN: 1\n"\
            + "Bond orders: 1 0.5\n"\
            + "id: 3 CN: 1\n"\
            + "Bond orders: 1 0.5\n\n"
