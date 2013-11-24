import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter
import pandas as pd
from numpy import polyfit, polyval
import itertools

#Set pylab formatting parameters
import pylab
params = {'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 13,
          'xtick.labelsize': 9,
          'ytick.labelsize': 9,
          'text.usetex': True, 
          'font.family': 'serif',
          'font.serif': ['Palatino'],
          'xtick.direction': 'out'}
pylab.rcParams.update(params)


# ANALYSIS --------------------------------------------------------

# Due to the resulting charts, it is fairly obvious that A is best
# correlated with C, less correlated with D, and probably not
# correlated with B.


# Set up data ------------------------------------------------------

# Input data into pandas dataframe
genes_df = pd.read_table('genes.dat', sep=',')

# Create list of gene combinations
gene_combs = itertools.product('ABCD', repeat=2)



# Plot gene combinations --------------------------------------------

# Set up subplots
fig, axarr = plt.subplots(4, 4)

# Iterate through combinations:
for comb, indx in zip(gene_combs, range(0,16)):
    
    # Set current subplot:
    x_val = indx % 4
    y_val = indx // 4
    ax = axarr[y_val, x_val]

    # Set plot title and ticks:
    ax.set_title('Gene ' + comb[1] + ' vs ' + comb[0], fontsize='11')
    ticklist = [0, 0.25, 0.5, 0.75, 1]
    ticknums = FixedLocator(ticklist)
    ax.yaxis.set_major_locator(ticknums)
    ax.xaxis.set_major_locator(ticknums)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    for label in ax.xaxis.get_ticklabels():
        label.set_rotation('30')
        label.set_position((0,0.05))
        # label.set_ha('right')
    for label in ax.yaxis.get_ticklabels():
        label.set_position((0.04, 0))
    ax.tick_params(axis='y', direction='out')

    # Set axis limits
    ax_min = -0.1
    ax_max = 1.1
    ax.set_ylim(ax_min, ax_max)
    ax.set_xlim(ax_min, ax_max)
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Plot gene expression:
    ax.plot(genes_df[comb[0]], genes_df[comb[1]], '.', color='0.35', ms=5, zorder=1)



# Regressions -----------------------------------------------------------------
y_vals = sorted(genes_df['A'])

# Regression function
def plot_regression_A(gene, y_loc, degree):
    x_vals = sorted(genes_df[gene])
    coeffs = polyfit(x_vals, y_vals, degree)
    y_fit_vals = polyval(coeffs, x_vals)
    axarr[y_loc, 0].plot(x_vals, y_fit_vals, color='r', zorder=2, linestyle='-', \
                         label='Best fit,\ndegree=' + str(degree))
    axarr[y_loc, 0].legend(loc='best', frameon=False, fontsize='xx-small', numpoints=1)

# Make regressions:
plot_regression_A('C', 2, 1)
plot_regression_A('D', 3, 3)
plot_regression_A('B', 1, 5)



# Final parameters, then save figure -------------------------------------------

fig.set_size_inches(8,8.5)
plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.suptitle('SCATTER PLOTS OF EXPRESSION OF GENES A, B, C, and D.', fontsize=14)

plt.savefig('Problem 4.png', dpi=300)
