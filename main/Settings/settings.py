"""Settings module to process data from settings yaml file."""

from BondOrderProcessing.bond_order_processing.calculations\
    import PairOfAtoms
from dataclasses import dataclass


class Settings:
    """Settings.

    Object represents data in settings yaml file

    Attributes:
        histogram (dict['calc': bool, 'nr_bars': int | None]):
        pairs_atoms_list (list[PairOfAtoms]):
        calculations (dict['Q_i': dict['calc': bool, 'bond_id': str | None],
                       'connections': bool,
                       'bond_length': bool,
                       'CN': bool]):
        types_of_calculations (set[str]): Default - {'Q_i', 'connections', 
                        'bond_length', 'CN'}

    Raises:
        ValueError: The number of histogram bars is not specified !!!
        ValueError: Wrong keywords in yaml file!
        ValueError: Wrong calculations settings!!!!

    """

    histogram: dict['calc': bool, 'nr_bars': int | None]
    pairs_atoms_list: list[PairOfAtoms]
    calculations: dict['Q_i': dict['calc': bool, 'bond_id': str | None],
                       'connections': bool,
                       'bond_length': bool,
                       'CN': bool]
    types_of_calculations: set[str] = {
        'Q_i', 'connections', 'bond_length', 'CN'}

    def __init__(self, data: dict, PairOfAtoms: type = PairOfAtoms) -> None:
        """Constructor.

        Constructor

        Example:
        >>> from BondOrderProcessing.bond_order_processing.calculations import PairOfAtoms
        >>> data = {'calculations': { \
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
        [PairOfAtoms(atom_1='P', atom_2='P', MBO_min=1.2, MBO_max='INF', id='P=O'), \
PairOfAtoms(atom_1='P', atom_2='P', MBO_min=0.02, MBO_max='INF', id='P-O'), \
PairOfAtoms(atom_1='Al', atom_2='Al', MBO_min=0.02, MBO_max='INF', id='Al-O')]

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

        self.pairs_atoms_list = []
        self.calculations = {}
        valid_keys = ['histogram', 'pairs_atoms_list', 'calculations']

        if self.check_keys_correct(data.keys(), valid_keys) is False:
            raise ValueError("Wrong keywords in yaml file!")

        for item in data.get("pairs_atoms_list"):
            self.pairs_atoms_list.append(PairOfAtoms(item.get('atom_1'), item.get('atom_1'),
                                                     item.get('mbo_min'),
                                                     item.get('mbo_max'),
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
                if type(item := calculations.get(key)) is dict and (key == 'Q_i'):
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
            self.calculations = {'Q_i': {'calc': False, 'bond_id': None},
                                 'connections': False,
                                 'bond_length': False,
                                 'CN': False}

    @staticmethod
    def check_keys_correct(keys: list[str], ref: list[str]) -> bool:
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
