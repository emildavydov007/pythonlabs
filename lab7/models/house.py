from .building import Building


class House(Building):

    def calc_heat(self):
        return self.calc_area() * 150

    def __repr__(self):
        return "House object"