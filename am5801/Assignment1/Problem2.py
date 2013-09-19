# Awais Malik
# Assignment 1
# Problem 2
# First attempt
# This works for the two examples in the assignment,
# but there is something wrong that I could not figure out.

import sys

# Making an array which only contains the sequence
array = sys.argv[2:len(sys.argv)]

# Converting each element in the array from string to integer
for i in range(0,len(array)):
    array[i] = int(array[i])

# Creating the difference array
diff = []

# function to test whether a sequence is Jolly or not
def jolly_test(my_array):
    # Any sequence of single integer is Jolly
    if len(my_array) == 1:
        print "Jolly"
    # If no number is entered, invalid entry
    elif len(my_array) == 0:
        print "Invalid Entry"
    # Method to analyze sequence with more than one integers
    else:
        for i in xrange(1, len(my_array)):
            # Calculate difference between the next number and the current one
            diff.append(my_array[i] - my_array[i-1])
        # Count variable for checking that all numbers from 1 to n-1
        # are present in the diff array
        count = 1
        # Method to check that no two elements in the diff array are same
        for j in xrange(diff[0], diff[len(diff)-1]):
            for k in xrange(diff[0], diff[len(diff)-1]):
                if diff[k] != diff[j]:
                    count = count + 1 # Add 1 to count
                else:
                    print "Not Jolly"
                    return # End the program
        
        # Print Jolly if all counts from 1 to n-1 are found
        if count == diff[len(my_array)-2]:
            print "Jolly"

# Run the function on the sequence inputted in the command prompt
jolly_test(array)