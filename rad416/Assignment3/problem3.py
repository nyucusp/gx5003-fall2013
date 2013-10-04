"""
An implementation of a generic tree to encode Erdos numbers based on input
"""




class TreeNode(object):
  def __init__(self, data, children=[]):
    self.data = data
    self.children = list(children)
  
  def add(self, child):
    self.children.append(child)

inputFile = open('input3.txt','r')
