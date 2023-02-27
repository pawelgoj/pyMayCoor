"""Settings module to process data from settings yaml file."""
import yaml
from BondOrderProcessing.bond_order_processing.calculations\
    import PairOfAtoms
import sys
import re
sys.path.append(r'main/')


class Settings:
    """Settings.

    Object represents data in settings yaml file

    Attributes:
        histogram (dict['calc': bool, 'nr_bars': int | None]):
        pairs_atoms_list (list[PairOfAtoms]):
        calculations (dict['q_i': dict['calc': bool, 'bond_id': str | None],
                       'connections': bool,
                       'bond_length': bool,
                       'cn': bool]):
        types_of_calculations (set[str]): Default - {'q_i', 'connections',
                        'bond_length', 'cn'}

    Raises:
        ValueError: The number of histogram bars is not specified !!!
        ValueError: Wrong keywords in yaml file!
        ValueError: Wrong calculations settings!!!!

    """
    VALID_KEYS_lEVEL_0: tuple[str] = (
        'histogram', 'pairs_atoms_list', 'calculations')

    VALID_KEYS_lEVEL_1_LIST: tuple[str] = ('atom_1', 'atom_2', 'mbo_min',
                                           'mbo_max', 'id')

    VALID_KEYS_lEVEL_2: tuple[str] = ('calc', 'bond_id')

    histogram: dict['calc': bool, 'nr_bars': int | None]
    pairs_atoms_list: list[PairOfAtoms]
    calculations: dict['q_i': dict['calc': bool, 'bond_id': str | None],
                       'connections': bool,
                       'bond_length': bool,
                       'cn': bool,
                       'covalence': bool]
    types_of_calculations: set[str] = {
        'q_i', 'connections', 'bond_length', 'cn', 'covalence'}

    def __init__(self, data: dict | None = None,
                 PairOfAtoms: type = PairOfAtoms) -> None:
        """Constructor.

        Constructor

        Example:
        >>> from BondOrderProcessing.bond_order_processing.calculations import PairOfAtoms
        >>> data = {'calculations': { \
                        'covalence': True,\
                        'bond_length': True, \
                        'cn': True, \
                        'connections': True, \
                        'q_i': {'bond_id': 'P=O', 'calc': True}}, \
                  'histogram': {'calc': True, 'nr_bars': 10}, \
                  'pairs_atoms_list': \
                        [{ \
                            'atom_1': 'P', \
                            'atom_2': 'O', \
                            'id': 'P=O', \
                            'mbo_max': 'INF', \
                            'mbo_min': 1.2 \
                        }, \
                        { \
                            'atom_1': 'P', \
                            'atom_2': 'O', \
                            'id': 'P-O', \
                            'mbo_max': 'INF', \
                            'mbo_min': 0.02 \
                        }, \
                        { \
                            'atom_1': 'Al', \
                            'atom_2': 'O', \
                            'id': 'Al-O', \
                            'mbo_max': 'INF',\
                            'mbo_min': 0.02 }]}
        >>> settings = Settings(data)
        >>> type(settings) is Settings
        True
        >>> settings.histogram
        {'calc': True, 'nr_bars': 10}
        >>> settings.pairs_atoms_list
        [PairOfAtoms(atom_1='P', atom_2='O', MBO_min=1.2, MBO_max='INF', id='P=O'), \
PairOfAtoms(atom_1='P', atom_2='O', MBO_min=0.02, MBO_max='INF', id='P-O'), \
PairOfAtoms(atom_1='Al', atom_2='O', MBO_min=0.02, MBO_max='INF', id='Al-O')]

        Args:
            data (dict): data from yaml setting file
            PairOfAtoms (type): PairOfAtoms

        Raises:
            ValueError: The number of histogram bars is not specified !!!
            ValueError: Wrong keywords in yaml file!
            ValueError: Wrong calculations settings!!!!

        Returns:
            Settings: Object

        """
        self.histogram = {}
        self.pairs_atoms_list: list[PairOfAtoms] = []
        self.calculations: dict = {}

        if data is None:
            self.histogram = {'calc': False}
            self.calculations = {'q_i': {'calc': False},
                                 'bond_length': False,
                                 'connections': False,
                                 'cn': False,
                                 'covalence': False}

        else:
            try:
                if self.check_keys_correct(data.keys(), self.VALID_KEYS_lEVEL_0) is False:
                    raise ValueError("Wrong keywords in yaml file!")
            except AttributeError:
                raise ValueError("Wrong yaml file!")

            for value in data.values():
                if type(value) is dict:
                    for key, value_2 in value.items():
                        if key == 'q_i':
                            if self.check_keys_correct(value_2.keys(),
                                                       self.VALID_KEYS_lEVEL_2)\
                                    is False:
                                raise ValueError(
                                    "Wrong keywords in yaml file!")
                elif type(value) is list:
                    for item in value:
                        if self.check_keys_correct(item.keys(),
                                                   self.VALID_KEYS_lEVEL_1_LIST)\
                                is False:
                            raise ValueError("Wrong keywords in yaml file!")

            for item in data.get("pairs_atoms_list"):
                mbo_min = float(item.get('mbo_min'))
                if item.get('mbo_max') == 'INF':
                    mbo_max = item.get('mbo_max')
                else:
                    mbo_max = float(item.get('mbo_max'))

                self.pairs_atoms_list.append(PairOfAtoms(item.get('atom_1'),
                                                         item.get('atom_2'),
                                                         mbo_min,
                                                         mbo_max,
                                                         item.get('id')))

            if (histogram := data.get('histogram')) is not None:
                if (histogram.get('calc') and (histogram.get('nr_bars') is not None))\
                        or (not histogram.get('calc')
                            and (histogram.get('nr_bars') is not None)):
                    self.histogram = {
                        'calc': histogram['calc'], 'nr_bars': histogram['nr_bars']}
                elif histogram.get('calc') and (histogram.get('nr_bars') is None):
                    raise ValueError(
                        'The number of histogram bars is not specified !!!')
                else:
                    self.histogram = {
                        'calc': False, 'nr_bars': None}

            if (calculations := data.get('calculations')) is not None:
                for key in self.types_of_calculations:
                    if type(item := calculations.get(key)) is dict and (key == 'q_i'):
                        if item.get('calc') and (item.get('bond_id') is not None)\
                            or (not item.get('calc') and (item.get('bond_id')
                                is not None)):

                            self.calculations.update(
                                {key: {'calc': True, 'bond_id': item.get('bond_id')}})

                        elif item.get('calc') == False:

                            self.calculations.update(
                                {key: {'calc': False, 'bond_id': None}})

                        else:
                            raise ValueError('Wrong calculations settings!!!!')
                    elif type(calculations.get(key)) is dict:
                        raise ValueError('Wrong calculations settings!!!!')
                    else:
                        self.calculations.update({key: calculations.get(key)})
            else:
                self.calculations = {'q_i': {'calc': False, 'bond_id': None},
                                     'connections': False,
                                     'bond_length': False,
                                     'cn': False,
                                     'covalence': False}

    def save_data(self, path: str):

        out_list = []
        for pair_of_atoms in self.pairs_atoms_list:
            out_dict = {}
            out_dict.update({'atom_1': pair_of_atoms.atom_1})
            out_dict.update({'atom_2': pair_of_atoms.atom_2})
            out_dict.update({'mbo_min': pair_of_atoms.MBO_min})
            out_dict.update({'mbo_max': pair_of_atoms.MBO_max})
            out_dict.update({'id': pair_of_atoms.id})

            out_list.append(out_dict)

        output = {'histogram': self.histogram,
                  'pairs_atoms_list': out_list,
                  'calculations': self.calculations}

        if re.search('.*\.yaml|.*\.yml', path) is not None:
            pass
        else:
            path += '.yaml'

        output_yaml = yaml.dump(output)

        with open(path, 'w') as file:
            file.write(output_yaml)

    @ staticmethod
    def check_keys_correct(keys: list[str], ref: tuple[str]) -> bool:
        """Check keys correct.

        Example:
        >>> Settings.check_keys_correct(['histogram', 'pairs_atoms_list', 'calculations'], \
            ['histogram', 'pairs_atoms_list', 'calculations'])
        True
        >>> Settings.check_keys_correct(['histogram', 'pairs_atoms_list', 'calculations'],\
            ['histogram', 'pairs_atoms_list', 'incorrect'])
        False

        Args:
            keys (list[str]): keywords
            ref (list[str]): reference

        Returns:
            bool: Keywords correct or not
        """

        for key in keys:
            if key in ref:
                pass
            else:
                return False
        return True

    def del_last_added_pair_of_atom_object(self):
        if self.pairs_atoms_list != []:
            self.pairs_atoms_list.pop()

    def cast_stored_data_to_correct_typest(self):

        if self.histogram.get('nr_bars', None) is not None:
            self.histogram['nr_bars'] = int(self.histogram['nr_bars'])

        temp = []
        for item in self.pairs_atoms_list:
            if item.MBO_max == 'INF':
                value = item.MBO_max
            else:
                value = float(item.MBO_max)
            temp.append(PairOfAtoms(item.atom_1, item.atom_2,
                        float(item.MBO_min), value, item.id))

        self.pairs_atoms_list = temp
