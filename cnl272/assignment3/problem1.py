import sys
myFile = open('input1.txt', 'r')
input_lines = []
for line in myFile:
	input_lines.append(line[:-1])
myFile.close()

def exchange_amount(expense_list, student_number):
#create a function to caculate the average expense and the amount of exchange
	total_expense = 0.0
	for i in expense_list:
		total_expense=total_expense+float(i)
	average_expense = total_expense/student_number
	total_expense = 0.0
	
	exchange = 0
	for g in expense_list:
		g=float(g)
		if g < average_expense:
			exchange += (int((average_expense-g)*100)/100.0)
		#get the second digit after the decimal point, and sum the difference

	print '$' + str(exchange)

def studentNumber():
	expense_list = []
	averge_expense = 0.0
	total_expense = 0.0
	current_position=0

	student_number=int(input_lines[current_position])
	while student_number != 0:
		position_of_next_student_number = student_number+1+current_position
		expense_list = input_lines[current_position+1:position_of_next_student_number]

		exchange_amount(expense_list, student_number)
		#call the function of exchange_amount
		student_number=int(input_lines[position_of_next_student_number])
		current_position=position_of_next_student_number

studentNumber()

