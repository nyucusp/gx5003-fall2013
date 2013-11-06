#Kara Leary
#Urban Informatics
#Assignment 3 - Problem 1

import sys

#Open the file to be read:
myFile = open('input1.txt','r')

#Initialize number of students n to maximum value (1000).  I will use this in my while loop to continue running the program until n is read as 0, at which case it will exit.
n = 1000

while n != 0:
    n = int(myFile.readline()) #read value of n
    if (n == 0): #if n is zero, exit the program
        sys.exit()
    total = 0
    count = 0
    amountpaid = []
    while count < n:
        value = myFile.readline().strip('\n') #read each value paid by students
        total += float(value)
        total = round(total, 2) #store a running total of amounts paid
        count += 1 #keep track of number of students so that I stop reading values before the next group of students begins
        amountpaid.append(value)
    avg_money = total/n #find the money each student needs to pay individually

    i = 0
    totalexchange = 0 #this variable stores the total amount of money that has changed hands
    while i < n:
        totalpaid = float(amountpaid[i]) 
        if (totalpaid > avg_money): #if a student has paid more than he or she needs to, enter this if statement that will find how much he has overpaid
            difference = totalpaid - avg_money
            difference = round(difference, 2)
            totalexchange += difference #the difference between what the student has paid and what he should have paid will be the amount of money that changes hands
        i += 1
    print '%.2f' % totalexchange #print the total amount exchanged to two decimal places

myFile.close()
