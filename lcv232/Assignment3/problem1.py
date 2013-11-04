import sys
import math

input = open('input1.txt','r')
value1 = input.readlines()


loops = 0    # Setting initial value = 0 for looping. 
trip1 = int(value1[loops])

while trip1 != 0:  # Conditioning the reason when data is non-zero.
    x = value1[loops] #Letting the case start with first value


    y = 1
    counter = int(loops) +1
    Expenditure = 0 
    while y <= int(x):
        Expenditure = float(value1[counter]) + Expenditure
        counter = counter + 1
        y = y + 1

    indi_cost = round(Expenditure / float(x), 2)  # Finding the value cost per student and rounding it; assigning to variable.

    y = 1
    counter = int(loops) +1
    cost_exch = 0
    while y <= int(x):	 
        if float(value1[counter]) < indi_cost:  
            cost_exch = cost_exch + (indi_cost - float(value1[counter]))  # Exchanging costs if money spent less subtracting costs after exchange.
        counter = counter + 1
        y = y + 1


    print '%.2f' % cost_exch
    loops = loops + int(x) + 1
    trip1 = int(value1[loops])