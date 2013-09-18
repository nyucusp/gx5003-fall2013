import sys

input = (sys.argv)
input.pop(0)


first_parameter = int(input[0])
second_parameter = int(input[1])


"""
The following function takes an integer and gives the length of its cycle, as defined
in the problem statement.  The variable k is a counter for the cycle length.
"""

def cycle_length(n):
    k = 0
    while n != 1:
        if n%2 == 0:
            n = n/2
            k += 1
        elif n%2 != 0:
            n = 3*n + 1
            k += 1
    return k+1
          
list_of_lengths = []


"""
Now we put all the cycle lengths into a list, and print the max of these lengths
as a string.

"""

for i in range(min(first_parameter, second_parameter), max(first_parameter, second_parameter)+1):
    list_of_lengths.append(cycle_length(i))

print str(first_parameter) + " " + str(second_parameter) + " " + str(max(list_of_lengths))
