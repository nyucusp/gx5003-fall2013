# A script to calculate maximum cycle length of the 3n+1 problem in a range
# The start of the range is the first argument and
# the end of the range is the second argument

import sys

maxCycleLength = 2 #max length value

def getNextNumber(n): #generates sequence
  if (n % 2 == 0): #n is even
    return (n / 2)
  else: #n is odd
    return (3 * n + 1)

#extract commandline arguments
for i in range(len(sys.argv)):
  if i == 1:
    rangeStart = int(sys.argv[i])
  if i == 2:
    rangeEnd = int(sys.argv[i])
  if i == 3:
      break

#for loop to generate cycles and calculate max length
for i in range(rangeStart, rangeEnd):
  cycleLength = 1
  while i != 1:
    i = getNextNumber(i)
    cycleLength += 1

  #test cycleLength against maxCycleLength, replace if greater
  if (cycleLength > maxCycleLength):
    maxCycleLength = cycleLength

print rangeStart, rangeEnd, maxCycleLength



