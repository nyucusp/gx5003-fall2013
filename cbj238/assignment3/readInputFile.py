
class InputFile:
    handle = None
    def __init__(self, filename):
        self.handle = open(filename, 'r')

class Problem1Input(InputFile):
    '''
    Problem 1's input contains:
    an integer n followed by n lines of prices.
    repeats until it sees n==0

    data is formatted as [(<n>, [<data>]),...]
    '''
    data = []
    def __init__(self):
        InputFile.__init__(self, 'input1.txt')

        self.parse()

    def parse(self):
        ''' State machine that handles input. Two states:
         0. line contains 'n'
         1. line cointains data.
         2. stop! '''
        state = 0
        n = -1
        costs = []
        idx = -1

        for line in self.handle:
            if state is 0:
                n = int(line)
                if n > 0 and n <= 1000:
                    state = 1
                    idx = 0
                else:
                    state = 2
            elif state is 1:
                if idx < n:
                    costs.append(float(line))
                    idx += 1
                
                # When you've finished with the data, append it to self.data
                if idx == n:
                    state = 0
                    self.data.append( (n, costs) )
                    n = -1
                    costs = []
            else:
                break
    

class Problem2Input(InputFile):
    pass

class Problem3Input(InputFile):
    pass

class Problem4Input(InputFile):
    pass
