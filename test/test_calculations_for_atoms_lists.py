import pytest
from pprint import pprint

from main.BondOrderProcessing.bond_order_processing.calculations\
    import Covalence

from main.BondOrderProcessing.bond_order_processing\
    .calculations_for_atoms_lists import _FromPairOfAtoms

from main.BondOrderProcessing.bond_order_processing.calculations\
    import PairOfAtoms


class Test_FromPairOfAtoms:

    def test__get_unique_atom_symbols(self):
        pairs_of_atoms = [PairOfAtoms("P", "O", 0.2, 2.0, "P-O"),
                          PairOfAtoms("Fe", "O", 0.2, 2.0, "Fe-O"),
                          PairOfAtoms("Al", "O", 0.2, 2.0, "Al-O"),
                          PairOfAtoms("Al", "Fe", 0.2, 2.0, "Al-Fe"),
                          PairOfAtoms("Fe", "P", 0.2, 2.0, "Fe-P")]
        results = _FromPairOfAtoms._get_unique_atom_symbols(pairs_of_atoms)
        assert set(results) == {'P', 'O', 'Fe', 'Al'}
