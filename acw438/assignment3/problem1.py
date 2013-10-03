#Alex Chohlas-Wood. Assignment 3, Problem 1.

rawFile = open('input1.txt', 'r')
input1 = []
for line in rawFile:
    input1.append(line.strip())

#General index for where we are in the inputted list:
#While our general index is less than the length of the list:
#Get number of people on this trip (string of item in input1):
#Put personal expenses into a temporary list:
#Find mean of list (floats of items in input1):
#Loop through list and accumulate distances from mean:
#Round to nearest cent:
#Return total distances from mean (total money exchanged):

print input1
rawFile.close()
