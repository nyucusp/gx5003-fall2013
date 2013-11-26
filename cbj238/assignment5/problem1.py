"""
author: Christopher B. Jacoby
date: 2013/11/19

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
     with an explanation of the plotting principles to make a clear plot.

     "Plotting principles" used:
     * White background
     * Used margins to separate the data from the axes
     * Added a grid to make reading it easier
     * Limited to 10 ticks
     """

     # Get datetimes from the raw input
    date_vals = [datetime.strptime(x[0], '%Y-%m') for x in file_data]
    # get apple stock values from the raw input
    apple_stock_vals = [x[1] for x in file_data]

    fig, ax = plt.subplots()

    ax.plot(date_vals, apple_stock_vals, 'ko-')

    # format the ticks
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.margins(.02, .05)
    ax.autoscale_view()

    # Set the ticks to face out (Principle 3)
    ax.tick_params(direction='out')

    ax.grid(True)
    ax.set_title("Apple Stock Over Time, 2006-01 to 2009-09")
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')

    fig.patch.set_facecolor('white')
    fig.autofmt_xdate()
    fig.savefig('problem1a.png')
    plt.show()

def problem1b(file_header, file_data):
    """ (b) Using the quote of January 2006 as a baseline,
    directly compare the progress of Apple's and Microsoft's stock price
    by generating a plot using superposition (both curves in the same plot).
    Tag this final plot as "Problem 1b" and annotate it with the conclusions
     you can draw from this plot.

     Conclusions:
     I would bet that the span in here with the giant jump in Apple's stock
     correlate's to the release of the iPhone.
     Microsoft's stock is pretty steady along this entire period, with a *slight*
     boost about the same time as the iPhone is released. (Perhaps they also
        released something but it was overshadowed by the iPhone?). Apple's
    stock is pretty wild and bouncy after that release, diving again (probaby
        due to some problem discovered), and then jumping back up again
    soon after.

     """

    # Get datetimes from the raw input
    date_vals = [datetime.strptime(x[0], '%Y-%m') for x in file_data]
    # get apple stock values from the raw input
    apple_stock_vals = np.array([float(x[1]) for x in file_data])
    # Compare with the first
    apple_stock_vals = apple_stock_vals - apple_stock_vals[-1]
    microsoft_stock_vals = np.array([float(x[2]) for x in file_data])
    microsoft_stock_vals = microsoft_stock_vals - microsoft_stock_vals[-1]

    fig, ax = plt.subplots(1)

    ax.plot(date_vals, apple_stock_vals, 'ko-', label='APPL', color='r')
    ax.plot(date_vals, microsoft_stock_vals, 'ko-', label='MSFT', color='g')

    # format the ticks
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.margins(.02, .05)
    # ax.autoscale_view()

    # Set the ticks to face out (Principle 3)
    ax.tick_params(direction='out')

    ax.grid(True)
    ax.set_title("Apple vs. Microsoft Stock, 2006-01 to 2009-09")
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price Delta From 2006-01')
    ax.legend(loc='upper left')

    fig.patch.set_facecolor('white')
    fig.autofmt_xdate()
    fig.savefig('problem1b.png')
    plt.show()

def problem1c(file_header, file_data):
    """ (c) Repeat item b, but now using juxtaposition:
    split the two curves (i.e. Apple's stock price relative to January 2006
     and Microsoft's stock price relative to January 2006) into two different plots.
    Tag the final version as "Problem 1c" and annotate it describing
    which technique (superpostion vs. juxtaposition)
    makes more sense for this data and why.

    Conclusions. 1b is a better comparison of the data here; the juxtoposition
    does not succesfully give a sense of scale, nor how the data moves together.
    This plot emphasizes the movement of the Microsoft stock in a way that the
    other does not, in a perceptually confusing way.
    """

    # Get datetimes from the raw input
    date_vals = [datetime.strptime(x[0], '%Y-%m') for x in file_data]
    # get apple stock values from the raw input
    apple_stock_vals = np.array([float(x[1]) for x in file_data])
    # Compare with the first
    apple_stock_vals = apple_stock_vals - apple_stock_vals[-1]
    microsoft_stock_vals = np.array([float(x[2]) for x in file_data])
    microsoft_stock_vals = microsoft_stock_vals - microsoft_stock_vals[-1]

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.plot(date_vals, apple_stock_vals, 'ko-')
    ax2.plot(date_vals, microsoft_stock_vals, 'ko-')

    # format the ticks
    ax1.xaxis.set_major_locator(locator)
    ax1.xaxis.set_major_formatter(yearsFmt)
    ax1.margins(.02, .05)
    ax1.autoscale_view()
    ax2.xaxis.set_major_locator(locator)
    ax2.xaxis.set_major_formatter(yearsFmt)
    ax2.margins(.02, .05)
    ax2.autoscale_view()

    # Set the ticks to face out (Principle 3)
    ax1.tick_params(direction='out')
    ax2.tick_params(direction='out')

    ax1.grid(True)
    ax2.grid(True)
    ax1.set_title("Apple Stock, 2006-01 to 2009-09")
    ax2.set_title("Microsoft Stock")
    ax2.set_xlabel('Date')
    ax1.set_ylabel('Stock Price Delta \nFrom 2006-01')
    ax2.set_ylabel('Stock Price Delta \nFrom 2006-01')

    fig.patch.set_facecolor('white')
    fig.autofmt_xdate()
    fig.savefig('problem1c.png')
    plt.show()

def main():
    """ main function """
    file_header, file_data = read_comma_separated_file('stocks.dat')

    problem1a(file_header, file_data)
    problem1b(file_header, file_data)
    problem1c(file_header, file_data)

if __name__ == "__main__":
    main()
