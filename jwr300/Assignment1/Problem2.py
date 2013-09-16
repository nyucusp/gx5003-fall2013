#!/usr/local/bin/python

import sys

def main(argv):
    sequence = [int(i) for i in argv] # use list comprehension to convert string list to int
    for i in range(len(sequence)): # loop through the entire list
        jolly = abs(sequence[i] - sequence[i-1])
        if jolly not in sequence:
            print "Not Jolly"
            return
        
    print "Jolly"


if __name__ == "__main__":
   main(sys.argv[1:])