"""
Author: Christopher B. Jacoby
date: 2013/11/21
gx5003 HW5 - Assignment 5 Problem 2

Annotations:
(a) I chose the bins to be days, starting from the first day in the actions.
    Days give a small enough resolution to see information, but not so
    tiny as to be unreadable. A finer resolution was too fine to read, and
    a larger resolution didn't provide enough information, especially
    since there are significant changes from one day to the next around
    the assignment deadlines.
(b) The 0th, first, and second assignments clearly took signifcantly less work
    than the others. Assigment 3 and 6 had by far the most, although
    it is difficult to tell how much of hte work around assignment 6
    is actually from assignment 6 and how much is from assignment 5.
    5 seems like it might not have had quite as much work.
(c) Quite obviously (and not surprisingly), most of the work is done on the
    day before and after the deadline. It looks like there is a general trend
    over the semester where more work is done before the due date
    early in the semester, and gradually less near the end of the semester.
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

    # fig.tight_layout()
    fig.patch.set_facecolor('white')
    fig.savefig('problem2.png')
    plt.show()

if __name__ == "__main__":
    main()
