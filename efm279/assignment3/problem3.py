
#read txt file
   
with open("input3.txt") as f:
    content = f.readlines()

no_scenario=int(content[0])
k=0  #Scenario counter
ic=0 #This is line counter


while k<no_scenario:
	ic=ic+1		#Skip the first line
	no_author=int(list(content[ic])[2])	#get the number of authors
	no_paper=int(list(content[ic])[0])	#get the number of papers

	subcontent=content[ic+1:ic+1+no_paper]	#define a list of lists that contain paper information
	authors=content[ic+1+no_paper:ic+1+no_paper+no_author]	#define a list of lists that contain author names that we will test



	papers_dic={}	# a dictionary for papers with values 1: Erdos included in the paper 2: not Erdos in the paper
	for line in subcontent:
		if line.find("Erdos")!=-1:
			papers_dic[line]=1
		else:
			papers_dic[line]=0		
			#print "found erdos"


	erdos=[[] for x in xrange(20)] #define a container 
	i=0

	authors3_dic={}
	#I assumed this as a network problem trying to find the shortest path where Erdos is in the center 	
	#define a function that takes author list, paper list, erdos paper list and paper dictionary 
	#then returns an updated author dictionary including values of the distance to the Erdos papers
	
	
	def finder(author,subcontent,erdos,papers_dic):
		for line in subcontent:
			a=line.find(author[:-2])
			#print author
			#print line
			#print a
			if a!=-1:
				for i in range(0,len(erdos)):
					#print i
					if author not in authors3_dic.keys():
						authors3_dic[author]=0
					for j in erdos[i]:
						#print j
						b=line.find(j[:-2])
						if (b!=-1):
							#print i
							authors3_dic[author]+=i
		return authors3_dic			

		
	erdos[1]=['Erdos, P.'] #Erdos is in the center with value 1 
	
	#For all candidates in the authors list call the function and get the values
	for cand in authors:
		t=finder(cand,subcontent,erdos,papers_dic)
		for aday in t.keys():
			if aday=='Erdos, P.\n':
				erdos[1].append(aday)
			else:
				erdos[t[aday]].append(aday)


	#Print the results
	print "Scenario "+ str(k+1)
	for cand in authors:
		if cand=='Erdos, P.':
			print cand[:-1]+" 0"
		for i in range(0,len(erdos)-1):
			if cand in erdos[i]:
				if i==0:
					if cand == 'Erdos, P.\n':
						print cand[:-1]+ " 1"
					else:					
						print cand[:-1]+" Infinity"

				else: 
					print cand[:-1]+ " "+ str(i)

	#go to the next scenario
	k=k+1	
	#go to the line where next scenario starts
	ic=ic+no_author+no_paper
	#reset the erdos and t lists
	erdos=[[0] for x in xrange(20)]
	for att in t.keys():
		t[att]=0	

