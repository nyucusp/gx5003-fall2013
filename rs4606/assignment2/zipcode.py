"""
Here we define a class called Zipcode which has two attributes, a number (the zip code
itself) and the population of the zip code.
"""

class Zipcode:
    number = None
    population = None
    
    def __init__(self, number, population):
        self.number = number
        self.population = population