#!/usr/bin/python
"""
Solution for problem defined at: http://www.programming-challenges.com/pg.php?page=downloadproblem&format=html&probid=110101
"""

def parse_input(strIn):
    return strIn.split()

def inputIsValid(i, j):
    if i > 0 and i < 1000000:
        return True
    else:
        return False

def run_algorithm(n):
    # if n is even
    if n%2==0:
        n /= 2
    else:
        n = ( (n * 3) + 1)

def main():
    strIn = raw_input("Enter a pair of integers between 0 and 1,000,000 (exclusive):")
    (i, j) = parse_input(strIn)

    if inputIsvalid(i, j):
        run_algorithm(i, j)
    else:
        print "Bad Input."

if __name__ == "__main__":
    main()
