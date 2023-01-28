from input_data import MayerBondOrders


class Histogram:
    numbers_of_bars: int = 0
    mayer_bond_orders: MayerBondOrders | None = None

    def __init__(self, numbers_of_bars: int = 0,
                 mayer_bond_orders: MayerBondOrders = None) -> None:
        self.mayer_bond_orders = mayer_bond_orders
        self.numbers_of_bars = numbers_of_bars

    def calculate_histogram(atom_symbol_1: str, atom_symbol_2: str)\
            -> tuple(list(float), list(int)):
        # TODO
        pass
    
    def get_mayer_bond_orders_list_of_atoms()
