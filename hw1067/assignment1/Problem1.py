# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys

# <codecell>

import sys
input_Range = map(int,sys.argv[1:])
happy = 0
for x in range(input_Range[0], input_Range[1]+1):
    input_num = x
    counter = 1 
    while input_num > 1:
        if input_num%2 == 0:
            input_num /= 2
        else:
            input_num *= 3
            input_num += 1
        counter += 1
        if input_num == 1:
            if counter > happy:
                happy = counter

print input_Range[0], input_Range[1], happy
