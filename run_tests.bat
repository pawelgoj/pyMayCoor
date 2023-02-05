:: Doctests (Examples)
pytest --doctest-modules main/BondOrderProcessing/bond_order_processing/input_data.py
pytest --doctest-modules main/BondOrderProcessing/bond_order_processing/__init__.py
pytest --doctest-modules main/Settings/settings.py
:: Normal unit tests
pytest -s --cov=main/BondOrderProcessing/bond_order_processing test/