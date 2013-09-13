import sys

input = (sys.argv)
input.pop(0)

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

for i in range(min(int(input[0]), int(input[1])), max(int(input[0]), int(input[1]))+1):
    list_of_lengths.append(cycle_length(i))

print input[0] + " " + input[1] + " " + str(max(list_of_lengths))


