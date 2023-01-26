"""Input data module."""
from abc import ABC
from abc import abstractmethod
import re


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

    mulliken: dict[int: tuple[str, float]] = {}
    lodwin: dict[int: tuple[str, float]] = {}
    valence: dict[int: tuple[str, float]] = {}

    def __init__(self):
        pass


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
                         int) -> tuple[str, str] | None:
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
    _CONSTANT_TO_CALCULATE_ANGSTROMS_FROM_BOHR: float = 0.52917720859

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

    def get_atom_coordinates_converted_in_angstrom(self, id: int)\
            -> tuple[x, y, z]:
        """Get atom coordinates converted in angstroms if they were stored as 
        Bohr units.

        Example:
        >>> coordinates_of_atoms = CoordinatesOfAtoms()
        >>> coordinates_of_atoms.add_new_atom(1, 'P', (1, 1, 1))
        >>> coordinates_of_atoms.get_atom_coordinates_converted_in_angstrom(1)
        (0.52917720859, 0.52917720859, 0.52917720859)

        Args:
            id (int): atom id

        Returns:
            tuple[x, y, z]: coordinates in angstroms
        """
        temp_coordinates = self._coordinates.get(id, None)
        if temp_coordinates is not None:
            coordinates = (self._CONSTANT_TO_CALCULATE_ANGSTROMS_FROM_BOHR
                           * temp_coordinates[0],
                           self._CONSTANT_TO_CALCULATE_ANGSTROMS_FROM_BOHR
                           * temp_coordinates[1],
                           self._CONSTANT_TO_CALCULATE_ANGSTROMS_FROM_BOHR
                           * temp_coordinates[2])
        else:
            coordinates = temp_coordinates

        return coordinates

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
    coordinates_of_atoms: CoordinatesOfAtoms | None = None

    def __init__(self, Populations: type = Populations,
                 UnitCell: type = UnitCell,
                 MayerBondOrders: type = MayerBondOrders,
                 CoordinatesOfAtoms: type = CoordinatesOfAtoms):
        """Construct.

        Args:
            Populations (type, optional): Defaults to Populations.
            UnitCell (type, optional): Defaults to UnitCell.
            MayerBondOrders (type, optional): Defaults to MayerBondOrders.
            CoordinatesOfAtoms (type, optional): Defaults to CoordinatesOfAtoms.
        """

        self.Populations = Populations
        self.UnitCell = UnitCell
        self.MayerBondOrders = MayerBondOrders
        self.CoordinatesOfAtoms = CoordinatesOfAtoms

    @abstractmethod
    def load_input_data_from_file(self, path: str) -> None:
        """Load input data from file.

        Args:
            path (str): path to file.

        Return:
            None
        """
        pass

    @staticmethod
    def check_is_correct_file(data_in_file: str, fingerprint: str) -> bool:
        if fingerprint in data_in_file:
            return True
        else:
            return False


