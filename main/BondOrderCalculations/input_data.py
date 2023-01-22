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
    mayer_bond_orders: list[list[float]] = []
    horizontal_atom_id: list[int] = []
    horizontal_atom_symbol: dict[int: str] = {}
    vertical_atom_id: list[int] = []
    vertical_atom_symbol: dict[int: str] = {}

    def __init__(self):
        pass
        # TODO

    def get_mayer_bond_order_between_atoms(self, atom_id_1: int, atom_id_2:
                                           int) -> float:
        # TODO
        pass


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
