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

def find_firsts(parsed_data):#Finds all locations of the first letter 
    letters = parsed_data[0]
    words = parsed_data[1]
    new_letters = []
    new_words = []
    for letter in letters:#break up grid and words into lists of letters
        new_letters.append(list(letter))
    for word in words:
        new_words.append(list(word))
    location_first = {}
    locations = []
    for word in new_words:#for each word in the list to search for
        r = 0
        while r < (len(new_letters)): #iterate through elements of letter
            c = 0
            while c < len(new_letters[0]):
                locations = []
                if word[0].lower() == new_letters[r][c].lower(): #create a dictionary with location of first letters in grid with (r, c) coordinates
                    locations.append(r)
                    locations.append(c)
                    if word[0] in location_first:
                        location_first[word[0]].append(locations)
                    else:
                        location_first[word[0]] = []
                        location_first[word[0]].append(locations)
                c = c + 1
            r = r + 1
    return location_first    

def cell_search(x, y, goal_val, rows, cols, list_name): #function return vals in surrounding cells
    if x<0 or y<0 or x>=rows or y>=cols:
        return False
    if list_name[x][y].lower() == goal_val.lower():
        return True
    else:
        return False

def find_words(parsed_data, location_first):
    letters = parsed_data[0]
    words = parsed_data[1]
    new_letters = []
    new_words = []
    final_locations={}
    for letter in letters:#break up grid and words into lists of letters
        new_letters.append(list(letter))
    for word in words:
        new_words.append(list(word))
    for new_word in new_words:
        #print new_word
        for new_letter in new_letters:
            #print new_letter
            for item in location_first.items():
                first_letter = item[0]
                locations = item[1]
                for location in locations:
                    r = location[0]
                    c = location[1]
                    r_init = location[0]
                    c_init = location[1]
                    n = 1
                    final_loc_store = []
                    if first_letter == new_word[0]:
                        while cell_search((r-1), (c-1), new_word[n], len(new_letters), len(new_letters[0]), new_letters) == True:
                            r = r - 1
                            c = c - 1
                            if n == len(new_word)-1:
                                #print ' Final Answer for ' + str(new_word) + str(location)
                                final_loc_store.append(r_init)
                                final_loc_store.append(c_init)
                                word = ''.join(new_word)
                                if word in final_locations:
                                    final_locations[word].append(final_loc_store)
                                else:
                                    final_locations[word] = []
                                    final_locations[word].append(final_loc_store)
                            else: 
                                n = n + 1
                        while cell_search(r-1, c, new_word[n], len(new_letters), len(new_letters[0]), new_letters) == True:
                            r = r - 1
                            c = c
                            if n == len(new_word) - 1:
                               # print 'final location is at ' + str(new_word) + ' is at ' + str(location)
                                final_loc_store.append(r_init)
                                final_loc_store.append(c_init)
                                word = ''.join(new_word)
                                if word in final_locations:
                                    final_locations[word].append(final_loc_store)
                                else:
                                    final_locations[word] = []
                                    final_locations[word].append(final_loc_store)
                            else:
                                n = n + 1 
                        while cell_search(r-1, c+1, new_word[n], len(new_letters), len(new_letters[0]), new_letters) == True:
                            r = r - 1
                            c = c + 1
                            if n == len(new_word) - 1:
                                #print 'final location is at ' + str(new_word) + str(location)
                                final_loc_store.append(r_init)
                                final_loc_store.append(c_init)
                                word = ''.join(new_word)
                                if word in final_locations:
                                    final_locations[word].append(final_loc_store)
                                else:
                                    final_locations[word] = []
                                    final_locations[word].append(final_loc_store)
                            else: 
                                n = n + 1
                        while cell_search(r, c-1, new_word[n], len(new_letters), len(new_letters[0]), new_letters) == True:
                            r = r 
                            c = c - 1
                            if n == len(new_word) - 1:
                                #print ' final location is at ' + str(new_word) + str(location)
                                final_loc_store.append(r_init)
                                final_loc_store.append(c_init)
                                word = ''.join(new_word)
                                if word in final_locations:
                                    final_locations[word].append(final_loc_store)
                                else:
                                    final_locations[word] = []
                                    final_locations[word].append(final_loc_store)
                            else:
                                n = n + 1
                        while cell_search(r, c+1, new_word[n], len(new_letters), len(new_letters[0]), new_letters) == True:
                            r = r
                            c = c + 1
                            if n == len(new_word) - 1:
                                #print 'final location is at ' + str(new_word) + str(location)
                                final_loc_store.append(r_init)
                                final_loc_store.append(c_init)
                                word = ''.join(new_word)
                                if word in final_locations:
                                    final_locations[word].append(final_loc_store)
                                else:
                                    final_locations[word] = []
                                    final_locations[word].append(final_loc_store)
                            else:
                                n = n + 1
                        while cell_search(r+1, c-1, new_word[n], len(new_letters), len(new_letters[0]), new_letters) == True:
                            r = r + 1
                            c = c - 1
                            if n == len(new_word)- 1: 
                                #print 'final location is at ' + str(new_word) + str(location)
                                final_loc_store.append(r_init)
                                final_loc_store.append(c_init)
                                word = ''.join(new_word)
                                if word in final_locations:
                                    final_locations[word].append(final_loc_store)
                                else:
                                    final_locations[word] = []
                                    final_locations[word].append(final_loc_store)
                            else:
                                n = n + 1
                        while cell_search(r+1, c, new_word[n], len(new_letters), len(new_letters[0]), new_letters) == True:
                            r = r + 1
                            c = c
                            if n == len(new_word) - 1:
                               # print 'final location is at ' + str(new_word) + str(location)
                                final_loc_store.append(r_init)
                                final_loc_store.append(c_init)
                                word = ''.join(new_word)
                                if word in final_locations:
                                    final_locations[word].append(final_loc_store)
                                else:
                                    final_locations[word] = []
                                    final_locations[word].append(final_loc_store)
                            else: 
                                n = n + 1
                        while cell_search(r+1, c+1, new_word[n], len(new_letters), len(new_letters[0]), new_letters) == True:
                            r = r + 1
                            c = c + 1
                            if n == len(new_word) - 1:
                                #print 'final location is at ' + str(new_word) + ' ' + str(location)
                                final_loc_store.append(r_init)
                                final_loc_store.append(c_init)
                                word = ''.join(new_word)
                                if word in final_locations:
                                    final_locations[word].append(final_loc_store)
                                else:
                                    final_locations[word] = []
                                    final_locations[word].append(final_loc_store)
                            else: 
                                n = n + 1

    return final_locations

def output(final_locations): #expected input is dictionary created by find_words
    for item in final_locations.items(): 
        name = item [0]
        vals = item[1]
        vals.sort()
        print name
        print str(vals[0][0] + 1) + ' ' + str(vals[0][1] + 1)
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
    first_locations = find_firsts(parsed_data)
    final_locations = find_words(parsed_data, first_locations)
    output(final_locations)
    j = j + 1
    print
    print


