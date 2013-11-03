import sys

#opened the file to read it
txtfile = open('input4.txt', 'r')
input = txtfile.readlines()

#replaced the gibberish by a 1
input[0] = 1
#print input

#called m the number of rows in the grid
m = input[2][0]
#print m

#called n the number of columns in the grid
n = input[2][2:]
#print n

#grid= the grid of letters to find the words, and made them lowercase
grid = input[3:int(3)+int(m)]
grid = [element.lower() for element in grid]
#print grid

#called a the number of words to find
a = input[int(3)+int(m)]
#print a

#called answers the words to find and made them lowercase
answers = input[int(4)+int(m):int(4)+int(m)+int(a)]
answers = [element.lower() for element in answers]
#print answers

#have a really long and lots of nested loops - probably should have
#made lots of it into a function
r = 0
c = 0
o = 0
#going through the rows in the answers and each letter in the grid
while int(r) < int(a):
	o = 0
	while int(o) < int(m):
		p = 0
		while int(p) < int(n):
			c = 0
			#checking if the letter in the answers matches the letter in the grid
			#if not keep going through the grid
			while answers[r][c] !='\n' and grid[o][p] !='' and str(answers[r][c]) == str(grid[o][p]):
				#if it does match a letter then you check around it to see if the
				#whole word is there in a certain direction
				while answers[r][c] !='\n' and grid[o][p] !='' and (str(answers[r][c]) == str(grid[o][p])) and ((str(answers[r][c+1]) == str(grid[o+1][p+1]))):
					#print "first", answers[r][c+1]
					o = o+1
					p = p+1
					c = c+1
					#This is to get the values that you want where the word starts
					# did it for c=3 to get rid of times where they find the first letter only
					if c ==3:
						print o-2,
						print p-2
					#if its the last letter in the answers then go onto the next line and do it again
					if answers[r][c+1] == '\n':
						r = r+1
						c=0
						o=0
						p=0
				#goes through the same thing for each direction
				while answers[r][c] !='\n' and grid[o][p] !='' and str(answers[r][c+1]) == str(grid[o][p+1]):
					#print "second", grid[o][p+1]
					p = p+1
					c = c+1
					#print answers[r][c+1]
					if c ==3:
						print o,
						print p
					if answers[r][c+1] == '\n':
						r = r+1
						c=0
						o=0
						p=0
				while answers[r][c] !='\n' and grid[o][p] !='' and str(answers[r][c+1]) == str(grid[o+1][p]):
					#print "third", grid[o+1][p]
					o = o+1
					c = c+1
					#print answers[r][c]
					if answers[r][c+1] == '\n':
						r = r+1
						c=0
						o=0
						p=0
					if c ==3:
						print o-2,
						print p+1
					if answers[r][c+1] == '\n':
						r = r+1
						c=0
						o=0
						p=0
				while answers[r][c] !='\n' and grid[o][p] !='' and str(answers[r][c+1]) == str(grid[o+1][p-1]):
					#print "4", answers[r][c]
					o = o+1
					p = p-1
					c = c+1
					#print answers[r][c]
					if c ==3:
						print o,
						print p
					if answers[r][c+1] == '\n':
						r = r+1
						c=0
						o=0
						p=0
				while answers[r][c] !='\n' and grid[o][p] !='' and str(answers[r][c+1]) == str(grid[o][p-1]):
					#print "5", answers[r][c+1]
					p = p-1
					c = c+1
					# if grid[o][p-1]!='':
					# 	p = p+2
					#print answers[r][c]
					if c ==3:
						print o+1,
						print p+4
					if answers[r][c+1] == '\n' and int(r)<int(a):
						r = r+1
						c=0
						o=0
						p=0
						if int(r)==int(a):
							sys.exit(0)
				while answers[r][c] !='\n' and grid[o][p] !='' and str(answers[r][c+1]) == str(grid[o-1][p-1]):
					#print "6", answers[r][c]
					o = o-1
					p = p-1
					c = c+1
					#print answers[r][c]
					if c ==3:
						print o,
						print p
					if answers[r][c+1] == '\n':
						r = r+1
						c=0
						o=0
						p=0
				while answers[r][c] !='\n' and grid[o][p] !='' and str(answers[r][c+1]) == str(grid[o-1][p]):
					#print "7", answers[r][c]
					o = o-1
					c = c+1
					#print answers[r][c]
					if c ==3:
						print o,
						print p
					if answers[r][c+1] == '\n':
						r = r+1
						c=0
						o=0
						p=0
				while answers[r][c] !='\n' and grid[o][p] !='' and str(answers[r][c+1]) == str(grid[o-1][p+1]):
					#print "8", answers[r][c]
					o = o-1
					p = p+1
					c = c+1
					if c ==3:
						print o,
						print p
					if answers[r][c+1] == '\n':
						r = r+1
						c=0
						o=0
						p=0
					#print answers[r][c]
#incrementing the while loops
				p=p+1
			#elif int(p+1) <= int(n):
			#print p
			p=p+1
		o=o+1
	r =r+1
		# elif int(p+1) <= int(n):
		# 	print p
		# 	p=p+1
		# else:
		# 	o=o+1
		# 	p=0

# for line in grid[m][n]:
# 	if answers[r][c] != '' and answers[r][c] in grid[m][n]:
# 		m = m + 1
# 		print answers[r][c]
# 	n = n + 1		