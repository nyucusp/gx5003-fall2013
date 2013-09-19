#!/usr/bin/python
"""
Christopher Jacoby
cbj238@nyu.edu
GX-5003
Assignment 1 problem 3

Solution for problem defined at: http://www.programming-challenges.com/pg.php?page=downloadproblem&format=html&probid=110102
"""

import sys

class InputError(Exception):
    def __init__(self, msg):
        self.msg = msg

class MinesweeperBoard():
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.field = []

    def __str__(self):
        string = "{0} {1}\n".format(self.m, self.n)
        for i in xrange(self.m):
            for j in xrange(self.n):
                string += self.field[i][j]
            string += "\n"
        return string
        
    def add_line(self, lineString):
        '''
        adds a line from the input to the field list, splitting it so you can address each
        point individually.
        '''
        self.field.append(list(lineString))

    def get_field_mask(self):
        mask = ""

        for y in xrange(self.m):
            for x in xrange(self.n):
                mask += str(self.get_mask_for_point(y, x))
            mask += "\n"

        return mask

    def get_mask_for_point(self, y, x):
        '''
        returns the number of adjacent mines for a point m, n
        '''
        ret = None
        # if it's a *, return a *
        if self.field[y][x] == '*':
            ret = self.field[y][x]
        # else, it's a '.' - need to look at the adjacent ones
        else:
            ret = 0
            # N
            if y > 0 and y < self.m:
                # NW
                if x > 0 and x < self.n and self.field[y-1][x-1] == '*':
                    ret += 1
                # NN
                if self.field[y-1][x] == '*':
                    ret += 1
                # NE
                if x >= 0 and x < (self.n - 1) and self.field[y-1][x+1] == '*':
                    ret += 1
            # S
            if y >= 0 and y < (self.m - 1):
                #SW
                if x > 0 and x < self.n and self.field[y+1][x-1] == '*':
                    ret += 1
                #SS
                if self.field[y+1][x] == '*':
                    ret += 1
                #SE
                if x >= 0 and x < (self.n - 1) and self.field[y+1][x+1] == '*':
                    ret += 1
            # E
            if x >= 0 and x < (self.n - 1) and self.field[y][x+1] == '*':
                ret +=1
            # W
            if x > 0 and x < self.n and self.field[y][x-1] == '*':
                ret += 1
        
        return ret    

def parse_input(strIn):
    '''
    The input is a single string, with multiple lines;
     the first line contains two numbers m and n, followed by a grid of 
     n lines, each containing m characters.
    The input can repeat multiple times; it will stop when m and n are 0
    The function returns a list containing each board.
    '''
    lines = strIn[0].split('\\n')
    return parse_boards(lines)

def parse_boards(lines):
    '''
    This function uses a state machine to read through the board strings.
    0 = read the string containing m and n
    1 = read a line containing n board characters
    2 = end / indeterminate
    '''
    state = 0
    i_m = 0          # the index in the current m
    board_list = []
    this_board = None

    for line in lines:
        if state == 0:
            m, n = [int(x) for x in line.split()]
            if m!=0 and n!=0:
                this_board = MinesweeperBoard(m, n)
                state = 1
                i_m = 0
            else:
                state = 2
        elif state == 1:
            if i_m <= this_board.m:
                this_board.add_line(line)
                i_m += 1

            # if we've finished this board, add it and move on.
            if i_m == this_board.m:
                board_list.append(this_board)
                state = 0
                i_m = 0
        elif state == 2:
            break

    return board_list
    
def main(args):
    try:
        mine_fields = parse_input(args)

        for i in xrange(len(mine_fields)):
            print "Field #", i + 1, ":\n", mine_fields[i].get_field_mask()

    except InputError as e:
        print "Input Error: {0}".format(e.msg)
    except ValueError as e:
        print "Invalid input! Try again..."

if __name__ == "__main__":
    main(sys.argv[1:])
