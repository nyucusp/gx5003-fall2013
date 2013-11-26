"""
readdat.py. methods for reading comma separated files
"""

from datetime import datetime

def read_comma_separated_file(filename):
    """
        reads the header and data from a comma separated file.

        returns (header, data)
    """
    header = []
    data = []
    with open(filename, 'r') as fptr:
        # Read the header.
        header = [x.strip() for x in fptr.readline().split(',')]

        while True:
            line = fptr.readline()

            if not line:
                break

            data.append([x.strip() for x in line.split(',')])

    return header, data

class ActionFileReader(object):
    """ Class for handling reading the actions file.
    Class behaves like a generator/iterator """

    filename = 'actions-fall-2007.dat'
    line_count = 0

    def __init__(self):
        self.fptr = open(self.filename, 'r')

        # read the header... we don't care about it.
        self.fptr.readline()

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        """ read a line if it's available. return it as a datetime.
        else, thow StopIteration() """
        line = self.fptr.readline()
        if not line:
            raise StopIteration()

        self.line_count += 1
        return datetime.strptime(line.strip(), '%Y-%m-%d %H:%M:%S')
