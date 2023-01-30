import numpy as np
from typing import Callable
from abc import ABC
from abc import abstractmethod
from ..BondOrderCalculations.input_data import MayerBondOrders
from dataclasses import dataclass


class Calculations(ABC):

    @abstractmethod
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

        histogram = cls()
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
    id_atom_2 = int
    mayer_bond_order = float

    id_atom_1: int
    cn: int
    bonds: dict[id_atom_2: mayer_bond_order]


class CoordinationNumbers(Calculations):
    mayer_bond_orders: MayerBondOrders
    CoordinationNumber: type = CoordinationNumber
    list_coordinations_number: list[CoordinationNumber]
    id_of_bond: str
    atom_symbol: str

    @classmethod
    def calculate(cls, mayer_bond_orders: MayerBondOrders,
                  atom_symbol_1: str, atom_symbol_2: str,
                  max_mayer_bond_order: float,
                  min_mayer_bond_order: float,
                  id_of_bond: str) -> type:

        atom_1_ids = mayer_bond_orders.get_atoms_ids(atom_symbol_1)
        atom_2_ids = mayer_bond_orders.get_atoms_ids(atom_symbol_2)

        list_coordinations_number = []
        for atom_1_id in atom_1_ids:

            coordination_number = cls.CoordinationNumber(atom_1_id, 0, {})

            for atom_2_id in atom_2_ids:
                if atom_1_id != atom_2_id:

                    mbo = mayer_bond_orders\
                        .get_mayer_bond_order_between_atoms(atom_1_id,
                                                            atom_2_id)
                    if (mbo > min_mayer_bond_order
                            and mbo < max_mayer_bond_order):
                        coordination_number.bonds.update({atom_2_id: mbo})
                        coordination_number.cn += 1
                    else:
                        continue

            list_coordinations_number.append(coordination_number)

        self = cls()
        self.id_of_bond = id_of_bond
        self.atom_symbol = atom_symbol_1
        self.list_coordinations_number = list_coordinations_number

        return self

    def calculate_statistics(self) -> None:
        pass
        # TODO

    def get_statistics(self):
        pass
        # TODO

    def to_string(self) -> str:
        string = "CN of " + str(self.atom_symbol) + " bond: "\
            + str(self.id_of_bond) + "\n\n"
        for item in self.list_coordinations_number:
            string = string + "id: " + str(item.id_atom_1) + " "\
                + "CN: " + str(item.cn) + "\n" + "Bond orders: "

            for key, value in item.bonds.items():
                string += str(key) + ' ' + str(value)

            string += '\n'
        string += '\n'
        return string
