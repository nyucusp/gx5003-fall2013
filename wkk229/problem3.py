import sys
print sys.argv
import select
import random

LA=["x","x","x" ,"x","x","x","x"]
LB=["x","x","x","x","x","x","x"]
LC=["x","x","x","x","x","x","x"]
LD=["x","x","x","x","x","x","x"]
LE=["x","x","x","x","x","x","x"]
LF=["x","x","x","x","x","x","x"]
LG=["x","x","x","x","x","x","x"]

print("", LA,"\n",LB,"\n",LC,"\n",LD,"\n",LE,"\n",LF,"\n",LG,"\n")

print"\n" 
#select.row starting from top = 1 and column from left = 0

num = random.randint(1,7)
numb= random.randint(0,6)
MINE= "0"

row = 9
column = 9
one = "1"
zero = "-"

while row != num or column != numb:
	print("",LA ,"\n", LB, "\n", LC,"\n",LD,"\n", LE,"\n",LF, "\n", LG,"\n")
	#cheeter 
	print(num, "" , numb)
	row = int (input("nEnter row"))
	column =int (input("nEnter column"))
	columnA = column + 1
	columnB = column -1
	rowA = row + 1
	rowB = row + 1

	if rowA == num and column == numb:
		if row == 1:
			del LA [column]
			LA.instert( column ,one)
		if row == 2:
			del LB [column]
			LB.instert( column ,one)
		if row == 3:
			del LC [column]
			LC.instert( column ,one)
		if row == 4:
			del LD [column]
			LD.instert( column ,one)
		if row == 5:
			del LE [column]
			LE.instert( column ,one)
		if row == 6 :
			del LF [column]
			LF.instert( column ,one)
		if row == 7:
			del LG [column]
			LG.instert( column ,one)
	elif row == num and columnA == numb :
		if row == 1:
			del LA [column]
			LA.instert( column ,one)
		if row == 2:
			del LB [column]
			LB.instert( column ,one)
		if row == 3:
			del LC [column]
			LC.instert( column ,one)
		if row == 4:
			del LD [column]
			LD.instert( column ,one)
		if row == 5:
			del LE [column]
			LE.instert( column ,one)
		if row == 6 :
			del LF [column]
			LF.instert( column ,one)
		if row == 7:
			del LG [column]
			LG.instert( column ,one)
	elif row == num and columnB == numb :
		if row == 1:
			del LA [column]
			LA.instert( column ,one)
		if row == 2:
			del LB [column]
			LB.instert( column ,one)
		if row == 3:
			del LC [column]
			LC.instert( column ,one)
		if row == 4:
			del LD [column]
			LD.instert( column ,one)
		if row == 5:
			del LE [column]
			LE.instert( column ,one)
		if row == 6 :
			del LF [column]
			LF.instert( column ,one)
		if row == 7:
			del LG [column]
			LG.instert( column ,one)
	else :
		if row == 1:
			del LA [column]
			LA.instert( column ,zero)
		if row == 2:
			del LB [column]
			LB.insert(column ,zero)
		if row == 3:
			del LC [column]
			LC.insert( column ,zero)
		if row == 4:
			del LD [column]
			LD.insert( column ,zero)
		if row == 5:
			del LE [column]
			LE.insert( column ,zero)
		if row == 6 :
			del LF [column]
			LF.insert( column ,zero)
		if row == 7:
			del LG [column]
			LG.insert( column ,zero)
	
if row ==1:
	
    del LA [column]
LA.insert( column ,MINE)
if row == 2:
	del LB [column]
	LB.insert( column ,MINE)
if row == 3:
	del LC [column]
	LC.insert( column ,MINE)
if row == 4:
	del LD [column]
	LD.insert( column ,MINE)
if row == 5:
	del LE [column]
	LE.insert( column ,MINE)
if row == 6 :
	del LF [column]
	LF.insert( column ,MINE)
if row == 7:
	del LG [column]
	LG.insert( column ,MINE)	

print("",LA ,"\n", LB, "\n", LC,"\n",LD,"\n", LE,"\n",LF, "\n", LG,"\n")
print ("Gmae over")

input ("press enter to exit")





