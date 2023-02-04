"""Library for processing Mayer bond orders.

.. include:: ../readme.md .

Example:

    >>> from BondOrderCalculations.input_data import LoadedData
    >>> from BondOrderCalculations.calculations import CoordinationNumbers
    >>> from BondOrderCalculations.input_data import InputDataFromCPMD
    >>> 
    >>> path_to_input_file = r'./egzamples_instructions/out1.txt'
    >>> 
    >>> input_data = InputDataFromCPMD()
    >>> input_data.load_input_data(path_to_input_file, LoadedData.MayerBondOrders)
    >>> mayer_bond_orders = input_data.return_data(LoadedData.MayerBondOrders)
    >>>
    >>> # Calculate percentage of coordination numbers of P
    >>> coordinations_numbers_stats = CoordinationNumbers.calculate(mayer_bond_orders, 'P', 'O', 'INF', 0.2, 'P-O').calculate_statistics()
    >>> coordinations_numbers_stats.statistics
    {4: 100.0}

"""
