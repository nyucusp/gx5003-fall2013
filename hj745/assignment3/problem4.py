#                   < algorithm >
# 1. find a particular word in the grid and print out the location of it
# 2. get the number of cases as integer and find a new waldorf with the number of cases
# 3. get the number of rows and columns as integet (1<= row AND col <= 50)
# 4. then, get the string input
# 5. the lengths of string should be the same as the number of col, and the number of string should be the same as the number of rows
# 6. get the number of words that should be found in the grid
# 7. get input as for finding words
# 8. find the particular word in the grid by directions of up, down, lef, right, and 4 of diagonal. 
# 9. once find the word, print out the starting point
# 10. if all of words are found, start from the #4 and repeat rest of steps until all of the cases finish

import sys

f = open('input4.txt', 'r') #open the input file
input = f.readlines() # read the whole file as a list of lines
line_index = 0 
line_index2 = int(input[line_index].replace('\n', ''))

while len(lines) != 0: # this is to find each case by finding the blank followed by the integer that represents the number of cases

    def fn_input_case_count():
        case_count = lines.read("*number") # get the number of cases that is represented as an integer followed by the blank line
    
    def fn_input_grid_size():
        line_index2.split() = [row,col]
 
def fn_input_grid(row, col):# this is to get the string input and make sure that the lengths of string is the same as the number of col,
                            # and the number of string is the same as the number of rows
    tb_grid = {}
    row_count = 1

    while row_count <= row :
        str_grid = line_index2
        str_grid = string.upper(str_grid)
        if col == string.len(str_grid):
            local tb_grid_col = {}
            for w in string.gmatch(str_grid, "%a"):
                tb_grid_col[tb_grid_col + 1] = w
            tb_grid[row_count] = tb_grid_col
            row_count = row_count + 1

    return tb_grid  

# find the particular word in the grid by directions of up, down, lef, right, and 4 of diagonal.

def fn_input_waldorfs():
    waldorf_count = 4 # get the number of words that should be found in the grid
    tb_waldorfs = {}
 
    i = 1
    while i <= waldorf_count: 
        str_waldorf = 4
        if nil != str_waldorf and "" != str_waldorf:
            str_waldorf = string.upper(str_waldorf)
            tb_waldorf = {}
            for w in string.gmatch(str_waldorf, "%a"):
                tb_waldorf[tb_waldorf + 1] = w
             
            tb_waldorfs[tb_waldorfs + 1] = tb_waldorf
            i = i + 1
    return tb_waldorfs

 def fn_where_is_real(tb_arg, tb_dir, tb_waldorf):
    
    local tb_grid, tb_result = tb_arg.tb_grid, tb_arg.tb_result
    local x, y, w, h, cur = tb_arg.x, tb_arg.y, tb_grid[1], tb_grid, 1
     
    while 1 <= x and x <= w and 1 <= y and y <= h and 0 != tb_waldorf and tb_grid[y][x] == tb_waldorf[cur]:
        if cur == tb_waldorf:
            return true
        x, y, cur = x + tb_dir.x, y + tb_dir.y, cur + 1
    return false

 def fn_where_is(tb_arg):
    for k, tb_waldorf in pairs(tb_arg.tb_waldorfs):
        for k, tb_dir in pairs(tb_arg.tb_directions):
            if true == fn_where_is_real(tb_arg, tb_dir, tb_waldorf):
                return true
    return false
 
def main():
    tb_directions ={{x=-1, y=-1}, {x=0, y=-1}, {x=1, y=-1},{x=-1, y= 0},{x=1, y= 0},{x=-1, y= 1}, {x=0, y= 1}, {x=1, y= 1}}
    case_count = fn_input_case_count()
     
    for i = 1, case_count, 1:
        grid_row, grid_col = fn_input_grid_size()
        tb_grid = fn_input_grid(grid_row, grid_col)
        tb_waldorfs = fn_input_waldorfs()
    
        local tb_arg = {}   
        tb_arg.tb_grid = tb_grid
        tb_arg.tb_waldorfs = tb_waldorfs
        tb_arg.tb_directions = tb_directions
         
        for row = 1, tb_grid, 1:
            for col = 1, tb_grid[row], 1:
                tb_arg.x, tb_arg.y = col, row
                if true == fn_where_is(tb_arg):
                    print(row, col)

if __name__ == '__main__':
    main()
