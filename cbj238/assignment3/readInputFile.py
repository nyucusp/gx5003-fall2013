def SplitAuthors(authorString):
    '''
        Given a string containing:
        Last Name, First Name, LastName, FirstName, ...
        return a list of ["LastName, Firstname", ...]
    '''
    authorList = []
    tmpStr = authorString
    endIdx = 0
    while endIdx is not -1:
        endIdx = tmpStr.find(',', tmpStr.find(',') + 1)
        if endIdx is not -1:
            authorList.append(tmpStr[:endIdx].strip())
        else:
            authorList.append(tmpStr.strip())
        tmpStr = tmpStr[endIdx+1:]
    return authorList

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
    def __init__(self):
        self.data = []
        InputFile.__init__(self, 'input3.txt')
        self.parse()

    def parse(self):
        ''' State machine that handles the input. States:
        0. Line contains the number of scenarios to follow.
        1. Line contains natrual numbers P N, P Papers to follow, then N names to follow.
        2. read P Papers
        3. read N names
        4. Exit
        '''
        state = 0
        s = -1      # Outer loop (scenarios) size
        n = -1      # inner looop (N) size
        p = -1      # P
        s_idx = -1
        p_idx = -1
        n_idx = -1
        papers = []
        names = []
        for line in self.handle:
            # print state, s, n, p, "|" + line + "|"
            if state is 0:
                s = int(line.strip())
                state = 1
            elif state is 1:
                line = line.strip()
                if line is not "":
                    (p, n) = [int(x) for x in line.split()]
                    state = 2
                    p_idx = 0
                    n_idx = 0
                else:
                    state = 4
            elif state is 2:
                (authors, title) = line.split(':')
                
                papers.append((SplitAuthors(authors), title.strip()))
                p_idx += 1

                if p_idx is p:
                    state = 3
            elif state is 3:
                names.append(line.strip())
                n_idx += 1

                if n_idx is n:
                    self.data.append((papers, names))

                    papers = []
                    names = []
                    s_idx += 1

                    if s_idx is s:
                        state = 4
                    else:
                        state = 1
            elif state is 4:
                break;

        if papers is not [] and names is not []:
            self.data.append((papers, names))


class Problem4Input(InputFile):
    def __init__(self):
        self.data = []
        InputFile.__init__(self, 'input4.txt')
        self.parse()

    def parse(self):
        ''' State machine that handles the input. States:
        0. Line contains the number of cases to follow.
        1. a blank line
        2. contains "m n", which is m lines and n characters
        3. read m lines (with n characters each)
        4. contains k, the number of words to follow
        5. read k lines
        6. Exit
        '''
        state = 0
        s = -1      # Outer loop (scenarios) size
        m = -1      # m lines
        n = -1      # n characters
        k = -1      # words to search
        p = -1      # P
        s_idx = -1
        m_idx = -1
        k_idx = -1
        charGrid = []
        words = []
        for line in self.handle:
            line = line.strip()
            print state, s_idx, m_idx, k_idx, "|" + line + "|"
            if state is 0:
                s = int(line)
                state = 1
            elif state is 1:
                state = 2
            elif state is 2:
                if line is not "":
                    (m, n) = [int(x) for x in line.split()]
                    state = 3
                    m_idx = 0
                    k_idx = 0
                else:
                    state = 6
            elif state is 3:
                charGrid.append(line)
                m_idx += 1

                if m_idx is m:
                    state = 4
            elif state is 4:
                k = int(line)
                state = 5
            elif state is 5:
                words.append(line)
                k_idx += 1

                if k_idx is k:
                    self.data.append((charGrid, words))

                    charGrid = []
                    words = []
                    s_idx += 1

                    if s_idx is s:
                        state = 6
                    else:
                        state = 1
            elif state is 6:
                break

        if charGrid is not [] and words is not []:
            self.data.append((charGrid, words))


