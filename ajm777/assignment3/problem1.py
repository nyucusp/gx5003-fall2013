#Aliya Merali
#Assignment 3
#Problem 1: The Trip

input = open('input1.txt','r')
data = input.readlines()

#Set the starting values to loop through the input
cycle = 0
cycleVal = int(data[cycle])

#While the value of the input integer is not zero, cycle through the input
while cycleVal != 0:
    n = data[cycle] #the no. of students = first value

    count = 1
    index = int(cycle) +1
    totalSpent = 0 
    while count <= int(n): #Cycle through the input for this trip - adding the money each student spent
        totalSpent = float(data[index]) + totalSpent
        index = index + 1
        count = count + 1

    costPer = round(totalSpent / float(n), 2)  #Calculate the cost/student

    count = 1
    index = int(cycle) +1
    exchange = 0
    while count <= int(n): #if a student spent < cost/student, they must exchange cost/student - their costs.
        if float(data[index]) < costPer:  
            exchange = exchange + (costPer - float(data[index]))
        index = index + 1
        count = count + 1

    print '%.2f' % exchange
    cycle = cycle + int(n) + 1
    cycleVal = int(data[cycle])
    
