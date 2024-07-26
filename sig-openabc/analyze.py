import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])
z = df['z (nm)'] * 10
rho = df['rho (g/L)'] # g/L is equivalent to mg/mL



###
from re import X
import numpy as np, numpy.ma as ma
import os
import random
import sys
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.gridspec import GridSpec
from textwrap import wrap
from matplotlib import rc # This sometimes gives problems
import csv
from random import randint
import pandas as pd

# colors = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "magenta", "lime", "pink"]

# These are the parameters to use to get a publication quality figure.
mpl.rcParams['axes.linewidth'] = 1.2
mpl.rcParams['xtick.major.size'] = 6
mpl.rcParams['xtick.major.width'] = 1.2
mpl.rcParams['xtick.minor.size'] = 3
mpl.rcParams['xtick.minor.width'] = 1.2
mpl.rcParams['ytick.major.size'] = 6
mpl.rcParams['ytick.major.width'] = 1.2
mpl.rcParams['ytick.minor.size'] = 3
mpl.rcParams['ytick.minor.width'] = 1.2
mpl.rcParams['xtick.direction'] = 'out'
mpl.rcParams['ytick.direction'] = 'out'
mpl.rcParams['font.size'] = 10
mpl.rcParams['mathtext.default'] = 'regular'
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10
mpl.rcParams['pdf.fonttype'] = 42 # new line
mpl.rcParams['legend.frameon'] = False
legend_properties = {'weight':'bold', 'size':8}
axisl_properties = {'family':'sans-serif','sans-serif':['Helvetica'], 'weight':'bold'}
label_properties = {'weight':'normal', 'size':10}

fig = plt.figure()
fig.set_size_inches(3.25, 3.25, forward=True)
ax1 = plt.Axes(fig, [0.115384615,0.230769231,0.769230769,0.769230769])
fig.add_axes(ax1)

##

# df = pd.read_csv(input_csv)
# z = df['z (nm)']
# rho = df['rho (g/L)'] # g/L is equivalent to mg/mL

### 

ax1.plot(z, rho, markersize=2, marker='None', linestyle='solid')

# Plot Analytical derivative with error bars

angstrom_symbol = '\u212B' ## for angstrom
ax1.set_ylabel(r'Concentration (mg/ml)', fontsize=15,fontweight='bold') # x-axis label
ax1.set_xlabel(f'Z ({angstrom_symbol})',fontsize=15,fontweight='bold') # y-axis label

# ax1.set_xlim(8,18) # x-axis limit (set limit according to your data)
# ax1.set_ylim(8,20) # y-axis limit
ax1.xaxis.set_major_locator(ticker.MultipleLocator(200))   # sets major tick spacing
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(4))   # sets minor tick spacing

# ax1.set_xticklabels(ax1.get_xticks(), fontweight='bold', fontsize=10)
ax1.set_yticklabels(ax1.get_yticks(), fontweight='bold', fontsize=10)
ax1.tick_params(top=False)
ax1.tick_params(right=False)
# ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f')) # set this based on your data (fraction vs integer number)
# ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
# ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
temp = sys.argv[2]
ax1.legend(prop=legend_properties, numpoints = 1, bbox_to_anchor=(1.0, 0.98))
# ax1.set_title(f'%s' % str(title)) # if you want to add title to your figure
ax1.set_title(f'DDX4 {temp} K', fontweight='bold')
plt.yscale('log')
plt.xlim(-700, 700)
plt.show()
plt.savefig(f'pot3_{temp}.png', bbox_inches='tight', dpi=300)
