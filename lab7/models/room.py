from models.building import Building

class Room(Building):

    def calc_heat(self):
        return self.calc_area() * 100

    def __repr__(self):
        return "Room object"