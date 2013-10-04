"""
An implementation of a generic tree to encode Erdos numbers based on input
"""
from _collections import defaultdict
from collections import deque

class Tree(object):
  def __init__(self, data, children=[]):
    self.data = data
    self.children = list(children)

  def add(self, child):
    self.children.append(child)

inputFile = open('input3.txt','r')

inputQue = deque()

for line in inputFile:
  inputQue.append(line.rstrip())

instances = int(inputQue.popleft()) #instances of Erdos calculations

papers, names = inputQue.popleft().split(" ") #split P,N into variables

authorList = [] #generate list of papers
for i in range(0,int(papers)):
  #intern string of paper citation to variable
  paperString = inputQue.popleft()
  #extract author block
  authorBlock = paperString[0:paperString.find(":")]
  authorList.append(authorBlock)

nameList = [] #generate list of names for evaluation
for i in range(0,int(names)):
  nameList.append(inputQue.popleft())




