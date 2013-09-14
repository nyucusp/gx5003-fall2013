#A script to test a sequence of integers for being "Jolly Jumpers"
#Integers are passed in as commandline arguments when the script is invoked

import sys
import math

jollyFlag = True

argv = sys.argv #new list from sys.argv
del argv[0] #delete script name from head of argv list
argv = map(int,argv) #convert strings to int
maxValue = max(argv) - 1 #hold n-1 for test in loop

#Test each interval for absolute value greater than n-1
for i in range(len(argv) - 1): #loop through to n-1 element to test interval n-1 and n
  if (math.fabs(argv[i] - argv[i+1]) > maxValue): #true if absolute value greater than n-1
    jollyFlag = False

#Test output from loop
if (jollyFlag == True):
  print "Jolly"
else:
  print "Not jolly"