class InputDataFromCPMD(InputData):
    """_summary_

    Args:
        InputData (_type_): _description_
    """
    _fingerprint: str = "The CPMD consortium"
    _fingerprint_beginning_populations: str = "POPULATION ANALYSIS FROM PROJECTED"\
        + " WAVEFUNCTIONS"
    _fingerprint_end_populations: str = "ChkSum\(POP_MUL\)"
    _fingerprint_coordinates_of_atoms: str = "ATOM             COORDINATES"\
        + "                   CHARGES"
    _fingerprint_end_coordinates_of_atoms: str = "ChkSum\(CHARGES\)"
    _fingerprint_mayer_bond_orders: str = "MAYER BOND ORDERS FROM PROJECTED"\
        + " WAVEFUNCTIONS"

    _fingerprint_unit_cell: str = "SUPERCELL"

    _valid_population_columns_names: tuple[str] = (
        'ATOM', 'MULLIKEN', 'LOWDIN', 'VALENCE')

    _valid_coordinatios_columns_names: tuple[str] = (
        'X', 'Y', 'Z')

    def load_input_data_from_file(self, path: str) -> None:
        with open(path, 'r') as file:
            data = file.read()

        if self.check_is_correct_file(data, self._fingerprint) is not True:
            raise Exception("Wrong input file!")
        else:
            # TODO
            pass

    def _load_populations_from_file(self, file: str) -> Populations:

        rows = self._get_rows_of_data_from_file(file, self._fingerprint_beginning_populations,
                                                self._fingerprint_end_populations)
        labels = []
        for row in rows:
            have_string = True if re.search('[a-zA-Z]+', row) is \
                not None else False

            have_number = True if re.search('[0-9]+', row) is \
                not None else False

            if have_string and not have_number:
                labels = row.split()
                populations = Populations()
                continue
            elif have_string and have_number:
                splited = row.split()
                if len(labels) + 1 != len(splited):
                    raise Exception('Wrong quantity of columns in input file!')
                else:
                    populations = self._add_populations_attributes(
                        populations, splited, labels)

        return populations

    @classmethod
    def _add_populations_attributes(cls, populations: Populations,
                                    splited: list, labels: list[str])\
            -> Populations:
        i = 0
        for item in splited:
            if i == 0:
                id = int(item)
            elif labels[i-1] == cls._valid_population_columns_names[0]:
                symbol = item
            elif labels[i-1] == cls._valid_population_columns_names[1]:
                mulliken_value = float(item)
            elif labels[i-1] == cls._valid_population_columns_names[2]:
                lowdin_value = float(item)
            elif labels[i-1] == cls._valid_population_columns_names[3]:
                valence_value = float(item)
            i += 1

        populations.lodwin.update({id: (symbol, lowdin_value)})
        populations.mulliken.update({id: (symbol, mulliken_value)})
        populations.valence.update({id: (symbol, valence_value)})

        return populations

    def _load_coordinates_of_atoms_from_file(self, file: str)\
            -> CoordinatesOfAtoms:
        rows = self._get_rows_of_data_from_file(file, self._fingerprint_coordinates_of_atoms,
                                                self._fingerprint_end_coordinates_of_atoms)
        for row in rows:
            have_string = True if re.search('[a-zA-Z]+', row) is \
                not None else False

            have_number = True if re.search('[0-9]+', row) is \
                not None else False

            if have_string and not have_number:
                labels = row.split()
                coordinates_of_atoms = self.CoordinatesOfAtoms()
                continue
            elif have_string and have_number:
                splited = row.split()
                if len(labels) + 2 != len(splited):
                    raise Exception('Wrong quantity of columns in input file!')
                else:
                    coordinates_of_atoms = self._add_coordinations_attributes(
                        coordinates_of_atoms, splited, labels
                    )
        return coordinates_of_atoms

    @classmethod
    def _add_coordinations_attributes(cls, coordinates_of_atoms:
                                      CoordinatesOfAtoms,
                                      splited: list, labels: list[str])\
            -> CoordinatesOfAtoms:
        i = 0
        for item in splited:
            if i == 0:
                atom_id = int(item)
            elif i == 1:
                atom_symbol = item
            elif labels[i - 2] == cls._valid_coordinatios_columns_names[0]:
                x = float(item)
            elif labels[i - 2] == cls._valid_coordinatios_columns_names[1]:
                y = float(item)
            elif labels[i - 2] == cls._valid_coordinatios_columns_names[2]:
                z = float(item)
            i += 1

        coordinates_of_atoms.add_new_atom(atom_id, atom_symbol, (x, y, z))
        return coordinates_of_atoms

    @staticmethod
    def _get_rows_of_data_from_file(file: str,
                                    finger_print_begin: str, finger_print_end)\
            -> list[str]:
        """Get rows fo data from file
        Args:
            finger_print_begin (str): fingerprint on beginning of data
            finger_print_end (str): fingerprint on end of data
        Returns:
            list[str]: rows of string data
        """

        regex = f'(?<={finger_print_begin})[\s\S]*' \
            + f'(?={finger_print_end})'

        match = re.search(regex, file)
        return match[0].split('\n')

    def _load_mayer_bond_orders_from_file(self, file: str) -> MayerBondOrders:
        match = re.search(
            f"(?<={self._fingerprint_mayer_bond_orders}\n\n)([\S ]+\n)*", file)
        rows = match[0].split('\n')
        rows = [row for row in rows if row != '']
        number_of_atoms = int(rows[-1].split()[0])
        n = number_of_atoms // 8
        m = 1 if number_of_atoms % 8 > 0 else 0
        number_of_tables = m + n

        number_of_rows = (len(rows)) * number_of_tables
        match = re.search(
            f"(?<={self._fingerprint_mayer_bond_orders}\n\n)([\S ]+\n*){{{number_of_rows}}}", file)

        rows_full_table = []
        tables = match[0].split('\n\n')
        first_table = True
        for table in tables:
            splited = table.split('\n')
            i = 0
            for item in splited:
                if first_table:
                    row = item.split()
                    rows_full_table.append(row)
                elif i == 0:
                    row = item.split()
                    rows_full_table[i].extend(row)
                else:
                    row = item.split()
                    rows_full_table[i].extend(row[2:])
                i += 1
            first_table = False

        row_horizontal = rows_full_table.pop(0)
        i = 0
        j = 0
        horizontal_atom_symbol = {}
        horizontal_atom_id = []
        for item in row_horizontal:
            if i % 2 == 0:
                j += 1
                horizontal_atom_id.append(int(item))
            else:
                horizontal_atom_symbol.update(
                    {horizontal_atom_id[j - 1]: str(item)})
            i += 1

        vertical_atom_symbol = {}
        vertical_atom_id = []
        new_rows_full_table = []
        for row in rows_full_table:
            vertical_atom_id.append(int(row.pop(0)))
            vertical_atom_symbol.update(
                {vertical_atom_id[-1]: str(row.pop(0))})
            row = [float(item) for item in row]
            new_rows_full_table.append(row)

        mayer_bond_order = self.MayerBondOrders(new_rows_full_table,
                                                horizontal_atom_id,
                                                vertical_atom_id,
                                                horizontal_atom_symbol,
                                                vertical_atom_symbol)
        return mayer_bond_order

    @classmethod
    def _return_unit_cell(file: str):
        # TODO
        pass
