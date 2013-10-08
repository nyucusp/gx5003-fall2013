#compare the average to everyone's cost in a trip, 
#find the cost which are larger than the average,
#the minimum exchange equals to the sum of each larger cost minus average cost

myFile = open('input1.txt','r')
readdata = []#create an array to put the data from input1
for line in myFile:
	readdata.append(line[:-1])#add the data into array
myFile.close


student=int(readdata[0])#make the student number(in the first line) into an integer
currentposition=0#the position of student number in the array of readdata
min_exchange=[]


while student!=0: #create a loop to calculate the data in every trip

	cost=[]#create an array to put everyone's cost in a trip
	for i in range (currentposition+1,currentposition+student+1):
		cost.append(float(readdata[i]))
	
	sumcost=sum(cost)#get the sum of cost
	averagecost=sumcost/student#get the average cost


	largercost=[]#create an array to put the cost larger than the average
	for x in cost:
		if x>averagecost:
			largercost.append(x)
			

			difference=[]#create an array to put the difference between larger cost and average
			for y in largercost:
				difference.append(int((y-averagecost)*100)/100.0)#make the money within one cent

	min_exchange.append(sum(difference))#minimum exchange is the sum of difference


	currentposition=currentposition+student+1#find the position of students number in the next trip in the array
	student=int(readdata[currentposition])#find the student number in next trip
	

for z in min_exchange:

	output=str(z)+"\n"
	print output






