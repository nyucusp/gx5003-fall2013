#Aliya Merali
#Assignment 3
#Problem 1: The Trip

import sys

#Set the starting values to loop through the input
cycle = 1
cycleVal = int(sys.argv[cycle])

#While the value of the input integer is not zero, cycle through the input
while cycleVal != 0:
    n = sys.argv[cycle] #the no. of students = first value

    count = 1
    index = int(cycle) + 1 
    totalSpent = 0 
    while count <= int(n): #Cycle through the input for this trip - adding the money each student spent
        totalSpent = float(sys.argv[index]) + totalSpent
        index = index + 1
        count = count + 1

    costPer = round(totalSpent / float(n), 2)  #Calculate the cost/student

    count = 1
    index = int(cycle) + 1
    exchange = 0
    while count <= int(n): #if a student spent < cost/student, they must exchange cost/student - their costs.
        if float(sys.argv[index]) < costPer:  
            exchange = exchange + (costPer - float(sys.argv[index]))
        index = index + 1
        count = count + 1

    print '%.2f' % exchange
    cycle = cycle + int(n) + 1
    cycleVal = int(sys.argv[cycle])
    
