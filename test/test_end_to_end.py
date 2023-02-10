import os
import pytest
import subprocess


class TestEndToEnd:
    @pytest.mark.usefixtures("env_for_end_to_end_tests")
    def test_execute_app_in_cmd(self, env_for_end_to_end_tests):
        print(env_for_end_to_end_tests)
        fn = env_for_end_to_end_tests / 'output.txt'
        print(f'{fn=}')
        subprocess.run(
            f'python3_10 main/main.py -i ./egzamples_instructions/out1.txt -s ./egzamples_instructions/settings.yaml -o {fn}', shell=True)

        with open(fn, 'r', encoding="utf-8") as file:
            print(file.read())
        assert True
