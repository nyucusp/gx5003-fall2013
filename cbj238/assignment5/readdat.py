"""
readdat.py. methods for reading comma separated files
"""

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


