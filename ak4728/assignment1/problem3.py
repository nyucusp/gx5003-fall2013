import sys
def wrap(grid, ROWS, COLS):
    return (['.' * (COLS+2)] +
           ['.'+r+'.' for r in grid] +
           ['.' * (COLS+2)])
def neighbor(r, c, grid):
    if grid[r][c] == '*':
        return '*'
    else:
        neighbors = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        #print [n for n in map(lambda (dr,dc): grid[r+dr][c+dc], neighbors)]
        return str(len([n for n in map(lambda (dr,dc): grid[r+dr][c+dc], neighbors) if n == '*']))
def mines_counter(grid):
    grid = [r.strip() for r in grid.split("\n") if len(r) > 0]
    print grid
    ROWS, COLS = len(grid), len(grid[0])
    wrapped_grid = wrap(grid, ROWS, COLS)
    #print wrapped_grid
    #print neighbor(1, 2, wrapped_grid)
    return ([''.join([neighbor(r+1, c+1, wrapped_grid) 
                for c in xrange(COLS)])
            for r in xrange(ROWS)])

print mines_counter("""
    *... 
    .... 
    .*.. 
    ....
""")
