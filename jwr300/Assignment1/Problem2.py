#!/usr/local/bin/python

import sys

def main(argv):
    input = [int(i) for i in argv] # use list comprehension to convert str list to int
    for i in range(len(input)): # loop through the entire list
        jolly = abs(input[i] - input[i-1])
        if jolly not in input:
            print "Not Jolly"
            return
        
    print "Jolly"


if __name__ == "__main__":
   main(sys.argv[1:])