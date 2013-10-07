#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 1, Problem 2
#Determines if a sequence if jolly or not


import sys

def main(argv):
    input = [int(i) for i in argv] # use list comprehension to convert str list to int
    for i in range(len(input)): # loop through the entire list
        jolly = abs(input[i] - input[i-1])
        #print jolly #to debug
        if jolly not in input:
            print "Not Jolly"
            return
        
    print "Jolly"


if __name__ == "__main__":
   main(sys.argv[1:])