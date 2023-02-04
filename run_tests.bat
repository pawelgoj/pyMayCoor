:: Doctests (Examples)
pytest --doctest-modules main/BondOrderCalculations/BondOrderCalculations/input_data.py
pytest --doctest-modules main/BondOrderCalculations/BondOrderCalculations/__init__.py
pytest --doctest-modules main/Settings/settings.py
:: Normal unit tests
pytest -s --cov=main\BondOrderCalculations\BondOrderCalculations test/ > pytest-converage.txt