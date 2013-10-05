from collections import deque

inputFile = open('input4.txt','r')

inputQue = deque()

for lines in inputFile:
  inputQue.append(lines.rstrip())

instances = int(inputQue.popleft())

#start while loop for instances

inputQue.popleft() #kill blank line

rows, columns = inputQue.popleft().split(" ")

grid = [] # grid list
for i in range(0,int(rows)):
    grid.append(list(inputQue.popleft().lower()))

words = int(inputQue.popleft())

wordsList = []

for i in range(0,words):
  wordsList.append(inputQue.popleft())



#end while loop for instances