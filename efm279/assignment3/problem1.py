import sys
import csv
import math

#read txt file
   
with open("input1.txt") as f:
    content = f.readlines()
i=0
sum=0
cpos=0
cneg=0
test=float(content[i])
change=[0 for x in xrange(1000)]
while test !=0:
	number=float(content[i])
	if number>10000:
		print "cannot calculate more than 10000 students"
		break
	
	
	start=i
	counter=0
	i=i+1
	
	sum=0
	while counter<number: 		
		sum= sum+float(content[i])
		if float(content[i])>10000:
			print "cannot calculate more than 10000 dollars"
			sys.exit(0)		
		counter=counter+1			
		i=i+1
	perper=sum/number

	#the reason I use ceil is we are considering monetary values
	#if I round down monetary values will not be correct
	#the way I use here can raise some rounding concerns too 
	#it was not clearly defined so I decided to stick with rounding always up

	perper=math.ceil(perper*100)/100
	#perper="{0:.2f}".format(perper)
	for j in range(start+1,start+int(number)+1):
		if float(content[j])>perper:
			change[j]=float(content[j])-perper
			cpos=cpos+change[j]
		else:
			change[j]=perper-float(content[j])
			cneg=cneg+change[j]		
	final=min(cpos,cneg)
	#print str(cpos) + " " +str (cneg)		
	print "$"+str("{0:.2f}".format(final))
	cneg=0
	cpos=0	
	#print str(perper)
	test=float(content[i])


