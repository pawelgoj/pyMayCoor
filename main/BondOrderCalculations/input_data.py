"""Input data module."""
from abc import ABC
from abc import abstractmethod


class UnitCell:
    """Unit cell.

    Attributes:
        a (float): Angstroms
        b (float): Angstroms
        c (float): Angstroms
        alfa (float): deg
        beta (float): deg
        gamma (float): deg

    """

    a: float = 0
    b: float = 0
    c: float = 0
    alfa: float = 0
    beta: float = 0
    gamma: float = 0

    def __init__(self):
        pass


class Populations:
    """Populations from MULLIKEN, LOWDIN analysis."""

    mulliken: dict[str: tuple[str, float]] | None = None
    lodwin: dict[str: tuple[str, float]] | None = None
    valence: dict[str: tuple[str, float]] | None = None

    def __init__(self):
        pass
        # TODO


class MayerBondOrders:
    """Mayer bond orders of atoms pairs."""
    rows = list[float]
    mayer_bond_orders: list[rows] = []
    horizontal_atom_id: list[int] = []
    horizontal_atom_symbol: dict[int: str] = {}
    vertical_atom_id: list[int] = []
    vertical_atom_symbol: dict[int: str] = {}

    def __init__(self, mayer_bond_orders: list[rows],
                 horizontal_atom_id: list[int],
                 vertical_atom_id: list[int],
                 horizontal_atom_symbol: dict[int: str] = {},
                 vertical_atom_symbol: dict[int: str] = {}):

        if (len(mayer_bond_orders) == len(horizontal_atom_id) or
           len(mayer_bond_orders[0]) == len(vertical_atom_id)):
            self.mayer_bond_orders = mayer_bond_orders
            self.horizontal_atom_id = horizontal_atom_id
            self.vertical_atom_id = vertical_atom_id
        else:
            raise ValueError("Size of mayer_bond_orders must fit"
                             + "to horizontal_atom_id and "
                             + "vertical_atom_id!!!")

        if (horizontal_atom_symbol != {} and vertical_atom_symbol != {}
            and len(horizontal_atom_symbol) == len(mayer_bond_orders)
                and len(vertical_atom_symbol) == len(mayer_bond_orders[0])):
            self.horizontal_atom_symbol = horizontal_atom_symbol
            self.vertical_atom_symbol = vertical_atom_symbol
        elif (horizontal_atom_symbol == {}
              and vertical_atom_symbol == {}):
            pass
        else:
            raise ValueError("Size of mayer_bond_orders must fit"
                             + "to horizontal_atom_symbol and "
                             + "vertical_atom_symbol!!!")

    def get_mayer_bond_order_between_atoms(self, atom_id_1: int, atom_id_2:
                                           int) -> float:
        """Get mayer bond order between atoms.

        Args:
            atom_id_1 (int): first atom id (row)
            atom_id_2 (int): second atom id (column)

        Returns:
            float: bond order
        """

        row = self.mayer_bond_orders[self.horizontal_atom_id.index(atom_id_2)]
        return row[self.vertical_atom_id.index(atom_id_1)]

    def get_atom_symbols(self, atom_id_1: int, atom_id_2:
                         int) -> tuple(str, str) | None:
        """Get atom symbols
        Args:
            atom_id_1 (int): atom 1 id
            atom_id_2 (int): atom 2 id
        Returns:
            tuple(str, str) | None: Symbol of atom 1 and atom 2,
                                    if wrong id of atoms returns None or
                                    atoms symbols have not been used.
        """
        atom_1 = self.horizontal_atom_symbol.get(atom_id_1, None)
        atom_2 = self.vertical_atom_symbol.get(atom_id_2, None)

        if atom_1 is None or atom_2 is None:
            return None
        else:
            return (atom_1, atom_2)


class CoordinatesOfAtoms:
    atom_id = int
    x = float
    y = float
    z = float
    ids: list[atom_id] = []
    _coordinates: dict[atom_id: tuple[x, y, z]] = {}
    atom_symbols: dict[atom_id: str] = {}

    def __init__(self, atom_coordinates_table: list[tuple[atom_id, str, x, y,
                                                          z]] = []) -> None:
        if atom_coordinates_table != []:
            while atom_coordinates_table != []:
                row = atom_coordinates_table.pop(0)
                self.ids.append(row[0])
                self.atom_symbols.update({row[0]: row[1]})
                self._coordinates.update({row[0]: (row[2], row[3], row[4])})

    def add_new_atom(self, id: int, atom_symbol: str, coordinates:
                     tuple[x, y, z]) -> None:
        self.ids.append(id)
        self.atom_symbols.update({id: atom_symbol})
        self._coordinates.update({id: coordinates})

    def get_atom_coordinates(self, id: int) -> tuple[x, y, z] | None:
        """Get atoms coordinates.

        Args:
            id (int): atom id

        Returns:
            tuple[x, y, z] | None: Returns atom coordinates or None if atom of
                                   given id does not exist.
        """
        return self._coordinates.get(id, None)

    def get_atom_symbol(self, id: int) -> str | None:
        """Get atom symbol

        Args:
            id (int): atom id

        Returns:
            str | None: Returns atom symbol or None if atom of
                        given id does not exist.
        """
        return self.atom_symbols.get(id)

    @property
    def coordinates(self) -> tuple[x, y, z]:
        coordinates = [value for value in self._coordinates.values()]
        return coordinates


class InputData(ABC):
    """Input data."""

    populations: Populations | None = None
    unit_cell: UnitCell | None = None
    mayer_bond_orders: MayerBondOrders | None = None

    def __init__(self, Populations: type = Populations,
                 UnitCell: type = UnitCell,
                 MayerBondOrders: type = MayerBondOrders):
        """Construct.

        Args:
            Populations (type, optional): _description_. Defaults to Populations.
            UnitCell (type, optional): _description_. Defaults to UnitCell.
            MayerBondOrders (type, optional): _description_. Defaults to MayerBondOrders.

        """

        self.Populations = Populations
        self.UnitCell = UnitCell
        self.MayerBondOrders = MayerBondOrders

    @abstractmethod
    def load_input_data_from_file(self, path: str) -> None:
        """Load input data from file.

        Args:
            path (str): path to file.

        Return:
            None
        """
        pass


class InputDataFromCPMD(InputData):
    """_summary_

    Args:
        InputData (_type_): _description_
    """
    pass
    # TODO
