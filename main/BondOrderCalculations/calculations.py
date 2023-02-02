import numpy as np
from typing import Callable
from abc import ABC
from abc import abstractmethod
from ..BondOrderCalculations.input_data import MayerBondOrders
from ..BondOrderCalculations.input_data import CoordinatesOfAtoms
from ..BondOrderCalculations.settings import PairOfAtoms

from dataclasses import dataclass


class Calculations(ABC):
    """Calculations base class."""

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
                  max_mayer_bond_order: float | str,
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

        if max_mayer_bond_order != "INF"\
                and not (type(max_mayer_bond_order) is float):
            raise ValueError("Wrong type of max_mayer_bond_order!!!!")

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
                            and max_mayer_bond_order is 'INF'):
                        coordination_number.bonds.update({atom_2_id: mbo})
                        coordination_number.cn += 1
                    elif (mbo > min_mayer_bond_order
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

        if max_mayer_bond_order != "INF"\
                and not (type(max_mayer_bond_order) is float):
            raise ValueError("Wrong type of max_mayer_bond_order!!!!")
        elif max_mayer_bond_order == "INF":
            inf = True
            max_mayer_bond_order = -1
            # -1 to prevent exception
        else:
            inf = False

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
                        and (mbo < max_mayer_bond_order or inf)):

                    for atom_3_id in atom_1_ids:
                        mbo = mayer_bond_orders\
                            .get_mayer_bond_order_between_atoms(atom_2_id,
                                                                atom_3_id)
                        if (mbo > min_mayer_bond_order
                                and (mbo < max_mayer_bond_order or inf)
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


@dataclass
class Connection:
    id_atom_2 = int
    mayer_bond_order = float

    atom_symbol_2: str
    bond_id: str
    quantity: int
    bonds: dict[id_atom_2: mayer_bond_order]


class Connections(Calculations):
    atom_1_id = int

    Connection: type = Connection
    connections: dict[atom_1_id: list[Connection]]
    atom_symbol_1: str

    @ classmethod
    def calculate(cls, mayer_bond_orders: MayerBondOrders,
                  atom_symbol_1: str,
                  pairs_atoms_list: list[PairOfAtoms]
                  ) -> type:

        pair_atom_list_containing_atom_1 = []
        for pair_atom in pairs_atoms_list:
            if pair_atom.atom_1 == atom_symbol_1\
                    or pair_atom.atom_2 == atom_symbol_1:

                pair_atom_list_containing_atom_1.append(pair_atom)
            else:
                continue

        atom_1_ids = mayer_bond_orders.get_atoms_ids(atom_symbol_1)
        connections = {}
        for atom_1_id in atom_1_ids:

            connections.update({atom_1_id: []})

            for pair_atoms in pair_atom_list_containing_atom_1:
                if v := pair_atoms.atom_1 != atom_symbol_1:
                    atom_symbol_2 = v
                else:
                    atom_symbol_2 = pair_atoms.atom_2

                connection = cls.Connection(
                    atom_symbol_2, pair_atoms.id, 0, {})

                atom_2_ids = mayer_bond_orders.get_atoms_ids(atom_symbol_2)

                for atom_2_id in atom_2_ids:

                    if pair_atoms.MBO_max != "INF"\
                            and not (type(pair_atoms.MBO_max) is float):
                        raise ValueError(
                            "Wrong type of max_mayer_bond_order!!!!")

                    mbo = mayer_bond_orders\
                        .get_mayer_bond_order_between_atoms(atom_1_id,
                                                            atom_2_id)

                    if (mbo > pair_atoms.MBO_min
                            and pair_atoms.MBO_max is 'INF'):

                        connection.quantity += 1
                        connection.bonds.update({atom_2_id: mbo})

                    elif (mbo > pair_atoms.MBO_min
                            and pair_atoms.MBO_max > mbo):

                        connection.quantity += 1
                        connection.bonds.update({atom_2_id: mbo})

                connections[atom_1_id].append(connection)

        self = cls()
        self.connections = connections
        self.atom_symbol_1 = atom_symbol_1

        return self

    def to_string(self) -> str:
        string = 'Connections of: ' + str(self.atom_symbol_1) + '\n\n'

        for atom_1_id, list_of_connections in self.connections.items():
            string = string + "Central atom id: " + str(atom_1_id) + "\n"

            for connection in list_of_connections:

                string = string + f"Bond id: {str(connection.bond_id)} "\
                    + f"(second atom: {str(connection.atom_symbol_2)})\n"\
                    + f"quantity: {connection.quantity}\n"\
                    + "Bonds:\n"

                string_id_line = "id: "
                string_mbo_line = "mbo: "

                for id, mbo in connection.bonds.items():
                    string_id_line += f"{id} "
                    string_mbo_line += f"{round(mbo, 3)} "

                string = string + string_id_line + '\n'\
                    + string_mbo_line + '\n\n'

        return string


class Covalence(Calculations):
    covalence: dict[int, float]
    atom_symbol: str

    @ classmethod
    def calculate(cls, mayer_bond_orders: MayerBondOrders,
                  atom_symbol: str) -> type:

        atom_ids = mayer_bond_orders.get_atoms_ids(atom_symbol)

        self = cls()
        self.atom_symbol = atom_symbol
        self.covalence = {}
        for id in atom_ids:
            mbos = mayer_bond_orders.get_all_mayer_bond_orders_of_atom(id)
            self.covalence.update({id: sum(mbos)})

        return self

    def to_string(self) -> str:
        # TODO
        pass


class BondLength(Calculations):
    atom_id_1 = int
    atom_id_2 = int

    id_of_bond: str
    atom_symbol_1: str
    atom_symbol_2: str
    lengths: dict[atom_id_1: dict[atom_id_2: float]]
    mbos: dict[atom_id_1: dict[atom_id_2: float]]

    @ classmethod
    def calculate(cls,
                  mayer_bond_orders: MayerBondOrders,
                  coordinates_of_atoms: CoordinatesOfAtoms,
                  atom_symbol_1: str,
                  atom_symbol_2: str,
                  max_mayer_bond_order: float | str,
                  min_mayer_bond_order: float,
                  id_of_bond: str) -> type:

        if max_mayer_bond_order != "INF"\
                and not (type(max_mayer_bond_order) is float):
            raise ValueError("Wrong type of max_mayer_bond_order!!!!")
        elif max_mayer_bond_order == "INF":
            inf = True
            max_mayer_bond_order = -1
            # -1 to prevent exception
        else:
            inf = False

        atom_1_ids = mayer_bond_orders.get_atoms_ids(atom_symbol_1)
        atom_2_ids = mayer_bond_orders.get_atoms_ids(atom_symbol_2)

        self = cls()
        self.id_of_bond = id_of_bond
        self.atom_symbol_1 = atom_symbol_1
        self.atom_symbol_2 = atom_symbol_2
        self.lengths = {}
        self.mbos = {}

        for atom_1_id in atom_1_ids:
            self.lengths.update({atom_1_id: {}})
            self.mbos.update({atom_1_id: {}})
            for atom_2_id in atom_2_ids:
                mbo = mayer_bond_orders\
                    .get_mayer_bond_order_between_atoms(atom_1_id,
                                                        atom_2_id)
                length = coordinates_of_atoms\
                    .get_distance_between_atoms(atom_1_id, atom_2_id)

                if mbo > min_mayer_bond_order and (
                    mbo < max_mayer_bond_order
                    or max_mayer_bond_order == 'INF'
                ):
                    self.lengths[atom_1_id].update({atom_2_id: length})
                    self.mbos[atom_1_id].update({atom_2_id: mbo})
                else:
                    continue

        # remove empty keys.
        for key in self.lengths.keys():
            if self.lengths[key] == {}:
                del self.lengths[key]
                del self.mbos[key]

        return self

    def to_string(self) -> str:
        string = f'Bond lengths of bond id: {self.id_of_bond} '\
            + f'(atoms: {self.atom_symbol_1}, {self.atom_symbol_2}):\n\n'\
            + 'id_1 id_2 length mbo\n'

        for key_1 in self.lengths.keys():
            for key_2 in self.lengths[key_1].keys():
                string = string + f'{key_1} {key_2} '\
                    + f'{self.lengths[key_1][key_2]} '\
                    + f'{self.mbos[key_1][key_2]}\n'

        string += '\n'

        return string
