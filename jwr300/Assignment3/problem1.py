#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 3, Problem 1
"""
For a given list of expenses this Python script will compute the minimum amount
of money that must exchange hands in order to equalize within one cent, all the students costs. 

"""

# Reads input form txt file into list
expenses = []
myFile = open('input1.txt','r')

for line in myFile:
    expenses.append(line)
myFile.close()

""" 
Method that accepts as arguments an expense list and the average expense and returns 
the sum of the difference between the average expense and expense that is less than the average
"""

def amountToExchange(expense_list, avgExpense):
    exchangeAmount = 0.0
    for i in range (0,len(expense_list)):
        if expense_list[i] < avgExpense:
            exchangeAmount += (round(avgExpense - expense_list[i],2))
    return exchangeAmount

"""
Parses through the expenses list, looking for a positve integer that denotes
the number of students on the trip. Script then creates an expense list that is 
passed to the method amountToExchange and returns the min exchangeAmount and prints
to screen.


"""
for i in range (0,len(expenses)):
    if expenses[i].find(".") == -1:
        expense_list = []
        for j in range (i+1, i+int(expenses[i])+1):
            expense_list.append(round(float(expenses[j]),2))
        if (len(expense_list) > 0):
            amount = amountToExchange(expense_list, round((sum(expense_list) / len(expense_list)),2))
            print "$%.2f" % (amount)  
