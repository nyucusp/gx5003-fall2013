"""
Author: Christopher B. Jacoby
date: 2013/11/21
gx5003 HW5 - Assignment 5 Problem 2
"""

from readdat import read_comma_separated_file
import matplotlib.pyplot as plt
import numpy as np


def main():
    """ main function """
    header, data = read_comma_separated_file("genes.dat")

    arr_data = np.zeros([len(data), 4])
    for x in xrange(len(data)):
        arr_data[x, 0] = float(data[x][0])
        arr_data[x, 1] = float(data[x][1])
        arr_data[x, 2] = float(data[x][2])
        arr_data[x, 3] = float(data[x][3])

    fig, ax = plt.subplots(4,4)

    for x in xrange(4):
        for y in xrange(4):
            ax[x,y].plot( arr_data[:, x], arr_data[:, y], 'x')

    # fig.tight_layout()
    # fig.patch.set_facecolor('white')
    # fig.savefig('problem3.png')
    plt.show()

if __name__ == "__main__":
    main()
