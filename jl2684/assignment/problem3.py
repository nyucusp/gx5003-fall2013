import sys
lines = sys.argv[1]
split_lines = lines.split('\\n')
mine_string_input = split_lines[1:]
n = int(split_lines[0][0]) - 1

mine_string_zeros = [[Row.replace('.','0') for Row in Column] for Column in mine_string_input]

#print mine_string_zeros

def addOne(n):
		if '*' in mine_string_zeros[n]:
			m = mine_string_zeros[n].index('*')
			if n - 1 != -1 and m - 1 != -1:
				mine_string_zeros[n-1][m-1] = int(mine_string_zeros[n-1][m-1]) + 1 
			if n - 1 != -1:
				mine_string_zeros[n-1][m] = int(mine_string_zeros[n-1][m]) + 1 
				mine_string_zeros[n-1][m+1] = int(mine_string_zeros[n-1][m+1]) + 1
			if m - 1 != -1:
				mine_string_zeros[n][m-1] = int(mine_string_zeros[n][m-1]) + 1
				mine_string_zeros[n+1][m-1] = int(mine_string_zeros[n+1][m-1]) + 1
			mine_string_zeros[n][m+1] = int(mine_string_zeros[n][m+1]) + 1
			mine_string_zeros[n+1][m] = int(mine_string_zeros[n+1][m]) + 1 
			mine_string_zeros[n+1][m+1] = int(mine_string_zeros[n+1][m+1]) + 1
		return mine_string_zeros

#print addOne(n)

	
def variousrows(n):
	while n != -1:
		addOne(n)
		n = n - 1 
	return mine_string_zeros
print 'Field #1'
print variousrows(n)

#output = ''.join(map(str, mine_string_zeros))

#print output

# learn repeat 



# Row i n 
# Column j m 

#def mine_position_column(Row): 
#	mine_position_column = mine_string_zeros[Row].index('*')
#	return mine_position_column

#print mine_position_column(Row)




#for Row in mine_string_zeros:
#	if '*' in Row:



#for Row in mine_string_zeros:
#	indexofMine = Row.find('*')
#	if indexofMine != -1:
#		addone(n)

#print addOne(n)

#

# mine_string_zeros = [map(int, x) for x in mine_string_zeros] # making into integers 

# print mine_string_zeros

# Row 0 = mine_string_zeros[0]

#Row0 values mine_string_zeros[0][j]

#while j < m:
#	index 
#j = j + 1 



#for i, value in enumerate(mine_string_input):
#	mylist[i] = value.replace()

#mine_string_input[0] = Row 1 
#mine_string_input[1] = Row 2 

#print mine_string_input

#mine_string_output = [

#print mine_string_output


# print mine_string[0][0]

#def mine_string[i][j]:
#	i = 0
#	j = 0
#	if mine_string[i][j] == '*'
#		mine_string[i][j] == '*'



# Row = n 
# Column = m 

#if split_lines[n][m]
