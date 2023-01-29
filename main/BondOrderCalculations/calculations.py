import numpy as np
from typing import Callable
from abc import ABC
from abc import abstractmethod
from input_data import MayerBondOrders
from dataclasses import dataclass


class Calculations(ABC):

    @abstractmethod
    @classmethod
    def calculate() -> type:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass


class Histogram(Calculations):
    """Methods to generate histograms"""
    histogram: Callable = np.histogram
    x: list[float] = []
    y: list[int] = []

    @classmethod
    def calculate(cls, values: list[float], bins: int)\
            -> type:
        """Calculate histogram.

        Args:
            values (list[float]): list of values
            bins (int): number of bins in histogram

        Returns:
            tuple[list[float], list[int]]: (list of x, list of y)
        """
        histogram = cls.histogram(values, bins)

        y = histogram[0]
        x = histogram[1]
        y = y.tolist()
        x = x.tolist()

        first_loop = True
        new_x = []
        for item in x:
            if first_loop:
                first_loop = False
                previous = item
            else:
                new_x.append((item
                              + previous) / 2)
                previous = item

        histogram = Histogram()
        histogram.x = new_x
        histogram.y = y
        return histogram

    def to_string(self, atom_symbol_1: str, atom_symbol_2: str)\
            -> str:
        """Make string from Histogram object

        Returns:
            str:
        """
        string = atom_symbol_1 + ', ' + atom_symbol_2 + '\n\n'
        string = string + 'Interval/2' + ' ' + 'Count' + '\n\n'
        for i in range(len(self.x)):
            string = string + str(self.x[i]) + ' ' + str(self.y[i]) + '\n'

        string = string + '\n'

        return string


@dataclass
class CoordinationNumber:
    id_atom_1: int
    cn: int
    id_atom_2 = int
    mayer_bond_order = float
    bonds: dict[id_atom_2: mayer_bond_order]


class CoordinationNumbers(Calculations):
    mayer_bond_orders: MayerBondOrders
    CoordinationNumber: type = CoordinationNumber
    id_of_bond: str

    @classmethod
    def calculate(cls, mayer_bond_orders: MayerBondOrders,
                  atom_symbol_1: str, atom_symbol_2: str,
                  max_mayer_bond_order: float,
                  min_mayer_bond_order: float,
                  id_of_bond: str) -> type:

        pass
