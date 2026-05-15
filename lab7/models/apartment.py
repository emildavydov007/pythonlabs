
from .building import Building

class Apartment(Building):

    def calc_heat(self):
        return self.calc_area() * 120

    def __repr__(self):
        return "Apartment object"