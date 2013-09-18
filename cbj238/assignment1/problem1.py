#!/usr/bin/python
"""
Christopher Jacoby
cbj238@nyu.edu
GX-5003
Problem 1

Solution for problem defined at: http://www.programming-challenges.com/pg.php?page=downloadproblem&format=html&probid=110101
"""

import sys

class InputError(Exception):
    ''' Class for handling exceptions with output '''
    def __init__(self, msg):
        self.msg = msg

def parse_input(strIn):
    # This is (ideally...) a list of 2 integers as a string. Make it a list of ints.
    intInput = [int(x) for x in strIn]

    # make sure all the inputs are in range.
    if ([(x > 0 and x < 1000000) for x in intInput]).count(True) == len(intInput):
        return intInput
    else:
        raise InputError('Inputs out of range')

def run_algorithm(n):
    """
    Return the cycle-length of n, for the 3n+1 algorithm:
    even: divide n by 2
    odd: n*3 + 1

    Loop until n = 1
    """

    cycle_length = 0
    
    while n != 1:
        if n%2==0:
            n /= 2
        else:
            n = ( (n * 3) + 1)
        cycle_length += 1

    # add one for when n==1
    cycle_length += 1

    return cycle_length

def main(args):
    try:
        (i, j) = parse_input(args)

        # Print the input.
        print i, j,

        # Keep track of all of the results.
        cycleLengths = []
        for n in xrange(i, j):
            # run the algorithm for each number between the two entered.
            cycleLengths.append(run_algorithm(n))
        # print only the max.
        print max(cycleLengths)

    except InputError as e:
        print "Input Error: {0}".format(e.msg)
    except ValueError:
        print "Invalid input! Try again..."

if __name__ == "__main__":
    main(sys.argv[1:])
