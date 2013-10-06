import sys



"""
SECTION 1: INPUT PARSING
"""



"""
First we open the text file and save the lines to the list input_lines.  Please note
this program is NOT robust enough to handle input that differs even slightly from
the format in the problem (e.g. if there are TWO blank lines between cases, as opposed
to ONE, there will be an error).  Also, if there is more than ONE blank line at the
end of input2.txt, there will be an error.

Note that the initial structure of this code will be very similar to that of problem 2,
because we will parse the file and organize the input in a similar fashion.
"""
inputfile = open('input4.txt', 'r')

input_lines = []
for line in inputfile:
    input_lines.append(line)
inputfile.close()



"""
Now we parse the file and save each case as a list in case_list (so case_list is a list
of lists).  Here, a case starts with two integers (the size of the grid), followed by
the grid, then another integer(the number of words to look for), followed by the 
list of words to look for.  Note that we don't make use of
the number of cases (the first line of input4.txt).
"""
case_list = []
newline_markers=[]
for i in range(1,len(input_lines)):
    if input_lines[i] == '\n':
        newline_markers.append(i)
newline_markers.append(len(input_lines))

for k in range(0,len(newline_markers)-1):
    case_list.append(input_lines[newline_markers[k]+1:newline_markers[k+1]]) 










"""
SECTION 2: DEFINING FUNCTIONS TO SOLVE THE PROBLEM
"""



"""
Now we define a function, wordsearch_results, that takes a case as input, and outputs
the starting coordinates of all words to be found.  We will (eventually) call this 
function for each case in case_list.  In this function, we first split the case into 
three structures.  The first is grid_size, a list whose two elements are the number of 
rows and columns of the grid.  The second is grid_rows, a list whose elements are the 
rows of the grid. The third is words_list, which is just a list of
all words to search for.  We will pass this information to another function called 
wordsearch_solver, which will take grid_size, grid_rows, and words_list as inputs, and
output the starting coordinates of all words in words_list.
"""

def wordsearch_results(current_case):
    numrows = int(current_case[0].split()[0])
    numcols = int(current_case[0].split()[1])
    grid_size = [numrows, numcols]
    
    grid_rows = []
    for i in range(1,numrows+1):
        grid_rows.append(current_case[i])
    
    words_list = []
    for i in range(numrows+2, len(current_case)):
        words_list.append(current_case[i][:-1])
        
    wordsearch_solver(grid_size, grid_rows, words_list)



"""
We now define the main function of this assignment, wordsearch_solver.  

The first thing that wordsearch_solver does is to make the grid in a form convenient
for searching, by calling the function grid_formatter, defined below, and saving the 
returned dict as grid.  

Next, for each word in the word list, wordsearch_solver iterates through the grid
(from top to bottom and left to right), calling the function words_at_coordinate 
(defined and explained after grid_formatter, below) and comparing the result 
with the given word (which we convert to lowercase to allow case-independent
comparison).

Finally, for each key in the word list, we output the first element in its value
list (the topmost, leftmost pair of coordinates), in the format specified in the
problem description.
"""
def wordsearch_solver(g_size, g_rows, w_list):
    grid = grid_formatter(g_size, g_rows)
    
    for testword in w_list:
        testword_coordinates = []
        for i in range(1,g_size[0]+1):
            for j in range(1, g_size[1]+1):     
                for word in words_at_coordinate((i,j), len(testword), grid):
                    if testword.lower() == word:
                        testword_coordinates.append((i,j))
        print str(testword_coordinates[0][0]) + " " + str(testword_coordinates[0][1])
   
   
                
"""
Here we define grid_formatter.  Grid_formatter will return a dict whose keys are 
coordinate tuples and whose values are the letter in the corresponding entry of the 
input grid.  However, we use a trick to make border cases easy (this is the same trick 
I used in my answer to the minesweeper problem in assignment 1).  Namely, we embed our
grid in a larger grid, where all the values corresponding to coordinates in the large
grid (but not the input grid) are the dummy value "*".  

Specifically, suppose that r, c, are the number of rows and columns of our input grid.
Let m = max(r,c).  Then we make a grid of size (2m+r)x(2m+c).  The (i,j)th entry of
our input grid will be the (i, j)th entry of our formatted grid.  All other entries
of the formatted grid will be "*".  For our formatted grid, the keys will be of the 
form (k, l), where k goes from (-m+1) to (r+m), and l goes from (-m+1) to (c+m).

Note that this is (slightly) overkill; we could get by
by adding m-1 "dummy" rows and columns (rather than m "dummy" rows and columns)
all around the input grid.  In fact, we could get away with merely adding
k-1 "dummy" rows and columns, where k is the maximum length of any word
in words_list, but there is no harm in adding a bit extra!
"""
def grid_formatter(size, rows):
    n_rows = size[0]
    n_cols = size[1]
    m = max(n_rows, n_cols)
    big_grid = {}
    for i in range(-m + 1, m + n_rows + 1):
        for j in range(-m + 1, m + n_cols + 1):
            if (0 < i and i < n_rows + 1) and (0 < j and j < n_cols + 1):
                big_grid[(i,j)] = rows[i-1][j-1]
            else:
                big_grid[(i,j)] = "*"
    
    return big_grid



"""
Here we define the function words_at_coordinate.  Words_at_coordinate takes three arguments,
a coordinate of the form (i,j), a number l, and a dict of the grid, and outputs a list 
of the 8 words (in the grid) that start at coordinate (i,j) and have length l.  
Note that we don't have to consider any kind of border case separately, because if 
we are near a border, some words may be composed partly or mostly of the character "*".  

For primarily aesthetic reasons, words_at_coordinate operates by calling the function
wac_vector 8 times ("wac" = "words at coordinate"), one for each integral multiple of
pi/4 in the range [0, 2pi).

wac_vector, defined after words_at_coordinate, takes a coordinate, a number l, a vector v 
(represented as a pair of numbers (a,b), where a and b are either 1, -1, or 0), and a
dict of the grid.  It returns the word in the grid that starts at the coordinate, 
has length l, and points in the direction of v.  

Note that we turn every returned word into all lowercase, so allow 
case-independent comparison later.
"""

def words_at_coordinate(coord, length, grid):
    wac_list = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                wac_list.append(wac_vector(coord, length, (i,j), grid))
    return wac_list


def wac_vector(coord, length, dir, grid):
    returned_word = ""
    for count in range(0, length):
        returned_word = returned_word + grid[(coord[0]-(count*(dir[1])), coord[1]+(count*(dir[0])))]
    return returned_word.lower()
  









"""
SECTION 3: OUTPUTTING THE RESULTS
"""


"""
Finally, for each case in case_list, we call wordsearch_results, and put a blank space
between each output.
"""
for case in case_list:
    wordsearch_results(case)
    print ""
