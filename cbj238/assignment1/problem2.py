#!/usr/bin/python
"""
Christopher Jacoby
cbj238@nyu.edu
GX-5003
Assignment 1 problem 2

Solution for problem defined at: http://www.programming-challenges.com/pg.php?page=downloadproblem&format=html&probid=110201
"""

import sys

def parse_input(strIn):
    # Should be a list of integers.
    if len(strIn) > 0:
        return [int(x) for x in strIn]
    else:
        raise ValueError()

def inputIsValid(inList):
    # a is a temp; make sure all items in list are < 3000
    a = [ x < 3000 for x in inList ]
    return ( a.count(True) == len(a) )

def isSequenceJollyJumper(seq):
    """
    For sequence of n > 0 integers,
    if the abs of the differences between successive elements take on all possible values
     of 1 through n - 1
    Any sequence of a single integer is a jolly jumper
    """
    bRet = False
    if len(seq) == 1:
        bRet = True
    elif len(seq) > 1:
        diffs = [ abs(seq[n]-seq[n-1]) for n in range(1, len(seq)) ]
        bRet = sorted(diffs) == range(1, len(seq))

    return bRet
    
def main(args):
        try:
            sequence = parse_input(args)

            # If the input is in a valid range...
            if inputIsValid(sequence):
                result = isSequenceJollyJumper(sequence)
                if result:
                    print "Jolly"
                else:
                    print "Not jolly"
            else:
                raise ValueError()
        except ValueError:
            print "Invalid input! Try again..."

if __name__ == "__main__":
    main(sys.argv[1:])
