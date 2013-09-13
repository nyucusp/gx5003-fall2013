# input any two numbers between 0 and 1,000,000, 
# Given any two numbers i and j, you are to determine the maximum cycle length over all numbers between i and j, including both endpoints.
# Input

# The input will consist of a series of pairs of integers i and j, one pair of integers per line. All integers will be less than 1,000,000 and greater than 0.
# Output

# For each pair of input integers i and j, output i, j in the same order in which they appeared in the input and then the maximum cycle length for integers between and including i and j. These three numbers should be separated by one space, with all three numbers on one line and with one line of output for each line of input.

#initialize and declare variables
# int maxCycleLength = 0
cycleCount = 1
n = 22

def getNextNumber(n):
  if (n%2 == 0): #n is even
    return (n / 2)
  else: #n is odd
    return (3 * n + 1)


#take in start and end
while n != 1:
  n=getNextNumber(n)
  cycleCount += 1

print(cycleCount)
#generate sequence
  #test even
  #test odd
#count sequence
  #return cycle length

# def argparse(argv):
#     for i in range(len(argv)):
#         if i==1:
#             if(vetdeploymentname(argv[i]))==argv[i]:
#                 deploymentnamelist=[argv[i]]
#         if i==2:
#             if(vetdate(argv[i]))==argv[i]:
#                 startdate=argv[i]
#         if i==3:
#             if(vetdate(argv[i]))==argv[i]:
#                 enddate=argv[i]
#         if i>3:
#             break


