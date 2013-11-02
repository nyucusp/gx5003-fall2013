#input
#so we want to input a positive integer on a line by itself indicating the number of cases
#followed by a blank line
#In each two consecutive cases there is also a blank line
#Each case begins with a pair of integers m followed by n on asingle line
# the next m lines contain n letters each,representing the grid of letters where the word must be found

#output
#you want to ouput a pair of integers representing each word and its locatio in the corresponding grid
#first integer us the line in the grid where the first letter of the given word can be found
#second integer is the column in the grid where the irst letter of the given word can be found
#if two words are uppermost , output the leftmost of the occurence.
def getInDirection(table, row_num, col_num, diff_row, diff_col):
    s = ''
# This loop is necessary as  it keeps the pointer in the grid

    while (row_num >= 0 and
            row_num < len(table) and
            col_num >= 0 and
            col_num < len(table[row_num])):
        s += table[row_num][col_num]
        col_num += diff_col
        row_num += diff_row
    return s

#read in file
lines =  open('input4.txt').readlines()
lines = [line.strip() for line in lines]  # clean up lines
lines = [line for line in lines if len(line) > 0]  # discard empty lines

#get number of cases
cases = int(lines.pop(0))

# For every case you have...
for case in range(cases):
    # read line which gives rows and cols, split it up, save as ints,
    # and then remove the line (pop).
    parts = lines.pop(0).split()
    num_rows = int(parts[0])
    num_cols = int(parts[1])

    # get rows for table and discard them
    table = [line.lower() for line in lines[:num_rows]]
    lines = lines[num_rows:]

    # read names to look for
    num_names = int(lines.pop(0))
    names = [line.lower() for line in lines[:num_names]]
    lines = lines[num_names:]

    print "Case: ", case + 1
    # As long as there are "names"/words to look for, search the table for them
    for name in names:
        found = False
        # The net loops simply move through all the coordinates of the table
        for row_num in range(num_rows):
            for col_num in range(num_cols):
                # Once we are at a coordinate, we compare the name/word to each string from every direction around that point
                # I use  -1, 0, or 1 to indicate direction to look.
                #  "[:len(name)]" portion, this says that if the string 
                #  receives is longer than the word, cut  off the extra characters
               
                if (name == getInDirection(table, row_num, col_num, 0, 1)[:len(name)] or
                        name == getInDirection(table, row_num, col_num, 0, -1)[:len(name)] or
                        name == getInDirection(table, row_num, col_num, 1, 0)[:len(name)] or
                        name == getInDirection(table, row_num, col_num, -1, 0)[:len(name)] or
                        name == getInDirection(table, row_num, col_num, 1, 1)[:len(name)] or
                        name == getInDirection(table, row_num, col_num, 1, -1)[:len(name)] or
                        name == getInDirection(table, row_num, col_num, -1, 1)[:len(name)] or
                        name == getInDirection(table, row_num, col_num, -1, -1)[:len(name)]):
                    # If a word is found, print the coordinates
                    if not found:
                        print row_num + 1, col_num + 1
                        found = True
        
    # Blank space between cases.
    print
