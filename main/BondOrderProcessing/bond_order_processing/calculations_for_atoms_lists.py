"""Calculations in this module are made for PairOfAtoms
objects lists. This module is added in version: 1.1.0"""

from .calculations import Calculations
from .calculations import Statistics


class HistogramsFromPairOfAtoms(Calculations):

    def calculate() -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass


class ConnectionsFromPairOfAtoms(Calculations):
    def calculate() -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass


class BondLengthFromPairOfAtoms(Calculations):
    def calculate() -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass


class CovalenceFromPairOfAtoms(Calculations):
    def calculate() -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass


class CoordinationNumbersFromPairOfAtoms(Calculations, Statistics):
    def calculate() -> type:
        # TODO
        pass

    def calculate_statistics(self) -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass


class QiUnitsFromPairOfAtoms(Calculations, Statistics):
    def calculate() -> type:
        # TODO
        pass

    def calculate_statistics(self) -> type:
        # TODO
        pass

    def to_string(self) -> str:
        # TODO
        pass
