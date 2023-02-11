import pytest
import subprocess


class TestEndToEnd:
    @pytest.mark.usefixtures("env_for_end_to_end_tests_2")
    def test_execute_app_in_cmd(self, env_for_end_to_end_tests_2):
        fn = env_for_end_to_end_tests_2

        subprocess.run(
            f'python3_10 ./main/main.py -i ./egzamples_instructions/out1.txt -s ./egzamples_instructions/settings.yaml -o "{fn}"', shell=True)

        with open(fn, 'r', encoding="utf-8") as file:
            data = file.read()
            check = ['# pyMayCoor', '# Histograms', '# Qⁱ numbers',
                     '# Connections', '# Bond lengths', '# Covalence from Mayer bond orders']

        result = True
        for item in check:
            if item not in data:
                result = False
                break

        assert result
