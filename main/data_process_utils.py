from BondOrderProcessing.bond_order_processing import input_data
from BondOrderProcessing.bond_order_processing.calculations import PairOfAtoms


def check_atoms_symbols_in_loaded_data(
        mayer_bond_orders: input_data.MayerBondOrders,
        pairs_atoms_list: list[PairOfAtoms]) -> list[str]:

    wrong_atoms_list = []
    for item in pairs_atoms_list:
        if not mayer_bond_orders.check_atom_symbol_in_MBO(item.atom_1):
            wrong_atoms_list.append(item.atom_1)
        if not mayer_bond_orders.check_atom_symbol_in_MBO(item.atom_2):
            wrong_atoms_list.append(item.atom_2)

    return wrong_atoms_list


def remove_wrong_atoms(wrong_atoms_list: list[str],
                       pairs_atoms_list: list[PairOfAtoms])\
        -> list[PairOfAtoms]:

    new = []
    for item in pairs_atoms_list:
        if item.atom_1 in wrong_atoms_list:
            continue
        elif item.atom_2 in wrong_atoms_list:
            continue
        else:
            new.append(item)

    return new
