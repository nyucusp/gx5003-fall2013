class Zipcode:
    number = None
    population = 0
    incidents = 0
    
    def __init__(self, number, population):
        self.number = number
        self.population = population

    def addIncident(self):
        self.incidents += 1

    def passAttributes(self):
        return self.population, self.incidents
