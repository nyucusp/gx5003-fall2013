#!/usr/bin/python
"""
Christopher Jacoby
cbj238@nyu.edu
GX-5003
Assignment 1 problem 2

Solution for problem defined at: http://www.programming-challenges.com/pg.php?page=downloadproblem&format=html&probid=110201
"""

import sys

class InputError(Exception):
    def __init__(self, msg):
        self.msg = msg

def parse_input(strIn):
    # Should be a list of integers.
    if len(strIn) > 1:
        n = int(strIn[0])
        if n >= 3000 or n < 1:
            raise InputError("Bad n")

        if len(strIn[1:]) != n:
            raise InputError("n not equal to number of input")

        return n, [ int(x) for x in strIn[1:] ]
    else:
        raise InputError("Not enough input.")

def isSequenceJollyJumper(n, seq):
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
        diffs = [ abs(seq[m]-seq[m-1]) for m in range(1, n) ]
        bRet = sorted(diffs) == range(1, len(seq))

    return bRet
    
def main(args):
        try:
            n, sequence = parse_input(args)
            #print n, sequence

            result = isSequenceJollyJumper(n, sequence)
            
            if result:
                print "Jolly"
            else:
                print "Not jolly"
        except InputError as e:
            print "Input Error: {0}".format(e.msg)
        except ValueError as e:
            print "Invalid input! Try again..."

if __name__ == "__main__":
    main(sys.argv[1:])
