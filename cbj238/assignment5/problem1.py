"""
author: Christopher B. Jacoby
date: 2013/19/11

For handling dates, I'm using
http://matplotlib.org/examples/pylab_examples/date_demo1.html
"""

from readdat import read_comma_separated_file
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter, AutoDateLocator
from datetime import datetime

# The date formating. Only 3-10 ticks allowed (Principle 3)
locator = AutoDateLocator(minticks=3, maxticks=10)
yearsFmt = DateFormatter('%Y-%m')

def problem1a(file_header, file_data):
    """ (a) generate a simple connected symbol plot for all Apple's stock quotes
     in the file stocks.dat.
    Tag the final version of this plot as "Problem 1a" and annotate it
     with an explanation of the plotting principles to make a clear plot. """

     # Get datetimes from the raw input
    date_vals = [datetime.strptime(x[0], '%Y-%m') for x in file_data]
    # get apple stock values from the raw input
    apple_stock_vals = [x[1] for x in file_data]

    fig, ax = plt.subplots()

    ax.plot_date(date_vals, apple_stock_vals, '-')

    # format the ticks
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.margins(.02, .05)
    ax.autoscale_view()

    # Set the ticks to face out (Principle 3)
    ax.tick_params(direction='out')

    ax.grid(True)
    ax.set_title("Apple Stock Over Time, 2006-01 to 2009-09")

    fig.autofmt_xdate()
    plt.show()

def problem1b(file_header, file_data):
    """ (b) Using the quote of January 2006 as a baseline,
    directly compare the progress of Apple's and Microsoft's stock price
    by generating a plot using superposition (both curves in the same plot).
    Tag this final plot as "Problem 1b" and annotate it with the conclusions
     you can draw from this plot. """
    pass

def problem1c(file_header, file_data):
    """ (c) Repeat item b, but now using juxtaposition:
    split the two curves (i.e. Apple's stock price relative to January 2006
     and Microsoft's stock price relative to January 2006) into two different plots.
    Tag the final version as "Problem 1c" and annotate it describing
    which technique (superpostion vs. juxtaposition)
    makes more sense for this data and why. """
    pass

def main():
    """ main function """
    file_header, file_data = read_comma_separated_file('stocks.dat')

    problem1a(file_header, file_data)
    problem1b(file_header, file_data)
    problem1c(file_header, file_data)

if __name__ == "__main__":
    main()
