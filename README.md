# pyMayCoor

Program allows you to process Mayer bond orders **MBO** from the CPMD software (<https://github.com/CPMD-code>) output file. It is planned to add the ability of the program to work with other software output files having the ability to calculate MBO.

You can calculate from Mayer bond orders:

- coordination numbers,
- Qi units,
- Connections between atoms,
- Relation between bond order and length
- Covalence (The sum of the bond orders of a given atom. This  value is close to the valence if atom have only purely covalent bonds)

### Calculations example

![calculations](claculations.gif)

### The application also allows you to see the MBO distribution for a given chemical bond

![figs](figs.gif)

## Requirements

### Installation

- Application works fine with python 3.10. The application has not been tested on other python versions.

- Before you run app, install dependencies by pip from requirements.txt

- After installing requirements install "matplotlib" flower from kivy garden. Below cmd command:

```
  garden install garden.matplotlib
```


### Installation on windows by installer

- If you ues windows you can install app, download "pyMayCoor.zip" (find it in Releases). Unpack it and run installer "pyMayCoor.exe".

## Usage

- launching the application gui:

```
py main.py
```

- launching the application in cmd:

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

## Also you can use the library associated with this project bond_order_processing

- <https://github.com/pawelgoj/pyMayCoor/tree/master/main/BondOrderProcessing>

- [Documentation page](https://pawelgoj.github.io/pyMayCoor/bond_order_processing)

## Technologies and tools

- python 3.10
- kivy
- kivyMD
- multiprocessing
- regex
- numpy
- pytest
- player
- mypy
- yaml
- PyYAML
- pdoc
- github actions
- plyer
- matplotlib
- seaborn
- pyinstaller
- Inno Setup Compiler
- Google Fonts

## How cite 
If you would like to cite the program in your work. The information below is provided.

### Script was written by Paweł Goj and first used in: 

1.	P. Stoch, P. Goj, M. Ciecińska, P. Jeleń, A. Błachowski, A. Stoch, I. Krakowiak, Influence of aluminum on structural properties of iron-polyphosphate glasses, Ceram. Int. 46 (2020) 19146–19157. doi:10.1016/j.ceramint.2020.04.250.


