import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
from matplotlib.ticker import MultipleLocator
import pandas as pd



#Set pylab formatting parameters
import pylab
params = {'axes.labelsize': 13,
          'text.fontsize': 13,
          'legend.fontsize': 13,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12,
          'text.usetex': True, 
          'font.family': 'serif',
          'font.serif': ['Palatino']}
pylab.rcParams.update(params)



#Input data into pandas dataframe
stocks_df = pd.read_table('stocks.dat', sep=',')
stocks_df['month'] = pd.to_datetime(stocks_df['month'])



#Create formatting functions:

def addgrid_removespines(axes):
    # Remove top & right spines
    axes.spines['top'].set_visible(False)
    axes.xaxis.set_ticks_position('bottom')
    axes.spines['right'].set_visible(False)
    axes.yaxis.set_ticks_position('left')

    # Add grid
    axes.grid(which='both', color='0.65', linestyle=':')
    axes.set_axisbelow(True)

def add_labels(titl, ylab, xlab, axes, showlegend):
    # Add labels
    t = axes.set_title(titl)
    t.set_y(1.03)
    axes.set_ylabel(ylab)
    axes.set_xlabel(xlab)
    top_height = 0.95-float(len(titl.splitlines()))/20
    plt.subplots_adjust(left=.11, top=top_height, right=.95, bottom=.13)
    if showlegend:
        axes.legend(loc=2,frameon=False)


# Problem 1a --------------------------------------------------------------

    # I have limited the number of ticks to a minimal amount, 
    # so as to make the data more obvious.

    # I set the axis limits to give the data a little breathing room,
    # and allowed the data to be shown at a roughly 45 degree angle

    # I added an unobtrusive grid, which helps locate points in time and value.
    # I also removed top and right spines, which are distracting.

    # (I added these annotations to the plot itself)

def problem1a():
    fig, ax = plt.subplots()

    #Plot data
    ax.plot_date(stocks_df['month'], stocks_df['apple'], '.', ms=8, \
                 c='0.35', linestyle='--', dashes=(3,2) )


    # Format x-ticks
    years = YearLocator()
    six_months = MonthLocator(bymonth=(1, 7))
    month_format = DateFormatter('%b %Y')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(month_format)
    ax.xaxis.set_minor_locator(six_months)

    # Format y-ticks
    fourties = MultipleLocator(50)
    ax.yaxis.set_major_locator(fourties)


    # Set axis limits
    xmin = pd.to_datetime('2005-10-02')
    xmax = pd.to_datetime('2008-10-30')
    ax.set_xlim(xmin, xmax)
    ymin = stocks_df['apple'].min()*0.7
    ymax = stocks_df['apple'].max()*1.1
    ax.set_ylim(ymin, ymax)


    # Make annotations
    bbox_style = dict(boxstyle = 'round,pad=0.3', fc = '0.85', ec='none', alpha = 0.5)
    arrow_style = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0')
    ax.annotate('Few ticks', \
                xy=(pd.to_datetime('2007-01-01'), ymin), \
                xytext=(25, 30), textcoords='offset points', \
                bbox = bbox_style, arrowprops = arrow_style)
    ax.annotate('No top or right spines', \
                xy=(xmax, 75), \
                xytext=(-100, -30), textcoords='offset points', \
                bbox = bbox_style, arrowprops = arrow_style)
    ax.annotate('Unobtrusive gridlines', \
                xy=(pd.to_datetime('2007-01-01'), 150), \
                xytext=(-50, 30), textcoords='offset points', \
                bbox = bbox_style, arrowprops = arrow_style)
    ax.annotate('Small dashes, \n Approx. 45 degree overall rise', \
                xy=(pd.to_datetime('2007-04-15'), 110), \
                xytext=(25, -30), textcoords='offset points', \
                bbox = bbox_style, arrowprops = arrow_style)


    # Add formatting
    addgrid_removespines(ax)
    add_labels('Apple stock price, Jan. 2006 - Sep. 2008', 'US DOLLARS', 'MONTH', ax, False)

    # Save and close figure
    plt.savefig('Problem 1a.png', dpi=300)
    print "Problem 1a saved."
    plt.clf()

problem1a()



#Reformat data for remaining two graphs:
stocks_df['apple'] = stocks_df['apple'] - stocks_df['apple'][len(stocks_df)-1]
stocks_df['microsoft'] = stocks_df['microsoft'] - stocks_df['microsoft'][len(stocks_df)-1]    



