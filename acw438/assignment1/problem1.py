#Alex Chohlas-Wood (acw438). Assignment 1, Problem 1.

import sys
inputRange = map(int,sys.argv[1:]) #map input to list of integers

longest = 0 #record for longest iteration length

for x in range(inputRange[0], inputRange[1]+1):
    target = x #integer in range to run iteration on
    counter = 1 
    while target > 1:
        if target%2 == 0:
            target /= 2
        else:
            target *= 3
            target += 1
        counter += 1
        if target == 1:
            if counter > longest:
                longest = counter

print inputRange[0], inputRange[1], longest
