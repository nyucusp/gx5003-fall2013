"""
Author: Christopher B. Jacoby
date: 2013/11/21
gx5003 HW5 - Assignment 5 Problem 2
"""

from readdat import ActionFileReader
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

deadlines = {
    "0" : datetime(2007, 9, 18, 12, 00, 00),
    "1" : datetime(2007, 9, 18, 12),
    "2" : datetime(2007, 10, 4, 12),
    "3" : datetime(2007, 10, 25, 12),
    "4" : datetime(2007, 11, 27, 12),
    "5" : datetime(2007, 12, 15, 12),
    "6" : datetime(2007, 12, 11, 12)
}

def get_data_range(data):
    """ returns the timedelta difference between the start and end."""
    first = data[0]
    last = data[-1]
    return last - first

def get_dates(fileReader):
    """ gets the dates from the file as datetime objects. """
    dates = []

    for date in fileReader:
        dates.append(date)

    return dates

def get_distances(fileReader):
    """ Computes the time difference between each date and each deadline.
    Returns a numpy array of these, with the rows as each sample and the columns
    as each deadline. """
    distances = []

    # for every entry
    for date in fileReader:
        #compute the time difference, and enter it into the matrix (in seconds.)
        compare_dict = {}
        for deadline in deadlines.keys():
            compare_dict[deadline] = deadlines[deadline] - date

        distances.append(compare_dict)

    return distances


def main():
    """ main function """
    afr = ActionFileReader()

    # Read dates from file
    dates = sorted(get_dates(afr))
    dates_float = [ (x - dates[0]).total_seconds() / 3600 / 24. for x in dates]
    total_days = (dates[-1] - dates[0]).days

    fig, ax = plt.subplots()
    (n, bins, patches) = ax.hist(dates_float, total_days, histtype='stepfilled')

    deadline_float = []
    for key in sorted(deadlines.keys()):
        deadline_float.append( (deadlines[key] - dates[0]).total_seconds() / 3600 / 24. )
    ax.vlines(deadline_float, 0, max(n) * 1.02, 'r')

    ax.set_xticks(deadline_float[1:]) # skip the overlapping one at the beginning.
    xlabels = [ ("Assignment " + x) for x in sorted(deadlines.keys()[1:]) ]
    ax.set_xticklabels(xlabels, ha='right', rotation='40')

    ax.margins(.02, 0)
    ax.grid(True)
    ax.set_title("Histogram of Actions by Day with Assignment Deadline Overlay.\n")

    ax.set_xlabel('Time (Days), starting at the first action')
    ax.set_ylabel('Number of actions')

    grid_bb = ax.get_position()
    ax.set_position([grid_bb.x0, grid_bb.y0 + grid_bb.height * .1, grid_bb.width, grid_bb.height * .9])

    fig.patch.set_facecolor('white')
    plt.show()

    # print "Reading file and computing distances"
    # Get distances from each deadline to each point.
    # deadline_distances = get_distances(afr)

    # int(x['0'].seconds/3600)
    # for key in deadlines.keys():
    #     print key, deadlines[key],
    #     dates_form_deadline = np.array([ x[key].days for x in deadline_distances if x[key].days > -3])

    #     hist = np.histogram(dates_form_deadline)
    #     print hist


if __name__ == "__main__":
    main()
