import sys

cycleMaxLength = 0              # set maximum cycle length

def newValue(n): 
    if (n % 2 == 0):            # if n is even
        return (n / 2)          # divide by 2
    else:                       # else n is odd
        return ((3 * n) + 1)    # multiply by 3 and add 1

for i in range(len(sys.argv)):
    if i == 1:
        rangeMin = int(sys.argv[i])
    if i == 2:
        rangeMax = int(sys.argv[i])
    if i == 3:
        break

for i in range(rangeMin, rangeMax):     # calculate maximum cycle length
    cycleLength = 1
    while i != 1:
        i = newValue(i)
        cycleLength += 1
    
    if (cycleLength > cycleMaxLength):
        cycleMaxLength = cycleLength

<<<<<<< HEAD
print rangeMin, rangeMax, cycleMaxLength
=======
print rangeMin, rangeMax, cycleMaxLength
>>>>>>> d6f40eeb85f30f87d7da17a58e366c13cf23b728
