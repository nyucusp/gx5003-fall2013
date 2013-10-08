'''
Christopher B. Jacoby
Urban Informatics
Homework 3, Problem 3
'''

import sys
import numpy as np
from Queue import Queue
from readInputFile import Problem3Input

class PaperAuthor:
	def __init__(self):
		self.erdosNum = None
		self.connectedAuthors = []
	def __str__(self):
		return "(Erdos#:{0}, Connections:{1})".format(self.erdosNum, self.connectedAuthors)
	def addConnections(self, authors):
		for author in authors:
			if author not in self.connectedAuthors:
				self.connectedAuthors.append(author)

def process_scenario(scenario):
	'''
	taken the input scenario,
	1. creates a dictionary of conneted authors
	2. calculate their erdos numbers, running breadth-first
	3. Specific Author's E#'s are just asking the tree for them now.
	'''
	papers = scenario[0]
	authors = scenario[1]

	authorDict = create_author_dict(papers)
	compute_erdos_numbers(authorDict)

	if debug:
		for author in authorDict:
			print author, authorDict[author]

	return get_results(authorDict, authors)

def create_author_dict(papers):
	retDict = {}

	for paper in papers:
		add_paper_authors_to_dict(retDict, paper)

	return retDict

def add_paper_authors_to_dict(authorDict, paper):
	# paper is made of (authors, name). We only care about the authors.
	npAuthors = np.array(paper[0])
	for author in npAuthors:
		# If the author is not in the dict, add it.
		if author not in authorDict:
			authorDict[author] = PaperAuthor()

		# Add the other authors as connections.
		authorDict[author].addConnections(npAuthors[npAuthors!=author])

def compute_erdos_numbers(authorDict):
	'''
	Compute every member of the dict's erdos numbers using a breadth-first search.
	Starting... with Erdos as the top of the tree.
	'''
	erdosName = "Erdos, P."
	authorQueue = Queue()
	authorSet = set()
	authorQueue.put(erdosName)
	authorSet.add(erdosName)
	authorDict[erdosName].erdosNum = 0
	while not authorQueue.empty():
		currentAuthor = authorQueue.get()
		for author in authorDict[currentAuthor].connectedAuthors:
			if authorDict[author].erdosNum is None:
				authorDict[author].erdosNum = (authorDict[currentAuthor].erdosNum + 1)

			if author not in authorSet:
				authorSet.add(author)
				authorQueue.put(author)

def get_results(authorDict, authors):
	results = []
	for author in authors:
		erdosStr = authorDict[author].erdosNum
		if erdosStr is None:
			erdosStr = "infinity"
		results.append("{0} {1}".format(author, erdosStr))
	return results

debug = False
if len(sys.argv) > 1:
	debug = True

scenarioList = Problem3Input()

i = 1
for scenario in scenarioList.data:
	print "Scenario", i
	for result in process_scenario(scenario):
		print result
	i += 1