#Aliya Merali
#Assignment 3
#Problem 4

#Write functions to call later:
def case_break(x):#Find out the range of data for each case by marking the index at start, new lines, and end - with raw data, less first two lines as input
    case_break = [0]
    i = 1
    for element in x:
        if element == '\n':
            case_break.append(i-1)
        i = i + 1
    case_break.append(len(x))
    return case_break

def data_parse(x_case): #take one case and parse the data 
    if x_case[0] == '\n':#get rid of extra '\n' from casebreak
        del(x_case[0])
    temp = x_case[0].split(' ')
    r = temp[0] #number of rows of grid
    c = temp[1] #number of columns in grid
    letters = []
    words = []
    i = 0
    for element in x_case:
        if 0 < i <=  int(r): #elem 2 - r
            letters.append(element.strip())
        elif (int(r)+ 1) < i  <= len(x_case): # elem r+1 - end
            words.append(element.strip())
        i = i + 1
    return letters, words

def analyze_letters(parsed_data):
    letters = parsed_data[0]
    words = parsed_data[1]
    new_letters = []
    new_words = []
    for letter in letters:#break up grid and words into letters
        new_letters.append(list(letter))
    for word in words:
        new_words.append(list(word))
    i = 0
    for word in new_words:#for each word in the list to search for
        while i < len(word):#iterate through the elements of word
            r = 0
            for letter in new_letters: #iterate through elements of letter
                c = 0
                while c < len(letter):
                    if word[i].lower() == letter[c].lower(): #if match, iterate surroundings
                        print 'column '+ str(c) + ' row ' + str(r)
                        print 'Match at '+str(i)+' '+str(c)
                        print word
                        print letter
                        print
                    c = c + 1
                r = r + 1
            i = i + 1
        
    print 
    print

#Apply functions to data:
input =  open('input4.txt','r')
data = input.readlines()
data = data[2:]

cases = case_break(data)
j = 0
while j < (len(cases) - 1):
    x_case = []
    index = cases[j]
    while ((cases[j]) <= index < (cases[j+1])):
        x_case.append(data[index])
        index = index + 1
    parsed_data = data_parse(x_case)
    analyze_letters(parsed_data)
    j = j + 1
