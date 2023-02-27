import pytest
import sys
sys.path.append(r'main/')
from main.settings.settings import Settings


class TestSettings:
    @pytest.mark.usefixtures("env_for_settings_tests")
    def test_save_data(self, env_for_settings_tests):
        data = {'calculations': {
            'covalence': True,
            'bond_length': True,
            'cn': True,
            'connections': True,
            'q_i': {'bond_id': 'P=O', 'calc': True}},
            'histogram': {'calc': True, 'nr_bars': 10},
            'pairs_atoms_list':
                [{
                    'atom_1': 'P',
                    'atom_2': 'O',
                    'id': 'P=O',
                    'mbo_max': 'INF',
                    'mbo_min': 1.2
                },
            {
                    'atom_1': 'P',
                    'atom_2': 'O',
                    'id': 'P-O',
                    'mbo_max': 'INF',
                    'mbo_min': 0.02
                },
            {
                    'atom_1': 'Al',
                    'atom_2': 'O',
                    'id': 'Al-O',
                    'mbo_max': 'INF',
                    'mbo_min': 0.02}]}
        settings = Settings(data)
        settings.save_data(env_for_settings_tests)
        with open(env_for_settings_tests, 'r', encoding="utf-8") as file:
            data = file.read()
        print(data)

        check = ['histogram', 'pairs_atoms_list', 'calculations',
                 'calc', 'atom_1', 'q_i']

        for item in check:
            assert item in data
