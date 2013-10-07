
#read txt file
   
with open("input3_ex.txt") as f:
    content = f.readlines()

no_scenario=int(content[0])
no_author=int(list(content[1])[2])
no_paper=int(list(content[1])[0])

subcontent=content[2:-no_author]

def firstlink(subcontent,author,no_paper):
	for line in subcontent:
		return line.find(author,len(line))

authors=content[2+no_paper:]

papers_dic={}

for line in subcontent:
	if line.find("Erdos")!=-1:
		papers_dic[line]=1
	else:
		papers_dic[line]=0		
		#print "found erdos"

authors_dic={}
for cand in authors:
	authors_dic[cand]=0
	for line in subcontent:
		a=line.find(cand[:-2])
		if a!=-1:
			if papers_dic[line]==1:
				authors_dic[cand]+=1

erdos_first=[]
for cand in authors:
	if authors_dic[cand]>0:
		erdos_first.append(cand)
			
authors2_dic={}
for cand in authors:
	authors2_dic[cand]=0
	for line in subcontent:
		a=line.find(cand[:-2])
		if a!=-1:
			for j in erdos_first:
				b=line.find(j[:-2])
				if (b!=-1) and authors_dic[cand]!=1:
					authors2_dic[cand]+=1
		
erdos_second=[]
for cand in authors:
	if authors2_dic[cand]>0:
		erdos_second.append(cand)		

for cand in authors:
	if cand in erdos_first:
		print cand[:-2]+" 1"
	elif cand in erdos_second:
		print cand[:-2]+" 2"
	else:
		print cand[:-2]+" Infinity"	
	#a=firstlink(subcontent,cand[0][:-2],no_paper)
		#print a
