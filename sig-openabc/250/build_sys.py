# load packages
import numpy as np
import pandas as pd
import sys
import os
try:
    import openmm as mm
    import openmm.app as app
    import openmm.unit as unit
except ImportError:
    import simtk.openmm as mm
    import simtk.openmm.app as app
    import simtk.unit as unit

import mdtraj
try:
    import nglview
except ImportError:
    print('Please install nglview to visualize molecules in the jupyter notebooks.')

sys.path.append('../../')
from openabc.forcefields.parsers import HPSParser
from openabc.forcefields import HPSModel
from openabc.utils.helper_functions import build_straight_CA_chain, write_pdb
from openabc.utils.insert import insert_molecules

# set simulation platform
platform_name = 'GPU'

sequence = 'MGDEDWEAEINPHMSSYVPIFEKDKYSGENGDNFNKTPASSSEMDDGPSKKDHFMKSGFASGKNFGNKDAGECNKKDNTSTMGGFGVGKSFGNKGFSNSKFEDGDSSGFWKESSNDCEDNPTKNKGFSKKGGYKDGNNSEASGPYKKGGKGSFKGCKGGFGLGSPNNDLDPDECMQKTGGLFGSKKPVLSGTGNGDTSQSKSGSGSEKGGYKGLNEEVITGSGKNSWKSEAEGGES'
ca_pdb = 'init_DDX4_R2K_CA.pdb'
ca_atoms = build_straight_CA_chain(sequence, r0=0.38)
write_pdb(ca_atoms, ca_pdb)
protein_parser = HPSParser(ca_pdb)

# insert molecules into the simulation box randomly
n_mol = 100
if not os.path.exists('start.pdb'):
    insert_molecules(ca_pdb, 'start.pdb', n_mol, box=[100, 100, 100])


protein = HPSModel()
for i in range(n_mol):
    protein.append_mol(protein_parser)
top = app.PDBFile('start.pdb').getTopology()
init_coord = app.PDBFile('start.pdb').getPositions()
protein.create_system(top, box_a=100, box_b=100, box_c=100)
protein.add_protein_bonds(force_group=1)
protein.add_contacts('Urry', mu=1, delta=0.08, force_group=2)
protein.dh_elec_dist_openabc()
protein.save_system('system.xml')