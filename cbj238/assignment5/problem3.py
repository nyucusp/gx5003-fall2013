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
    header, data = read_comma_separated_file("microprocessors.dat")

    data_processor = [x[0] for x in data]
    data_year = np.array([int(x[1]) for x in data])
    data_transistors = np.array([int(x[2]) for x in data])

    year_dict = dict(zip(data_year, data_processor))
    transistor_dict = dict(zip(data_processor, data_transistors))

    y = np.arange(len(data_processor))
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.plot(sorted(year_dict.keys()), y, 'ko')
    xtick_labels = [ year_dict[x] for x in sorted(year_dict.keys()) ]

    ax1.set_yticks( y )
    ax1.set_yticklabels(xtick_labels)
    ax2.set_yticklabels([])

    ordered_transistor_data = np.array([ transistor_dict[year_dict[x]] for x in sorted(year_dict.keys()) ])
    ax2.plot(ordered_transistor_data, y, 'ko')
    ax2.set_yticks( y )
    ax2.set_xscale('log')
    ax2.set_xlim( min(ordered_transistor_data) * .5, max(ordered_transistor_data) * 1.5 )

    ax1.margins(.05, .1)
    ax2.margins(0, .1)
    ax1.grid(True)
    ax2.grid(True, which='both')
    ax1.tick_params(direction='out')
    ax2.tick_params(direction='out', which="both")
    ax1.set_title("Processor Year Released")
    ax2.set_title("Processor Transistors")
    ax1.set_xlabel('Year')
    ax2.set_xlabel('Number of Transistors')

    # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    fig.tight_layout()
    fig.patch.set_facecolor('white')
    # fig.savefig('problem3.png')
    plt.show()

if __name__ == "__main__":
    main()
