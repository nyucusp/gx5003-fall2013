# Awais Malik
# Assignment 1
# Problem 1

import sys

first = int(sys.argv[1])
last = int(sys.argv[2])

# Function for creating 3n+1 chain and return length of chain
def collatz(n):
    array = []
    while n > 1:
        array.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n *= 3
            n += 1
    if n == 1:
        array.append(1)
        # print array
        return len(array)
    elif n < 1:
        print "Please type a positive integer!"
    else:
        print "Invalid input."        

# Function to measure max length of chain in given range
def user_collatz(a, b):
    max_length = collatz(a)
    for i in range(a,b+1):
        if max_length < collatz(i):
            max_length = collatz(i)
    print a, b, max_length

user_collatz(first, last)