#!/usr/bin/python
"""
Christopher Jacoby
cbj238@nyu.edu
GX-5003

Solution for problem defined at: http://www.programming-challenges.com/pg.php?page=downloadproblem&format=html&probid=110101
"""

def parse_input(strIn):
    # This is (ideally...) a list of 2 integers as a string. Make it a list of ints.
    return [int(x) for x in strIn.split()]

def inputIsValid(i, j):
    # ensure the correct range.
    if (i > 0 and i < 1000000) and (j > 0 and j < 1000000):
        return True
    else:
        return False

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

def main():
    while True:
        #Initialize these for scope...
        i = 0
        j = 0

        # This is so we can loop if we recieve a ValueError
        bValidInput = False
        while not bValidInput:
            try:
                strIn = raw_input("Enter a pair of integers between 0 and 1,000,000 (exclusive):")
                (i, j) = parse_input(strIn)
                break
            except ValueError:
                print "Invalid input! Try again..."

        # Print the input.
        print i, j,

        # If the input is in a valid range...
        if inputIsValid(i, j):
            # Keep track of all of the results.
            cycleLengths = []
            for n in xrange(i, j):
                # run the algorithm for each number between the two entered.
                cycleLengths.append(run_algorithm(n))
            # print only the max.
            print max(cycleLengths)
        else:
            print "Bad Input."

if __name__ == "__main__":
    main()