#Problem 1b --------------------------------------------------------------

# I take from the graph that Microsoft's stock price hovered around
# its January 2006 price during the time period shown on the graph.
# Apple's stock price had largely the same behavior until early 2007,
# but then added ~$75 over the remaining timespan shown in the
# graph. This rise was possibly due to the iPhone's launch in early
# 2007.

def problem1b():
    fig, ax = plt.subplots()

    #Plot data
    ax.plot_date(stocks_df['month'], stocks_df['apple'], '.', ms=8, \
                 c='#E41A1C', linestyle='--', dashes=(3,2), alpha=0.7, \
                 label="Apple stock prices")
    ax.plot_date(stocks_df['month'], stocks_df['microsoft'], '.', ms=8, \
                 c='#377EB8', linestyle='--', dashes=(3,2), alpha=0.7, \
                 label="Microsoft stock prices")

    # Format x-ticks
    years = YearLocator()
    six_months = MonthLocator(bymonth=(1, 7))
    month_format = DateFormatter('%b %Y')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(month_format)
    ax.xaxis.set_minor_locator(six_months)

    # Format y-ticks
    fourties = MultipleLocator(50)
    ax.yaxis.set_major_locator(fourties)


    # Set axis limits
    xmin = pd.to_datetime('2005-10-02')
    xmax = pd.to_datetime('2008-10-30')
    ax.set_xlim(xmin, xmax)
    ymin = stocks_df['apple'].min()*1.5
    ymax = stocks_df['apple'].max()*1.1
    ax.set_ylim(ymin, ymax)

    # Add formatting
    addgrid_removespines(ax)
    add_labels('Apple and Microsoft stock prices, Jan. 2006 - Sep. 2008, \n indexed to Jan. 2006 price', 'US DOLLARS', 'MONTH', ax, True)

    # Save and close figure
    plt.savefig('Problem 1b.png', dpi=300)
    print "Problem 1b saved."
    plt.clf()

problem1b()



#Problem 1c --------------------------------------------------------------

# I would personally prefer the superposition technique over
# juxtaposition. But it really depends on the purpose of the
# exercise. Here I assume that our purpose is to compare how the two
# stock prices changed over time to see which company gained or lost
# more over the same time period. Clearly, either method shows that
# Apple has gained more, but by juxtaposing the graphs we can't see
# that they acted roughly the same way until April 2007 -- or at least
# this comparison is a lot harder.

# If the purpose was to understand how each company's stock price
# changed over time, but NOT compare them, it would make more sense to
# use juxtaposition, and possibly to rescale the Microsoft graph to a
# smaller vertical scale.

def problem1c():
    fig, axarr = plt.subplots(1, 2, sharey = False)
    fig.set_size_inches(10,5)

    #Plot data
    axarr[0].plot_date(stocks_df['month'], stocks_df['apple'], '.', ms=8, \
                 c='#E41A1C', linestyle='--', dashes=(3,2), alpha=0.7, \
                 label="Apple stock prices")
    axarr[1].plot_date(stocks_df['month'], stocks_df['microsoft'], '.', ms=8, \
                 c='#377EB8', linestyle='--', dashes=(3,2), alpha=0.7, \
                 label="Microsoft stock prices")

    # Format x-ticks
    years = YearLocator()
    six_months = MonthLocator(bymonth=(1, 7))
    month_format = DateFormatter('%b %Y')

    # Format y-ticks
    fourties = MultipleLocator(50)
    axarr[0].yaxis.set_major_locator(fourties)
    axarr[1].yaxis.set_major_locator(fourties)

    # Set axis limits
    xmin = pd.to_datetime('2005-10-02')
    xmax = pd.to_datetime('2008-10-30')
    ymin = stocks_df['apple'].min()*1.5
    ymax = stocks_df['apple'].max()*1.1
    for ax in axarr:
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(month_format)
        ax.xaxis.set_minor_locator(six_months)
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        addgrid_removespines(ax)
        handles, labels = ax.get_legend_handles_labels()
        add_labels(labels[0] + ', Jan. 2006 - Sep. 2008, \n indexed to Jan. 2006 price', \
                   'US DOLLARS', 'MONTH', ax, False)
        
    plt.savefig('Problem 1c.png', dpi=300)
    print "Problem 1c saved."
    plt.clf()

problem1c()
