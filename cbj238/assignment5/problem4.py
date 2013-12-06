"""
Author: Christopher B. Jacoby
date: 2013/11/21
gx5003 HW5 - Assignment 5 Problem 2
"""

from readdat import read_comma_separated_file
import matplotlib.pyplot as plt
import numpy as np

GENE_TITLE = ["A", "B", "C", "D"]


def main():
    """ main function """
    header, data = read_comma_separated_file("genes.dat")

    arr_data = np.zeros([len(data), 4])
    for x in xrange(len(data)):
        arr_data[x, 0] = float(data[x][0])
        arr_data[x, 1] = float(data[x][1])
        arr_data[x, 2] = float(data[x][2])
        arr_data[x, 3] = float(data[x][3])

    fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)

    for x in xrange(4):
        for y in xrange(4):
            ax[x, y].plot( arr_data[:, x], arr_data[:, y], '.')
            ax[x, y].margins(.1, .1)
            ax[x, y].set_title(GENE_TITLE[x] + " vs. " + GENE_TITLE[y])

    a_x = np.linspace( arr_data[:, 0].min(), arr_data[:, 0].max(), 100)

    # C is the best fit. Run a linear regression on it.
    ac_fit = np.poly1d(np.polyfit(arr_data[:, 0], arr_data[:, 2], 1))
    ac_y = ac_fit(a_x)
    ax[0, 2].plot(a_x, ac_y, '-', color='r')

    # D is the second best correllation. - cubic
    ad_fit = np.poly1d(np.polyfit(arr_data[:, 0], arr_data[:, 3], 3))
    ad_y = ad_fit(a_x)
    ax[0, 3].plot(a_x, ad_y, '-', color='r')

    # B is not really correlated at all... - order 5
    ab_fit = np.poly1d(np.polyfit(arr_data[:, 0], arr_data[:, 1], 5))
    ab_y = ab_fit(a_x)
    ax[0, 1].plot(a_x, ab_y, '-', color='r', )

    fig.tight_layout()
    fig.patch.set_facecolor('white')
    fig.suptitle('Gene Correlations', fontsize=20)
    plt.subplots_adjust(top=0.85)
    fig.savefig('problem4.png')
    plt.show()

if __name__ == "__main__":
    main()
