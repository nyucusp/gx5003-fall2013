# create a set of functions which will search the grid for a given word
# this needs to account for every direction, using the starting location
# as the pivot point. These are not searching for words, but instead
# simply collecting a string of letters in that direction.
#####################################################
# def getRight(table, row_num, col_num):
# This string will hold the characters I find in that direction.
#     s = ''
# This loop limits the string length by keeping the search within teh table
#     while col_num < len(table[row_num]):
# this line adds the character which is at that location in the table to the string
#         s += table[row_num][col_num]
# this line moves the pointer to the next col.
#         col_num += 1
# This returns the string for analysis
#     return s

# def getLeft(table, row_num, col_num):
#     s = ''
#     while col_num >= 0:
#         s += table[row_num][col_num]
#         col_num -= 1
#     return s

# def getUp(table, row_num, col_num):
#     s = ''
#     while row_num >= 0:
#         s += table[row_num][col_num]
#         row_num -= 1
#     return s

# def getDown(table, row_num, col_num):
#     s = ''
#     while row_num < len(table):
#         s += table[row_num][col_num]
#         row_num += 1
#     return s

# def getUpRight(table, row_num, col_num):
#     s = ''
#     while row_num >= 0 and col_num < len(table[row_num]):
#         s += table[row_num][col_num]
#         col_num += 1
#         row_num -= 1
#     return s
##################################################
# These functions can then actually be replaced by a more straight forward
# design, capable of looking in every direction
# This function is given below.
# The table, starting row, and starting column are passed in, just like
# the previous functions. The difference is that I also pass in diff_row
# and diff_col, which will be either a -1, 0, 1, that indicate a change
# in direction on teh x-y axis

def getInDirection(table, row_num, col_num, diff_row, diff_col):
    s = ''
# This loop is different because it keeps the pointer in the grid
# no matter what direction it could be looking in.
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
                # Once we are at a coordinate, I compare the name/word to each
                # of the strings from every direction pivoting around that point.
                # Notice how I'm using -1, 0, or 1 to indicate direction to look.
                # Also, notice the "[:len(name)]" portion, this says that
                # if the string I receive is longer than the word, chop off the
                # extra characters.
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
        # While the instructions indicated that all words were present in the grid,
        # i felt that it was a good practice to alert the user if there was a
        # missing word in some instance
        # if not found:
        #     print name, 'not found'

    # Blank space between cases.
    print
