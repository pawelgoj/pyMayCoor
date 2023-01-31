import numpy as np
from typing import Callable
from abc import ABC
from abc import abstractmethod
from ..BondOrderCalculations.input_data import MayerBondOrders
from dataclasses import dataclass
from copy import deepcopy


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
    """Coordination Numbers.

    Generate list of CoordinationNumber objects and processes it.

    Args:
        Calculations (_type_): _description_

    Returns:
        _type_: _description_
    """
    mayer_bond_orders: MayerBondOrders
    CoordinationNumber: type = CoordinationNumber
    list_coordinations_number: list[CoordinationNumber]
    id_of_bond: str
    atom_symbol: str
    statistics: dict[int: float] | None = None

    @classmethod
    def calculate(cls, mayer_bond_orders: MayerBondOrders,
                  atom_symbol_1: str, atom_symbol_2: str,
                  max_mayer_bond_order: float,
                  min_mayer_bond_order: float,
                  id_of_bond: str) -> type:
        """Calculate CoordinationNumbers object.

        Args:
            mayer_bond_orders (MayerBondOrders): MayerBondOrders object
            atom_symbol_1 (str): central atom symbol
            atom_symbol_2 (str): Ligand symbol
            max_mayer_bond_order (float): max cut of radius
            min_mayer_bond_order (float): min cut of radius
            id_of_bond (str): id of bond

        Returns:
            type: CoordinationNumbers object
        """

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

    def calculate_statistics(self) -> type:
        """Calculate statistics of CoordinationNumbers.

        Statistic are in "statistics" attribute.

        Returns:
            type: CoordinationNumbers object
        """
        cns = self._get_list_of_coordination_numbers()
        quantities = {}
        for cn in cns:
            for item in self.list_coordinations_number:
                if item.cn == cn:
                    if quantities.get(cn, None) is None:
                        quantities.update({cn: 1})
                    else:
                        quantities[cn] = quantities[cn] + 1

        number_of_atoms = len(self.list_coordinations_number)
        statistics = {}
        for key, value in quantities.items():
            statistics.update({key: (value/number_of_atoms) * 100})

        self.statistics = statistics

        return self

    def _get_list_of_coordination_numbers(self) -> list[int]:
        cns = []
        for item in self.list_coordinations_number:
            if item.cn not in cns:
                cns += [item.cn]

        return cns

    def to_string(self) -> str:
        """Make string from CoordinationNumbers object.

        Returns:
            str:
        """
        string = "CN of " + str(self.atom_symbol) + " bond: "\
            + str(self.id_of_bond) + "\n\n"
        for item in self.list_coordinations_number:
            string = string + "id: " + str(item.id_atom_1) + " "\
                + "CN: " + str(item.cn) + "\n" + "Bond orders (id: mbo): "

            length = len(item.bonds)
            i = 1
            for key, value in item.bonds.items():
                string += str(key) + ': ' + str(value)
                if i < length:
                    string += ', '
                else:
                    pass
                i += 1

            string += '\n'
        string += '\n'

        if self.statistics is not None:
            string = string + "Statistics of: "\
                + str(self.atom_symbol) + "\n\n" + "CN %\n"
            for key, value in self.statistics.items():
                string = string + str(key) + ' ' + str(round(value, 3)) + '\n'

            string = string + '\n'

        return string


class QiUnits(Calculations):
    id_of_bond: str
    atom_symbol_1: str
    atom_symbol_2: str
    q_i_units: dict[int, int] = {}
    statistics: dict[int: float] | None = None

    @classmethod
    def calculate(cls, mayer_bond_orders: MayerBondOrders,
                  atom_symbol_1: str,
                  atom_symbol_2: str,
                  max_mayer_bond_order: float,
                  min_mayer_bond_order: float,
                  id_of_bond: str) -> type:

        atom_1_ids = mayer_bond_orders.get_atoms_ids(atom_symbol_1)
        atom_2_ids = mayer_bond_orders.get_atoms_ids(atom_symbol_2)

        self = cls()
        self.id_of_bond = id_of_bond
        self.atom_symbol_1 = atom_symbol_1
        self.atom_symbol_2 = atom_symbol_2
        for atom_1_id in atom_1_ids:

            self.q_i_units.update({atom_1_id: 0})

            for atom_2_id in atom_2_ids:
                mbo = mayer_bond_orders\
                    .get_mayer_bond_order_between_atoms(atom_1_id,
                                                        atom_2_id)
                if (mbo > min_mayer_bond_order
                        and mbo < max_mayer_bond_order):

                    for atom_3_id in atom_1_ids:
                        mbo = mayer_bond_orders\
                            .get_mayer_bond_order_between_atoms(atom_2_id,
                                                                atom_3_id)
                        if (mbo > min_mayer_bond_order
                                and mbo < max_mayer_bond_order
                                and atom_3_id != atom_1_id):

                            self.q_i_units[atom_1_id] += 1
                            break

                        else:
                            continue

        return self

    def calculate_statistics(self) -> type:

        unique_values = []
        for value in self.q_i_units.values():
            if value not in unique_values:
                unique_values.append(value)

        quantities = {}
        for unique in unique_values:
            quantities.update({unique: 0})
            for value in self.q_i_units.values():
                if value == unique:
                    quantities[unique] += 1
                else:
                    continue

        quantity_of_all_Q_i = len(self.q_i_units)

        self.statistics = {}

        for key, value in quantities.items():
            self.statistics.update({key: (value/quantity_of_all_Q_i) * 100})

        return self

    def to_string(self) -> str:
        string = "Q_i of " + str(self.atom_symbol_1) + ' bond id: '\
            + str(self.id_of_bond) + "\n\n"

        string += "id Q_i[i]\n"

        for key, value in self.q_i_units.items():
            string = string + str(key) + ' ' + str(value) + '\n'

        string += '\n'

        if self.statistics is not None:
            string = string + 'Statistics of Q_i: ' + str(self.atom_symbol_1)\
                + ', bond id: ' + str(self.id_of_bond) + '\n\n'

            string += 'Q_i[i] [%]\n'

            for key, value in self.statistics.items():
                string = string + str(key) + ' ' + str(round(value, 3)) + '\n'

        string += '\n'

        return string
