import sys

lines_temp = sys.argv[1]
lines = lines_temp.split('\\n')
parameters_temp = lines[0]
parameters = parameters_temp.split()

"""
Here we extract the dimensions of the input field
"""
rows = int(parameters[0])
cols = int(parameters[1])

"""
Working_lines is a list which has the rows of the input field as strings
"""
working_lines = lines
working_lines.pop(0)

"""
Here we make a dict whose key is the (i,j) position and whose value is * or .
However, we imagine augmenting our initial field with two extra rows and two extra
    columns of '.'s on the outside.  This will make our 'count' function easier to 
    implement.
Therefore, we add extra keys to our dict to correspond to positions in the extra rows
    and columns    
"""

positions = {}
k = 0
while k < (rows+2)*(cols+2):
    for i in range(0,rows+2):
        for j in range(0, cols+2):
            key = (i,j)
            if (i in range (1, rows+1)) and (j in range(1, cols+1)):
                value = (working_lines[i-1])[j-1]
                positions[(i,j)] = value
            else:
                value = "."
                positions[(i,j)] = value
            k += 1

"""
Now we make a count function which takes an input (i,j) and returns the number of
adjacent mines, or a "*" if the entry at position (i,j) is a mine.
"""

def count(i,j):            
    mines = 0               #this variable keeps track of how many mines are adjacent
    if positions[(i,j)] == "*":
        return "*"
    else:
        for k in range(-1,2):
            for l in range(-1,2):
                if positions[(i+k,j+l)] == "*":
                    mines += 1
        return mines

                            
print "Field 1:"
"""
Now we construct the output field using our count function
"""

for i in range(1, rows+1):
    for j in range(1, cols+1):
        print count(i,j),
        sys.stdout.softspace=0
    print ""

        
    


