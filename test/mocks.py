class MayerBondOrders:
    """Mock class."""
    mbo = {1: {1: 0.5, 2: 0.5, 3: 0.4},
           2: {1: 0.5, 2: 0.1, 3: 0.05},
           3: {1: 0.5, 2: 0.1, 3: 0.05}}

    def get_mayer_bond_order_between_atoms(self, atom_id_1: int, atom_id_2:
                                           int) -> float:
        return self.mbo.get(atom_id_1).get(atom_id_2)

    def get_atoms_ids(self, atom_symbol_1):
        return [1, 2, 3]

    def get_all_mayer_bond_orders_of_atom(self, id):
        return [0.5, 0.5, 0.4]

    def get_mayer_bond_orders_list_between_two_atoms(self, atom_symbol_1,
                                                     atom_symbol_2):
        return [0.05, 0.10, 0.2, 0.50, 0.7, 1.2, 1.0, 0.8, 0.1, 0.5]
