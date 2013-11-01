def main():
    f = open('input1.txt', 'r') #open the input file
    input = f.readlines() # read the whole file as a list of lines
    line_index = 0 
    line_index2 = int(input[line_index].replace('\n', '')) # this line is to set the number of student in each trip (the number of student is formatted as integer)
                                                           
    while line_index2 != 0:
        sum = 0.00 # set the initial value of the computed money
        line = []
        for i in range(line_index2): # this loop is for setting the amount spent by a student in dollars and cents
            sum += float(input[line_index + i + 1].replace('\n', '')) #the amount spent by a student in dollars and cents is formatted as float
            line.append(float(input[line_index + i + 1].replace('\n', ''))) # add line
        total = sum/line_index2
        line_index += line_index2 + 1
        minimum = 0
        for j in line: # this loop is for finding the minimum amount
            if float(j - round(total,2)) > 0:
                minimum += j-total
        print "$ %0.2f" % minimum #show the minimum number to two decimal places
        line_index2 = int(input[line_index].replace('\n', ''))# to find the next chunk in the input file,such as the number of student and amount spent by a student in dollars and cents
    
if __name__ == '__main__':
    main()
