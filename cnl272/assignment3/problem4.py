
myFile = open('input4.txt', 'r')
input_lines = []
for line in myFile:
	if line[-1] == '\n':
		line=line.lower()
		input_lines.append(line[:-1])
myFile.close()
input_lines.append('')
#add '/n' after the last string in case it can't be read

def get_words(input_lines):
	case_number=int(input_lines[0])
	blank = []
	all_word_context = []
	for all_line in range(1,len(input_lines)):
		if input_lines[all_line] == '':
			blank.append(all_line)
			#use blank to identify each case
	for blank_line in range(0,len(blank)-1):
		words=input_lines[blank[blank_line]+1:blank[blank_line+1]]
		all_word_context.append(words)
#put the information of candidates number, candidates'name and ballots into word_context

	grid_context=[]
	word_list=[]
	for i in range(len(all_word_context)):
		seperate_case = all_word_context[i]
		#seperate each case in all_word_context so we can run it seperately
		m=int(seperate_case[0].split()[0])
		n=int(seperate_case[0].split()[1])
		
		grids = seperate_case[1:m+1]
		grid_context.append(grids)

		w=int(seperate_case[m+1])
		words=seperate_case[m+2:m+2+w]
		word_list.append(words)		
	return grid_context,word_list
	
def get_words_in_directions(grid_context,l,x,y):
	m=len(grid_context)
	n=len(grid_context[0])

	words_for_compare=[]
	temp_vec=[]
	all_directions=[[1,0],[0,1],[1,1],[-1,0],[0,-1],[1,-1],[-1,1],[1,1]]
	for d in all_directions:
		tempx=x
		tempy=y
		lastword_in_gridx=x+d[0]*l
		lastword_in_gridy=y+d[1]*l
		if lastword_in_gridy >= m or lastword_in_gridy <0 or lastword_in_gridx >=n or lastword_in_gridx<0:
			break
		word_for_compare=''
		for i in range(l):
			tempx=tempx+d[0]
			tempy=tempy+d[1]
			cha=grid_context[tempy][tempx]
			word_for_compare+=cha
		words_for_compare.append(word_for_compare)
	return words_for_compare


def find_words(grid_context, word_list):
	for word in word_list:
		nextword=0
		for y in range(len(grid_context)):
			if nextword==1:
				break
			for x in range(len(grid_context[y])):
				if nextword==1:
					break
				if word[0] == grid_context[y][x]:

					words_for_compare=get_words_in_directions(grid_context,len(word)-1,x,y)
					if word[1:] in words_for_compare:
 						print y+1, x+1
 						return

grid_context,word_list=get_words(input_lines)
for case_number in range(len(grid_context)):
	find_words(grid_context[case_number], word_list[case_number])

					

