scenarioList = Problem3Input()

class PaperAuthor:
	erdosNum = None
	connectedAuthors = []
	def __init__(self, connectedAuthors):
		self.connectedAuthors = connectedAuthors

def process_scenario(scenario):
	'''
	taken the input scenario,
	1. creates a dictionary of conneted authors
	2. calculate their erdos numbers, running breadth-first
	3. Specific Author's E#'s are just asking the tree for them now.
	'''
	authorDict = create_author_dict(scenario)
	compute_erdos_numbers(authorDict)
	return get_results(authorDict)

def create_author_dict(scenario):
	return {}

def compute_erdos_numbers(authorDict):
	pass

def get_results(authorDict):
	return None

for scenario in scenarioList:
	print process_scenario(scenario)