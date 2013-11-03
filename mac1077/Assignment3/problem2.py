import sys
import csv
import math
import operator

#it first reads the text file input2
   
with open("input2.txt") as f:
    content = f.readlines()

i=0
numcase=float(content[i])

#check number of votes
#input of votes and candidate orders returning the vote % the highest
def check(votes,cand_order):
	total={}   
	for y in range (0,len(votes)):
		for t in range (0,len(cand_order)):
			if votes[y][:1]==' ':    
				votes[y][:1]=votes[y][2:3]
			if int(votes[y][:1])==cand_order[t]:
				if cand_order[t] not in total.keys():				
					total[cand_order[t]]=0
				total[cand_order[t]]=total[cand_order[t]]+1  # add 1 if vote is to the candidate
	total_per={} 
	
	for q in total.keys():  # deletes lowest candidates & check keys
	
		q=q-1   #candidate order starts from 1
		total_per[cand_order[q]]=float(total[cand_order[q]])/float(sum(total.values()))
	
	return (max(total_per.values()),min(total_per.iteritems(), key=operator.itemgetter(1))[0],max(total_per.iteritems(), key=operator.itemgetter(1))[0])

for k in range(0,int(numcase)): 
	i=i+2 
	noofcand=float(content[i])
	cand_names=[]   # names on the list
	cand_order=[]	# order of candidates in the list
	counter=0       
	for u in range(0,int(noofcand)):  #will write the txt with the lists
		i=i+1
		counter=counter+1
		cand_names.append(content[i])
		cand_order.append(counter)	
	
	i=i+1
	votes=[]
	t=0
	# read votes and add to the list
	while (i<len(content)):
		votes.append(content[i])
		i=i+1
	
	a=(0,0,0)
	a=check(votes,cand_order) 
	while a[0]<0.51:          # no loop if votes >50%
				  
		
		for c in range(0,len(votes)):
			for p in range(0,len(list(votes[c]))):
			
				
				if votes[c][p:p+1]==str(a[1]):	
					votes[c]=votes[c].replace(str(a[1]),votes[c][p+2:])  
		a=check(votes,cand_order)  
	
	print cand_names[a[2]-1]  # name of the winner
	k=k+1 
	

				
