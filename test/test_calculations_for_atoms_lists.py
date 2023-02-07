import pytest
from pprint import pprint

from main.BondOrderProcessing.bond_order_processing.calculations\
    import Covalence

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import _FromPairOfAtoms

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import HistogramsFromPairOfAtoms

from main.BondOrderProcessing.bond_order_processing.calculations\
    import PairOfAtoms
from .mocks import MayerBondOrders

pairs_of_atoms = [PairOfAtoms("P", "O", 0.2, 2.0, "P-O"),
                  PairOfAtoms("Fe", "O", 0.2, 2.0, "Fe-O"),
                  PairOfAtoms("Al", "O", 0.2, 2.0, "Al-O"),
                  PairOfAtoms("Al", "Fe", 0.2, 2.0, "Al-Fe"),
                  PairOfAtoms("Fe", "P", 0.2, 2.0, "Fe-P")]


class Test_FromPairOfAtoms:

    def test__get_unique_atom_symbols(self):
        results = _FromPairOfAtoms._get_unique_atom_symbols(pairs_of_atoms)
        assert set(results) == {'P', 'O', 'Fe', 'Al'}


class TestHistogramsFromPairOfAtoms:
    def test_calculate(self):
        mbos = MayerBondOrders()

        result = HistogramsFromPairOfAtoms.calculate(pairs_of_atoms, mbos, 4)
        histogram = result.histograms['P-O']

        assert len(result.histograms) == 5 and \
            result.histograms['P-O'].y == [4, 2, 2, 2]

    def test_to_string(self):
        mbos = MayerBondOrders()

        string = HistogramsFromPairOfAtoms.calculate(pairs_of_atoms, mbos, 4)\
            .to_string()

        assert "Bond_id: P-O (P, O)" in string\
            and "Bond_id: Fe-O (Fe, O)" in string\
            and "Bond_id: Al-O (Al, O)" in string\
            and "Bond_id: Al-Fe (Al, Fe)" in string\
            and "Bond_id: Fe-P (Fe, P)" in string