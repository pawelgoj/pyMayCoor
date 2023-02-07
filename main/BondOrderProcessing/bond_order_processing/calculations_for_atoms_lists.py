"""Calculations in this module are made for PairOfAtoms
objects lists. This module is added in version: 1.1.0"""

from .calculations import Calculations
from .calculations import Statistics
from .calculations import PairOfAtoms
from .calculations import Histogram
from .input_data import MayerBondOrders
from .input_data import CoordinatesOfAtoms
from .calculations import CoordinationNumbers
from .calculations import Connections
from .calculations import BondLength


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
    _atoms_names: dict[str, (str, str)]

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders,
                  bins: int) -> type:
        """Calculate HistogramsFromPairOfAtoms object.

        Args:
            pair_of_atoms (list[PairOfAtoms]): list of PairOfAtoms objects.
            mayer_bond_orders (MayerBondOrders): MayerBondOrders object.
            bins (int): Number of bins in histogram.

        Returns:
            **HistogramsFromPairOfAtoms**: HistogramsFromPairOfAtoms object
        """
        self = cls()
        self.histograms = {}
        self._atoms_names = {}
        for item in pair_of_atoms:
            mbos = mayer_bond_orders\
                .get_mayer_bond_orders_list_between_two_atoms(
                    item.atom_1, item.atom_2)
            self._atoms_names.update({item.id: (item.atom_1, item.atom_2)})
            histogram = cls._Histogram.calculate(mbos, bins)
            self.histograms.update({item.id: histogram})
        return self

    def to_string(self) -> str:
        """Make string from HistogramsFromPairOfAtoms object

        Returns:
            **str**: String
        """
        string = ""
        for key, histogram in self.histograms.items():
            string += histogram.to_string(key,  *self._atoms_names[key])

        return string


class CoordinationNumbersFromPairOfAtoms(Calculations, Statistics):
    _CoordinationNumbers: type = CoordinationNumbers
    coordination_numbers: list[str, CoordinationNumbers]
    """**key** - bond_id, **value** - CoordinationNumbers object"""
    _atoms_names: dict[str, (str, str)]

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders) -> type:
        """Calculate CoordinationNumbersFromPairOfAtoms object.

        Args:
            pair_of_atoms (list[PairOfAtoms]): list of PairOfAtoms objects.
            mayer_bond_orders (MayerBondOrders): MayerBondOrders object.

        Returns:
            **CoordinationNumbersFromPairOfAtoms**: CoordinationNumbersFromPairOfAtoms object.
        """
        self = cls()
        self.coordination_numbers = {}
        self._atoms_names = {}
        for item in pair_of_atoms:
            self._atoms_names.update({item.id: (item.atom_1, item.atom_2)})
            coordination = cls._CoordinationNumbers\
                .calculate(mayer_bond_orders,
                           item.atom_1, item.atom_2,
                           item.MBO_max, item.MBO_min,
                           item.id)
            self.coordination_numbers.update({item.id: coordination})
        return self

    def calculate_statistics(self) -> type:
        """Calculate statistic in **CoordinationNumbers** objects."""

        for keys in self.coordination_numbers.keys():
            self.coordination_numbers[keys].calculate_statistics()
        return self

    def to_string(self) -> str:
        """Make string from CoordinationNumbersFromPairOfAtoms object

        Returns:
            **str**: String
        """
        string = ""
        for coordination_numbers in self.coordination_numbers.values():
            string += coordination_numbers\
                .to_string()

        return string


class ConnectionsFromPairOfAtoms(Calculations):
    _Connections: type = Connections
    connections: dict[str, Histogram]
    """**key** - bond_id, **value** - Connections object"""
    _atoms_names: dict[str, (str, str)]

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders) -> type:
        """Calculate ConnectionsFromPairOfAtoms object.

        Args:
            pair_of_atoms (list[PairOfAtoms]): list of PairOfAtoms objects.
            mayer_bond_orders (MayerBondOrders): MayerBondOrders object.

        Returns:
            **ConnectionsFromPairOfAtoms**: ConnectionsFromPairOfAtoms object.
        """
        self = cls()
        self.connections = {}
        self._atoms_names = {}
        for item in pair_of_atoms:
            self._atoms_names.update({item.id: (item.atom_1, item.atom_2)})
            connections = cls._Connections\
                .calculate(mayer_bond_orders,
                           item.atom_1, pair_of_atoms)
            self.connections.update({item.id: connections})
        return self

    def to_string(self) -> str:
        """Make string from ConnectionsFromPairOfAtoms object

        Returns:
            **str**: String
        """
        string = ""
        for connections in self.connections.values():
            string += connections\
                .to_string()

        return string


class BondLengthFromPairOfAtoms(Calculations):
    _BondLength: type = BondLength
    bond_lengths: dict[str, Histogram]
    """**key** - bond_id, **value** - BondLength object"""
    _atoms_names: dict[str, (str, str)]

    @classmethod
    def calculate(cls, pair_of_atoms: list[PairOfAtoms],
                  mayer_bond_orders: MayerBondOrders,
                  coordinates_of_atoms: CoordinatesOfAtoms) -> type:
        self = cls()
        self.bond_lengths = {}
        self._atoms_names = {}
        for item in pair_of_atoms:
            self._atoms_names.update({item.id: (item.atom_1, item.atom_2)})
            bond_lengths = cls._BondLength\
                .calculate(mayer_bond_orders,
                           coordinates_of_atoms,
                           item.atom_1, item.atom_2,
                           item.MBO_max, item.MBO_min,
                           item.id)
            self.bond_lengths.update({item.id: bond_lengths})
        return self

    def to_string(self) -> str:
        """Make string from BondLengthFromPairOfAtoms object

        Returns:
            **str**: String
        """
        string = ""
        for connections in self.bond_lengths.values():
            string += connections\
                .to_string()

        return string


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
