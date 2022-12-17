from dataclasses import dataclass
from pprint import pprint


@dataclass
class PairOfAtoms:
    atom_1: str
    atom_2: str
    MBO_min: float
    MBO_max: float | str
    id: str


class Settings:
    histogram: dict['calc': bool, 'nr_bars': int | None]
    pairs_atoms_list: list[PairOfAtoms]
    calculations: dict['Q_i': dict['calc': bool, 'bond_id': str | None],
                       'connections': bool,
                       'bond_length': bool,
                       'CN': bool]
    types_of_calculations: set[str] = {
        'Q_i', 'connections', 'bond_length', 'CN'}

    def __init__(self, data: dict) -> None:
        self.pairs_atoms_list = []
        self.calculations = {}
        valid_keys = ['histogram', 'pairs_atoms_list', 'calculations']

        if check_keys_correct(data.keys(), valid_keys) is False:
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
                if type(item := calculations.get(key)) is dict and (key is 'Q_i'):
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
            for key in keys:
                if key in ref:
                    pass
                else:
                    return False
            return True
