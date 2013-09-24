#Receive import in the command line
import sys

#Define seq1 as the imput sequence with n integers
n=int(sys.argv[1])
seq1=map(int,sys.argv[2:])

#Define seq2 as a new sequence of the absolute differences of seq1
seq2=list()
for i in range(0,len(seq1)-1):
    seq2.append(abs(seq1[i]-seq1[i+1]))

# Check if there are reduplicative values in seq2. Use variable "judge" as an indicator
judge=0
for i in range(0, len(seq2)):
    for j in range(i+1, len(seq2)):
        if seq2[i]==seq2[j]:
            print "Not jolly"
            judge=1

# If there are no reduplicative values in seq2 and its maximum value is equal to the n-1 then seq1 is jolly jumper           
if judge==0:
    if max(seq2)==n-1:
        print "Jolly"
    else: 
        print "Not jolly"
