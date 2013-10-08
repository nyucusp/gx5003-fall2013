#The trip
#number of students are members of a club 
#they all different amounts in a trip they took
# however you want to eqaulize and make sure that they all spent the same 
#the same amount of money.so you calculate the average spent, then from there you or subtract dependin
#on how much they spent.

#import sys
myfile = open("input1.txt")
number_of_students=0

def avg():
	avg = (sum(tripcost)/len(tripcost))
	return avg
while True:
	number_of_students=int(myfile.readline())
	if number_of_students==0:
		break 

	tripcost=[]
	for i in range(0,number_of_students):
		costs =float (myfile.readline())
		tripcost.append(costs)
		avg()
#print avg()

	#finding the differences
	differences= [x-float(avg()) for x in tripcost]
	roundup= [round(d,2) for d in differences]

	min_amount =[]
	for y in roundup:
		if y<0:
			min_amount.append(abs(y))
			#Avg_cost_per_student=tripcost[i]/number_of_students[i]
	print "%.2f" %float(sum(min_amount))

			#first try

#def equalize(students):
	#number_of_students=len(students)
	#tripcost=sum(students)
	#Avg_cost_per_student=tripcost/number_of_students
	#print Avg_cost_per_student


	#equalize2=[] #initializing
	#total=0
	#for i in range (number_of_students):
		#total=0
		#if Avg_cost_per_student> students[i]:
			#total=total+round(Avg_cost_per_student-students[i])
	#print total	
		#difference=Avg_cost_per_student-students[i]
		#equalize2.append(difference)
		#return equalize2
#d#ef main():
	#price_paid=[10,20,30] #data
	#equalize(price_paid)
	#print equalize
#if __name__ == '__main__':
	#main
