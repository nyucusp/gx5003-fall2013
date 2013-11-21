"""
Author: Christopher B. Jacoby
date: 2013/11/21
gx5003 HW5 - Assignment 5 Problem 2
"""

from readdat import read_date_file
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

def get_distances(data):
    """ Computes the time difference between each date and each deadline.
    Returns a numpy array of these, with the rows as each sample and the columns
    as each deadline. """
    distances = np.zeros([len(data), len(deadlines.keys())], dtype=int)

    # for every entry
    for index in xrange(len(data)):
        # compute the time difference, and enter it into the matrix (in seconds.)
        for deadline in deadlines.keys():
            distance = (data[index] - deadlines[deadline]).total_seconds()
            distances[index, int(deadline)] = distance

    return distances


def main():
    """ main function """
    print "Reading Input."
    file_data = read_date_file('actions-fall-2007.dat')
    date_data = [datetime.strptime(x.strip(), '%Y-%m-%d %H:%M:%S') for x in file_data]

    date_range = get_data_range(date_data)
    print "Range:", date_range

    print "Computing distances"
    # Get distances from each deadline to each point.
    deadline_distances = get_distances(date_data)
    print deadline_distances[0:10]



if __name__ == "__main__":
    main()
