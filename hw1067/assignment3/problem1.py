#Problem 1
#Haozhe Wang

#Math behind the calculation
#first, calculate the average n\ (add all the costs and divided by the number of participants)
#then, let each cost subtract the average
#finally, add abs(all the negative difference)

#all the commented print commend was used to testrun my code

inputfile = open("input1.txt")

def avg():
    avg=(sum(costs)/len(costs))
    return avg
    
while True:
    NumOfTravelers = int(inputfile.readline())#the integers are number of travelers
    if NumOfTravelers == 0:
        break

#Now, caculate the average.
    costs=[]#store the costs in a list
    for i in range(0, NumOfTravelers):
        costsvalue = float(inputfile.readline())
        costs.append(costsvalue)
    avg()
    #print avg()

#Find out the differences, and round them to two decimals
    difference = [x - float(avg()) for x in costs]
    #print difference
    roundup = [round(d, 2) for d in difference]
    #print roundup

#Add up all the abs(negative differences)
#I got 12.0 if no rounding was processed, don't understand why 11.99 is more correct than 12.00
    min_amount=[]
    for y in roundup:
        if y < 0:
            min_amount.append(abs(y))
    print "%.2f" %float(sum(min_amount))
