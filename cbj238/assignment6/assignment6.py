"""
assignment6.py
author: Christopher Jacoby <cbj238@nyu.edu>
"""

import argparse, csv
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

LABELLED_DATA = "labeled_data.csv"
UNLABELLED_DATA = "unlabeled_data.csv"

def read_csv_to_dict(csvfilename):
    csv_data = []
    with open(csvfilename, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            csv_data.append(row)

    return datareader.fieldnames, csv_data

def datadict_to_nparray(keys, data):
    dataarr = np.zeros([len(data), len(keys)])
    for point_index in xrange(len(data)):
        for key_index in xrange(len(keys)):
            dataarr[point_index, key_index] = np.float( data[point_index][keys[key_index]] )
    return dataarr

def get_data():
    keys1, labelled_data = read_csv_to_dict(LABELLED_DATA)
    labelled_data_arr = datadict_to_nparray(keys1, labelled_data)

    keys2, unlabelled_data = read_csv_to_dict(UNLABELLED_DATA)
    unlabelled_data_arr = datadict_to_nparray(keys2, unlabelled_data)

    return (keys1, labelled_data_arr), (keys2, unlabelled_data_arr)

def part_a(data):
    """ Plot the data and reason about any phenomena of interest you see
    (you should report it in a short text).

    takes: n x m numpy array;
    n is the number of samples, m is the number of features (2 for this example)
    Plots the first feature against the second."""

    fig, ax = plt.subplots()

    ax.plot(data[1][:, 1], data[1][:,2], 'ko')

    ax.grid(True)
    ax.margins(.02, .02)
    ax.set_title("")
    ax.set_xlabel(data[0][1])
    ax.set_ylabel(data[0][2])

    fig.patch.set_facecolor('white')
    plt.show()


def part_b():
    """ Using the labeled dataset produce python codes that report the
    10-fold-Cross Validated RMSE and R^2 scores for OLS
    (num_incidents ~ f(population)) with polynomial models from
     1 to 5th order (e.g. for second order t ~ w_0 + w_1*x1 + w2*x^2)
      and select a model complexity (polynomial order) based on these scores.
    """
    pass

def part_c():
    """ Compute the RMSE on the whole training set (all your data) and plot it
     against the 10-fold CV average (with std error-bars) as a function of model
     complexity (y-axis RMSE, x-axis order of polynomial). What do you observe?.
    """
    pass

def part_d():
    """ Build your final OLS model (you can use as many predictor
        variables/features as you want or other external data matched by
        zip code, again be careful not to overfit) and submit your predictions
        for the number of incidents on the test data.
    """
    pass

def main():
    ld, uld = get_data()

    print "Labelled Data - \nFields: {0}\nLength: {1}".format(ld[0], len(ld[1]))
    print "\nUnlabelled Data - \nFields: {0}\nLength: {1}".format(uld[0], len(uld[1]))
    all_data = np.concatenate([ld[1][:,0:2], uld[1]])
    print "\nAll Data: \nLength: {0}".format(len(all_data))

    parser = argparse.ArgumentParser()
    parser.add_argument("--run", help="part to run, if you just want to run one.")
    args = parser.parse_args()

    if not args.run or args.run == "a":
        part_a(ld)

    if not args.run or args.run == "b":
        part_b()

    if not args.run or args.run == "c":
        part_c()

    if not args.run or args.run == "d":
        part_d()

if __name__ == "__main__":
    main()
