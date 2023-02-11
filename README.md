# pyMayCoor

Program allows you to process Mayer bond orders from the CPMD output file. 


You can calculate from Mayer bond orders:

- coordinations numbers,
- Qi units,
- Connections between atoms,
- Relation between bond order and length

Work in progress, program is not full functional yet.🔨

![program](program.png)

## At the moment only the cli interface is available

Run App by:

```
py main.py -i <input_file_from_CPMD> -s <settings.yaml> -o <output_file>
```

Command flags:

`-i` - set path to input file

`-s` - set path to settings file

`-o` - set path for output file


### Example of settings file

Settings file is in yaml format. You can specify what calculations you want to perform. It should also be specified for which pairs of atoms they are to be made.

```
histogram:
  calc: true
  nr_bars: 10
pairs_atoms_list:
  - atom_1: P
    atom_2: O
    mbo_min: 1.2
    mbo_max: 2
    id: P=O
  - atom_1: P
    atom_2: O
    mbo_min: 0.1
    mbo_max: INF
    id: P-O
  - atom_1: Al
    atom_2: O
    mbo_min: 0.1
    mbo_max: INF
    id: Al-O
  - atom_1: Fe
    atom_2: O
    mbo_min: 0.1
    mbo_max: INF
    id: Fe-O
calculations:
  q_i:
    calc: true
    bond_id: P-O
  cn: true
  connections: true
  bond_length: true
  covalence: true
```

## Also You can use the library associated with this project bond_order_processing

- <https://github.com/pawelgoj/pyMayCoor/tree/master/main/BondOrderProcessing>

- [Documentation page](https://pawelgoj.github.io/pyMayCoor/bond_order_processing)
