"""Calculations in this module are made for PairOfAtoms
objects lists. This module is added in version: 1.1.0"""

from .calculations import Calculations
from .calculations import Statistics
from .calculations import PairOfAtoms
from .calculations import Histogram
from .input_data import MayerBondOrders
from .input_data import CoordinatesOfAtoms


class _FromPairOfAtoms:
    @ staticmethod
    def _get_unique_atom_symbols(pair_of_atoms: list[PairOfAtoms])\
            -> list[str]:
        unique_symbols = []
        for item in pair_of_atoms:
            if item.atom_1 not in unique_symbols:
                unique_symbols.append(item.atom_1)
            if item.atom_2 not in unique_symbols:
                unique_symbols.append(item.atom_2)

        return unique_symbols


class HistogramsFromPairOfAtoms(Calculations, _FromPairOfAtoms):
    _Histogram: type = Histogram
    histograms: dict[str, Histogram]
    """**key** - bond_id, **value** - Histogram object"""

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders,
                  bins: int) -> type:
        self = cls()
        self.histograms = {}
        for item in pair_of_atoms:
            mbos = mayer_bond_orders\
                .get_mayer_bond_orders_list_between_two_atoms(
                    item.atom_1, item.atom_2)
            histogram = cls._Histogram.calculate(mbos, bins)
            self.histograms.update({item.id: histogram})
        return self

    def to_string(self) -> str:
        # TODO
        pass


class CoordinationNumbersFromPairOfAtoms(Calculations, Statistics):

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders) -> type:
        # TODO
        pass

    def calculate_statistics(self) -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass


class ConnectionsFromPairOfAtoms(Calculations):

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders) -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass


class BondLengthFromPairOfAtoms(Calculations):

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders,
                  coordinates_of_atoms: CoordinatesOfAtoms) -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass


class CovalenceFromPairOfAtoms(Calculations):

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders) -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass


class QiUnitsFromPairOfAtoms(Calculations, Statistics):

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders) -> type:
        # TODO
        pass

    def calculate_statistics(self) -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass
