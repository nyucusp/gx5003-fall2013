#read txt file

display_list = []

with open('input4.txt') as data_file:
   for line in data_file:
      display_list.append(line.strip().split(' '))


ic=0
k=0
no_scenario=int(display_list[0][0])
while k<no_scenario:	
	ic=ic+2
	no_row=int(display_list[ic][0])
	no_col=int(display_list[ic][1])
	
	matrixo=[]
	for r in range(0,no_row):
		matrixo.append(display_list[ic+1+r])

	no_words=int(display_list[ic+no_row+1][0])
	
	words_list=[]
	for k in range(0,no_words):
		words_list.append(display_list[ic+no_row+2+k])

	def seeker(sx,sy,letter,ati):
		#print sx+1
		#print sy+1
		
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
		

	def searcher(word,matrix):
		leng=len(matrix)
		ati=[]
		for u in range(0,leng):
			for g in matrix[u]:
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
								counter=1
								for ol in range(z+1,len(olta)):
									kiki=seeker(st,en,olta[ol],ati)
									if kiki>0:
										st=kiki[0]
										en=kiki[1]
										ol+=1
										counter+=1
									if counter==len(olta):
										return (i+1,j+1)
									#print kiki
									#print counter							
							
							#print ati[i][j]
							#print olta[z]

		
	for words in words_list:
		veli=list(words)
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
		print kolpa
	print "\n"
	k=k+1
