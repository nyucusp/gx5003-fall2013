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

def check(votes,cand_order):
	total={}
	for y in range (0,len(votes)):
		for t in range (0,len(cand_order)):
			if int(votes[y][:1])==cand_order[t]:
				if cand_order[t] not in total.keys():				
					total[cand_order[t]]=0
				total[cand_order[t]]=total[cand_order[t]]+1
	total_per={}
	for q in range (0, len(total.values())):
		total_per[cand_order[q]]=float(total[cand_order[q]])/float(sum(total.values()))
	
	return (max(total_per.values()),min(total_per.iteritems(), key=operator.itemgetter(1))[0])

def shiftitems(temp_votes,remo):
	for h in range(0,len(temp_votes)-1):
		if temp_votes[h]==str(remo):
			temp_votes[h]==temp_votes[h+1]
	return temp_votes

for k in range(0,int(noofcase)):
	i=i+2
	noofcand=float(content[i])
	cand_names=[]
	cand_order=[]
	counter=0
	for u in range(0,int(noofcand)):
		i=i+1
		counter=counter+1
		cand_names.append(content[i])
		cand_order.append(counter)	
	#filter(lambda a: a != '0', cand_names)
	i=i+1
	votes=[]
	t=0
	while (i<len(content)):
		votes.append(content[i])
		i=i+1
	a=(0,0)	
	#while a[0]<0.51:
	a=check(votes,cand_order)
	for c in range(0,len(votes)):
		for p in range(0,len(list(votes[c]))):
			temp_votes=list(votes[c])
			if temp_votes[p]==' ':
				p=p+1
			if temp_votes[p]=='\n':
				break
			if temp_votes[p]==str(a[1]):
				q=p	
				#temp_votes2=shiftitems(temp_votes,a[1])
				while q in range(p,len(list(votes[c]))):

					if temp_votes[q]==temp_votes[-1:][0]:
						break
					if temp_votes[q+1]=='\n':
						temp_votes[q]=temp_votes[q+1]			
					else:						
						temp_votes[q]=temp_votes[q+2]
					q=q+2
			#votes[c]=temp_votes
				#print str(a)		
				#votes[c]=votes[c].replace(str(a[1]),votes[c][p:p+1])
	b=check(votes,cand_order)
	
	#print str(a)	
	

				
