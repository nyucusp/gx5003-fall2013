#This program receives a list of expenses, and computes the minimum amount of money 
#that must change hands in order to equalize (within one cent) all the students' costs.
"""
Since an exchange is a "give & receive" transaction, the total to exchange is either of the two equal sums 
	a) total money to be paid by one or more person to one or more others for a trip 
	b) total money to be received by one or more person from one or more others for a trip

I will use positive amounts, obtained through these steps: 
1) calculating expenses per person for the trip, which is the calculation of the average (arithmetic mean) of all expenses spent on the trip
2) checking what each person owes or is owed by the operation (Trip Average - Amount Spent).
	a) if  (Trip Average - Amount Spent) is positive, the person still owes money, and will pay (positive exchange, at least for the sake of our problem...)
	b) if  (Trip Average - Amount Spent) is negative, the person is owed money, and will be paid (negative exchange, can be disregarded)
3) the amount to be exchanged is the sum of positive exchanges
"""

import sys

from decimal import Decimal

myFile = open('input1.txt','r')

#we load the file contents into a list trip_info to manipulate with Python
trip_info = []

for line in myFile:
	trip_info.append(line) 

#this function takes a list of values as an input, and returns the amount to exchange based on summing the payments made. 
#we will use it for each trip individually
def exchanged_amount(expenses):
	value_record = 0 #we'll use this as an index in the list of expenses
	while value_record <= len(expenses)-1:
		#print 'first while' #debugging
		expenses[value_record] = Decimal(expenses[value_record]) 
		value_record += 1

	expenses_per_person = Decimal(sum(expenses)/len(expenses)) #average is sum of values over their number, or the length of the list they're in
	#print 'expenses_per_person is ' + str(expenses_per_person) #debugging
	amount_to_exchange = 0
	value_record = 0 
	while value_record <= len(expenses)-1:
		#print 'second while' #debugging
		if expenses_per_person - expenses[value_record] > 0:
			amount_to_exchange = Decimal(amount_to_exchange + (expenses_per_person - expenses[value_record]))
			#print 'amount_to_exchange is ' + str(amount_to_exchange) #debugging
		value_record += 1

	#print 'amount_to_exchange is ' + str(amount_to_exchange) #debugging. 
	#It is outputting 12.000 instead of 11.991 for trip 2.
	#not sure of reason
	
	return round(amount_to_exchange, 2) 


#now we parse the list to locate individual trips
list_index = 0 

#we use this to count how many trips we are finding the exchanged amount for
trip_counter = 1

while list_index < len(trip_info) - 1: 
	#index less than length of input list means we're still looking in the input list

	this_trip = [] #we will use this list to load trip info to calculate amount to exchange
	#print 'trip_info[list_index] is ' + trip_info[list_index] #debugging
	number_of_students =  int(trip_info[list_index])
	#print 'number_of_students is ' + str(number_of_students) #debugging
	this_trip = trip_info[list_index + 1:list_index + number_of_students + 1] 	
	#this loads the values from the first line of the trip (just after the number of students) 
	#till last line, i.e. just before the number of students for next trip in input
	
	print 'The amount exchanged for trip ' + str(trip_counter) + ' is ' + str(exchanged_amount(this_trip))
	list_index += number_of_students + 1
	trip_counter += 1
	#print 'list index for trip info list is ' + str(list_index) #debugging


myFile.close()





