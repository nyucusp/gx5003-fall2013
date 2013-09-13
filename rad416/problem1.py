import sys

maxCycleLength = 2

def getNextNumber(n): #generates sequence
  if (n % 2 == 0): #n is even
    return (n / 2)
  else: #n is odd
    return (3 * n + 1)

for i in range(len(sys.argv)):
  if i == 1:
    rangeStart = int(sys.argv[i])
  if i == 2:
    rangeEnd = int(sys.argv[i])
  if i == 3:
      break

for i in range(rangeStart, rangeEnd):
  cycleLength = 1
  #take in start and end
  while i != 1:
    i = getNextNumber(i)
    cycleLength += 1

  #test cycleLength against maxCycleLength, replace if greater
  if (cycleLength > maxCycleLength):
    maxCycleLength = cycleLength

print rangeStart, rangeEnd, maxCycleLength



