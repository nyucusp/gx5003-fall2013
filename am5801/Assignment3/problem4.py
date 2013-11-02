# Awais Malik
# Assignment 3
# Problem 4
# Collaborated with Schuyler Poukish

grid =  open('input4.txt').readlines()
grid = [line.strip() for line in grid]
grid = [line for line in grid if len(line) > 0]

num_grids = int(grid.pop(0))

def Direction(table, row_num, col_num, row_diff, col_diff):
    word = ''
    while (row_num >= 0 and
            row_num < len(table) and
            col_num >= 0 and
            col_num < len(table[row_num])):
        word += table[row_num][col_num]
        col_num += col_diff
        row_num += row_diff
    return word

for case in range(num_grids):
    parts = grid.pop(0).split()
    num_rows = int(parts[0])
    num_cols = int(parts[1])

    table = [line.lower() for line in grid[:num_rows]]
    grid = grid[num_rows:]

    num_words = int(grid.pop(0))
    words = [line.lower() for line in grid[:num_words]]
    grid = grid[num_words:]

    for key_word in words:
        found = False
        for row_num in range(num_rows):
            for col_num in range(num_cols):
                if(key_word == Direction(table, row_num, col_num, 0, 1)[:len(key_word)] or
                key_word == Direction(table, row_num, col_num, 0, -1)[:len(key_word)] or
                key_word == Direction(table, row_num, col_num, 1, 0)[:len(key_word)] or
                key_word == Direction(table, row_num, col_num, -1, 0)[:len(key_word)] or
                key_word == Direction(table, row_num, col_num, 1, 1)[:len(key_word)] or
                key_word == Direction(table, row_num, col_num, 1, -1)[:len(key_word)] or
                key_word == Direction(table, row_num, col_num, -1, 1)[:len(key_word)] or
                key_word == Direction(table, row_num, col_num, -1, -1)[:len(key_word)]):
                    if not found:
                        print row_num + 1, col_num + 1
                        found = True
    print ''