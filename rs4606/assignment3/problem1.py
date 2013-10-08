import sys


"""
First we open the text file and save the lines to the list input_lines
"""


inputfile = open('input1.txt', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()

"""
This function will take a list of floats as input, which are the costs incurred by
each member of a trip.  It will print the minimum amount of money that needs to change
hands.  Let avg be the the average of the elements of cost_list, then the amount to be
printed is clearly the sum of the differences between avg and and those items of 
cost_list less than avg.  Note that we round to the nearest cent at the stage when we 
compute the difference between avg and an item below avg.
"""

def print_min_money(cost_list):
    avg = sum(cost_list)/len(cost_list)
    min_money = 0.00
    for elt in cost_list:
        if elt <= avg:
            min_money += round((avg - elt), 2)
    return min_money
  

"""
Now we go through input_lines.  When we find an integer n, we feed print_min_money the 
list consisting of the next n elements of input_lines, converted to floats, and print
the result.  We ignore the integer 0 appearing at the end of the input file, and we
append a 0 to the end of the result of print_min_money if the result has only one 
decimal place displayed (for example, if print_min_money returns 10.0, we append a 0
to get the output 10.00).
"""


for i in range(0,len(input_lines)):
    if input_lines[i].find(".") == -1:
        current_trip = []
        for j in range(i+1, i+int(input_lines[i])+1):
            current_trip.append(float(input_lines[j]))
        if len(current_trip) > 0:
            if len(str(print_min_money(current_trip) - int(print_min_money(current_trip)))) > 3:
                print print_min_money(current_trip)
            else: 
                print str(print_min_money(current_trip)) + "0"