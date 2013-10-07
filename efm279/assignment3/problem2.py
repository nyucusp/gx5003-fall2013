import sys
import csv
import math
import operator

#read txt file
   
with open("input2.txt") as f:
    content = f.readlines()

#number of cases
i=0
noofcase=float(content[i])

#function for checking the number of votes
#takes votes list and candidate order as inputs
#returns the vote percentage of the highest, the ids of the lowest and highest voted candidates 
def check(votes,cand_order):
	total={}   #total votes are held in a dictionary
	for y in range (0,len(votes)):
		for t in range (0,len(cand_order)):
			if votes[y][:1]==' ':    #check if it is a space in votes list
				votes[y][:1]=votes[y][2:3]
			if int(votes[y][:1])==cand_order[t]:
				if cand_order[t] not in total.keys():	#check if the candidate id is defined in the dictionary			
					total[cand_order[t]]=0
				total[cand_order[t]]=total[cand_order[t]]+1  #if vote is to the candidate in the loop, add 1
	total_per={} # vote percentages in a dictionary
	
	for q in total.keys():  # we check the keys for the later stages when we delete the lowest voted candidate
	
		q=q-1   #this is because the candidate orders start from 1
		total_per[cand_order[q]]=float(total[cand_order[q]])/float(sum(total.values()))
	
	return (max(total_per.values()),min(total_per.iteritems(), key=operator.itemgetter(1))[0],max(total_per.iteritems(), key=operator.itemgetter(1))[0])

#main part, first takes the number of cases

for k in range(0,int(noofcase)): #loop for the cases
	i=i+2 #jumps the space
	noofcand=float(content[i])
	cand_names=[]   #holds the names in a list
	cand_order=[]	#the order of candidates in a list
	counter=0       
	for u in range(0,int(noofcand)):  #fill in the above two lists from the text file read
		i=i+1
		counter=counter+1
		cand_names.append(content[i])
		cand_order.append(counter)	
	#filter(lambda a: a != '0', cand_names)  tried filter here.
	i=i+1
	votes=[]
	t=0
	#read the votes and add it to a list of strings
	while (i<len(content)):
		votes.append(content[i])
		i=i+1
	#a is what returns from the function "check"	
	a=(0,0,0)
	a=check(votes,cand_order) #call the function for the initial condition	
	while a[0]<0.51:          #if someone got more than 50% do not enter the while loop
				  # the logic is to manipulate the "votes" list in the loop, delete the lowest voted candidate and reorder
		
		for c in range(0,len(votes)):
			for p in range(0,len(list(votes[c]))):
			#votes[c]=temp_votes
				#print str(a)
				if votes[c][p:p+1]==str(a[1]):	#here it checks the lowest voted candidate in the votes list	
					#votes[c][p:p+1]=votes[c][p+1:p+2]
					votes[c]=votes[c].replace(str(a[1]),votes[c][p+2:])  #here it makes the reorder
	#cand_order[a[1]-1]=0	
		a=check(votes,cand_order)  #sends it back to the check function until someone exceeds 50%
	
	print cand_names[a[2]-1]  # print the name of the winner
	k=k+1 #go to the other case	
	

				
