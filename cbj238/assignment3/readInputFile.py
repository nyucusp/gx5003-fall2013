
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
    def __init__(self):
        self.data = []
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
    def __init__(self):
        self.data = []
        InputFile.__init__(self, 'input2.txt')
        self.parse()

    def parse(self):
        ''' State machine that handles the input. States:
        0. Line contains the number of cases.
        1. blank line after a case entry
        2. m where m is the number of candidates / lines to follow.
        3. the m candidates
        4. Voting data. If it is blank (and we haven't reached the number of cases), go 2 the next time.
        5. End
        '''
        state = 0
        n = -1      # Outer loop (cases) size
        m = -1      # inner looop (candidates) size
        n_idx = -1
        m_idx = -1
        candidates = []
        votes = []

        for line in self.handle:
            # print state, "|" + line.strip() + "|", n, n_idx, m, m_idx
            if state is 0:
                n = int(line)
                state = 1  
            elif state is 1:
                if line.strip() is not "":
                    pass  # maybe throw an error here?
                n_idx += 1
                state = 2

            elif state is 2:
                m = int(line)
                m_idx = 0
                state = 3
            elif state is 3:
                candidates.append(line.strip())
                m_idx += 1

                if m_idx >= m:
                    state = 4
            elif state is 4:
                if line.strip() is not "":
                    votes.append([int(x) for x in line.split()])
                else:
                    n_idx += 1

                    self.data.append((candidates, votes))
                    candidates = []
                    votes = []

                    if n_idx >= n:
                        state = 5    
                    else:
                        state = 2

            else:
                break;

        if candidates is not [] and votes is not []:
            self.data.append((candidates, votes))

class Problem3Input(InputFile):
    pass

class Problem4Input(InputFile):
    pass
