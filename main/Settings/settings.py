"""Settings module to process data from settings yaml file."""

from BondOrderProcessing.bond_order_processing.calculations\
    import PairOfAtoms


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

    def __init__(self, data: dict, PairOfAtoms: type = PairOfAtoms) -> None:
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

        self.pairs_atoms_list: list[PairOfAtoms] = []
        self.calculations: dict = {}

        if self.check_keys_correct(data.keys(), self.VALID_KEYS_lEVEL_0) is False:
            raise ValueError("Wrong keywords in yaml file!")

        for value in data.values():
            if type(value) is dict:
                for key, value_2 in value.items():
                    if key == 'q_i':
                        if self.check_keys_correct(value_2.keys(),
                                                   self.VALID_KEYS_lEVEL_2)\
                                is False:
                            raise ValueError("Wrong keywords in yaml file!")
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
            if histogram.get('calc') and (histogram.get('nr_bars') is not None):
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
                    if item.get('calc') and (item.get('bond_id') is not None):
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
