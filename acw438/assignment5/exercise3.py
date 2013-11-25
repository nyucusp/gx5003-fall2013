import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter
from matplotlib.dates import date2num, YearLocator, DateFormatter
from matplotlib.patches import ConnectionPatch
import pandas as pd

#Set pylab formatting parameters
import pylab
params = {'axes.labelsize': 13,
          'text.fontsize': 10,
          'legend.fontsize': 13,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12,
          'text.usetex': True, 
          'font.family': 'serif',
          'font.serif': ['Palatino'],
          'xtick.direction': 'out'}
pylab.rcParams.update(params)

# Input data into pandas dataframe, convert, and sort
mp_df = pd.read_table('microprocessors.dat', sep=',')
mp_df['Year of Introduction'] = mp_df['Year of Introduction'].astype(str) + "-01-01"
mp_df['Year of Introduction'] = pd.to_datetime(mp_df['Year of Introduction'])
mp_df.sort(['Year of Introduction'], ascending=True, inplace=True)
mp_df = mp_df.reset_index(drop=False)

# Get rid of dangling p's in redundant 'processor' (messes up va of tickmarks)
mp_df['Processor'] = mp_df['Processor'].map(lambda x: x.rstrip(' processor'))

# Create repetitive functions:
def formatting(axes, titl):
    # Set y-axis labels
    ticklist = range(1,14)
    ticknums = FixedLocator(ticklist)
    axes.yaxis.set_major_locator(ticknums)
    ticknames = FixedFormatter(mp_df['Processor'])
    axes.yaxis.set_major_formatter(ticknames)

    # Set y-axis limits
    ymin = 0
    ymax = 14
    axes.set_ylim(ymin, ymax)

    # Remove top and right spines
    axes.spines['top'].set_visible(False)
    axes.xaxis.set_ticks_position('bottom')
    axes.spines['right'].set_visible(False)
    axes.spines['left'].set_visible(False)
    axes.yaxis.set_ticks_position('none')

    # Set title
    t = axes.set_title(titl)
    t.set_y(1.03)
    plt.subplots_adjust(top=0.9)

# Set parameters
fig, (ax1, ax2) = plt.subplots(1, 2, sharey = True)
yr_list = [1+x for x in range(0,13)]

def first_graph():
    # Set axis limits
    xmin = mp_df['Year of Introduction'].min() - pd.DateOffset(months=15)
    xmax = mp_df['Year of Introduction'].max() + pd.DateOffset(months=12)
    ax1.set_xlim(xmin, xmax)
    # Format x-ticks
    year = YearLocator(10)
    year_format = DateFormatter('%Y')
    ax1.xaxis.set_major_locator(year)
    ax1.xaxis.set_major_formatter(year_format)

    # Plot first graph
    ax1.plot(mp_df['Year of Introduction'], yr_list, '.', color='0.35', ms=12, zorder=1)

    formatting(ax1, 'Processor release year')

def second_graph():
    # Set axis limits:
    ax2.set_xscale('log')

    # Plot second graph
    ax2.plot(mp_df['Transistors'], yr_list, '.', color='0.35', ms=12, zorder=1)

    formatting(ax2, 'Processor transistor count')

first_graph()
second_graph()

# Create horizontal lines across subplots
line_list = range(1,14)

for y in line_list:
    ax1.axhline(y=y,xmin=0,xmax=1.4,c="0.35",linewidth=1,linestyle=':',zorder=0, clip_on=False)
    ax2.axhline(y=y,xmin=0,xmax=1,c="0.35",linewidth=1,linestyle=':',zorder=0,clip_on=False)


fig.set_size_inches(14,5)

plt.savefig('Problem 3.png', facecolor='0.95', dpi=300)
