from decimal import *
import math

inp = open("input1.txt","r")
data = inp.readlines()
inp.close()


iteration = 1 #it goes through the input file and distributes the numbers
avg = [] #this is the average money they spent
topla = [] #this calculates the total money spent
param = [] #this is a list of each expenditure
numOfStudents = [] #pretty straightforward :)


#This part calculates the number students, total money, money spent each, and average money spent
while data:
    numberOfStudents = int(data.pop(0))
    para=[]
    for i in range(numberOfStudents):
        x = int(float(data.pop(0))*100)
        if x>1000000: #if they spend more than $10,000; we might need to call their family.            
            print "Easy boy, you can't spend more than $10,000, remember?"+"\n"+"I don't think you have $"+str(x)+" anyway."
            break
        else:
            para.append(x)
            param.append(x)
    if numberOfStudents==0:
        break
    elif numberOfStudents > 1000:
        print "Come on!"+str(numberOfStudents)+" Students???"+" Some kids need to stay home man..."
        break
    else:
        toplam = 0       
        for i in range(numberOfStudents):
            exp = int(para.pop(0))
            toplam += exp        
        topla.append(toplam)        
    if numberOfStudents > 0:
        getcontext().rounding = ROUND_UP
        AvgExp = round(Decimal(toplam)/Decimal(numberOfStudents))
        avg.append(AvgExp)
    numOfStudents.append(numberOfStudents)
    iteration = iteration + 1

# I defined this in order to get 2 decimals
def trunc(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    return ('%.*f' % (n + 1, f))[:-1]

#this part looks at average values and calculates given and taken amounts of money
m = 0
for i in range(0,len(numOfStudents)): #range shoulde be the length of numOfStudents
    sumdown = 0
    sumup = 0
    b = avg[i] #b is equal to the average
    for j in range(m,(m+numOfStudents[i])): 
        a = param[j]
        if(a<b):
            sumdown += (b-a) #sum of given
        else:
            sumup += (a-b) #sum of taken
    if (sumup<sumdown):
        print '$'+ trunc((Decimal(sumup)/Decimal(100)),2)
    else:
        print '$'+trunc((Decimal(sumdown)/Decimal(100)),2)
    if(sum(numOfStudents) == m+numOfStudents[i]):
       break
    else:
       m = m+numOfStudents[i]

#Note: In my opinion, for this problem, you should tell that if we need to round up or down the results.


    
