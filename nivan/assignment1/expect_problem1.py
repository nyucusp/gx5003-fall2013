import sys 

firstParam  = int(sys.argv[1])
secondParam = int(sys.argv[2])
longest = -1

for x in xrange(firstParam, secondParam+1):
    counter = 1 
    target = x
    while target > 1: 
        #print target
        if target%2 == 0: 
            target /= 2 
        else: 
            target = 3*target + 1 
        counter += 1 
    if longest < counter:
        longest = counter

print firstParam, secondParam, longest
