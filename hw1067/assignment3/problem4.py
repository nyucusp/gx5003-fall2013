#Problem 4
#Haozhe Wang

""""General solution:
read the file, take the table out and put in a new list(lists of a list);
convert all the letters to  lowercase;
also, store the check words in a different list;
look for the first letter of the check words, then search for the letters in the table;
search from eight directions, such as from (x,y) to (x+-len(woldorf), y+-(len(woldorf)) if w is found at (x,y);
if such check was finished, export the (x,y) location;
if not, go to next word;
names are the variables. len(name) determines if the word can be found.
do the same for next group of input in the file.
"""

    
#open and read file
lines =  open('input4.txt').readlines()#note, not readline() here
lines = [line.strip() for line in lines]
#print lines 
lines = [line for line in lines if len(line) > 0]  # discard empty lines
#print lines 

def knowitall(table, row_number, col_number, end_row, end_col):
    rubics = ''
#method: split the "8 11" input, and use them as column and row numbers
    while (row_number >= 0 and
            row_number < len(table) and
            col_number >= 0 and
            col_number < len(table[row_number])):
        rubics += table[row_number][col_number]
        col_number += end_col
        row_number += end_row
    return rubics
    #print rubics

#get number of cases
cases = int(lines.pop(0))

#find a way to use line "8 11"
for c in range(cases):
    lame = lines.pop(0).split()
    num_row = int(lame[0])
    num_col = int(lame[1])

    # get rows for table and discard them
    table = [line.lower() for line in lines[:num_row]]
    lines = lines[num_row:]
    #print lines

    #
    num_name = int(lines.pop(0))
    #print num_name
    names = [line.lower() for line in lines[:num_name]]#lowercase names for search
    #print names
    lines = lines[num_name:]
    #print lines


    print "Senario: ","No.", c + 1
    for name in names:
        found = False
        for row_number in range(num_row):
            for col_number in range(num_col):
                # there are eight possible ways/directions to look for a word in a table.
                if (name == knowitall(table, row_number, col_number, 0, 1)[:len(name)] or
                    name == knowitall(table, row_number, col_number, 1, 0)[:len(name)] or
                    name == knowitall(table, row_number, col_number, -1, 0)[:len(name)] or
                    name == knowitall(table, row_number, col_number, 0, -1)[:len(name)] or
                    name == knowitall(table, row_number, col_number, 1, -1)[:len(name)] or
                    name == knowitall(table, row_number, col_number, -1, 1)[:len(name)] or
                    name == knowitall(table, row_number, col_number, 1, 1)[:len(name)] or
                    name == knowitall(table, row_number, col_number, -1, -1)[:len(name)]):
                    # print the coordinate(x,y) for each result found.
                    if not found:
                        print row_number + 1, col_number + 1
                        found = True
#not tested for more than one senario. fixed a problem with the word-checking directions.
    print
