#read txt file
#here I create a list to store all the lines in the text
display_list = []


#line.strip method is used to pass the data to the list
with open('input4.txt') as data_file:
   for line in data_file:
      display_list.append(line.strip().split(' '))

#ic is the line counter
ic=0

#kt is the scenario counter 
kt=0

#first get the number of scenarios from the first entry in the list
no_scenario=int(display_list[0][0])

#scenarios are handled by a while loop
while kt<no_scenario:	
	ic=ic+2				#go to the number of rows and columns line
	no_row=int(display_list[ic][0])
	no_col=int(display_list[ic][1])
	
	matrixo=[]			#define a matrix for the words grid
	for r in range(0,no_row):
		matrixo.append(display_list[ic+1+r])

	no_words=int(display_list[ic+no_row+1][0])	#get the number of words that we will search
	
	words_list=[]					#put the words in a list
	for k in range(0,no_words):
		words_list.append(display_list[ic+no_row+2+k])

	def seeker(sx,sy,letter,ati):			#this function gets the location of the start point of a word
		#print sx+1				#and gets the next letter and scans the neighboring characters
		#print sy+1				#in the grid. if finds the next letter returns the location of 
							#the new letter
		
		if sx+1<no_row and sy+1<no_col:
			if ati[sx+1][sy+1]==letter:
				return (sx+1,sy+1)
		if sx-1>0 and sy-1>0:
			if ati[sx-1][sy-1]==letter:
				return (sx-1,sy-1)		
		if sx-1>0 and sy+1<no_col:
			if ati[sx-1][sy+1]==letter:
				return (sx-1,sy+1)
		if sx+1<no_row and sy-1>0:
			if ati[sx+1][sy-1]==letter:
				return (sx-1,sy-1)
		if sy-1>0:
			if ati[sx][sy-1]==letter:
				return (sx,sy-1)
		if sx-1>0:
			if ati[sx-1][sy]==letter:
				return (sx-1,sy)
		if sx+1<no_row:
			if ati[sx+1][sy]==letter:
				return (sx+1,sy)
		if sy+1<no_col:
			if ati[sx][sy+1]==letter:
				return (sx,sy+1)	
		#return end
		

	def searcher(word,matrix):			#this function gets the word to be found in the grid
		leng=len(matrix)			#and the grid as a matrix
		ati=[]					#find the location of the first letter
		for u in range(0,leng):			#then calls the "seeker function" to find the location of 	
			for g in matrix[u]:		#the next letter
				temp=g
				ati.append(list(g))
				
		dene=list(word)
		#print dene
		for char in dene:
			olta=list(char)
			#print olta
			for z in range(0,len(olta)):
				for i in range(0,no_row):
					for j in range(0,no_col):
						if ati[i][j]==olta[z]:
							#print olta[z]
							#print str(i) + str(j)
							if z+1<len(olta):
								st=i
								en=j
								counter=1				#counter is used to find the match
								for ol in range(z+1,len(olta)):		#since it scans with order from the top
									kiki=seeker(st,en,olta[ol],ati)	#the result will always be the topmost as defined in the description
									if kiki>0:
										st=kiki[0]
										en=kiki[1]
										ol+=1
										counter+=1
									if counter==len(olta):		#if counter has the same length with the word 
										return (i+1,j+1)	#it means we have a match and the function returns the location	
									#print kiki			#of the first letter of the word
									#print counter							
							
							#print ati[i][j]
							#print olta[z]

		
	for words in words_list:						#since we have upper and lower case letters which does not matter in the search
		veli=list(words)						#before sending to the "searchcer" function we convert everything to lowercase letters
		kavlak=list(veli)[0]
		
		matrixo_low=[]
		for matri in matrixo:
			matri=list(matri)[0]
			matri=matri.lower()
			matrixo_low.append([matri])
		#print kavlak.lower()
		#print matrixo_low
		kolpa=searcher([kavlak.lower()],matrixo_low)
	#kolpa=searcher(words_list[2],matrixo)
		print str(kolpa[0])+" "+str(kolpa[1])				#print the location
	print "\n"								#print a blank between scenarios
	kt=kt+1									#go to the next scenario
	ic=ic+1+no_row+no_words							#jump to the line where next scenario begins
