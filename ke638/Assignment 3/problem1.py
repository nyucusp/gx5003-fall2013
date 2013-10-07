#Katherine Elliott
#ke638
#Assignment 3 Problem 1

import re

f = open('./input1.txt', 'r')

expenses = []
student_num = 0

for line in f:
    if re.search('\.', line): # only append figures that have a '.'
        expenses.append(float(line))

    # if line is an integer calculate trip expenses
    elif(len(expenses) > 0):
        # calculate average
        avg = float( sum(expenses) / len(expenses) )

        # loop through expenses and calculate diff
        total_diff = 0
        for expense in expenses:
           if expense < avg:
                diff = avg - expense
                total_diff = total_diff + diff

        print "${0:.2f}".format(total_diff)

        expenses = [] # reset for next set of trip expenses

        # when number equals zero money is exchanged
        if line == "0":
            break

f.close()
