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

    def __init__(self, data: dict) -> None:
        self.pairs_atoms_list = []
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

        if data.get('calculations') is not None:
            # TODO
            pass
        else:
            self.calculations = {'Q_i': {'calc': False, 'bond_id': None},
                                 'connections': False,
                                 'bond_length': False,
                                 'CN': False}
