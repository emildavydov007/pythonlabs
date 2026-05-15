from abc import ABC, abstractmethod


class Building(ABC):

    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def calc_area(self):
        return self._length * self._width

    @abstractmethod
    def calc_heat(self):
        pass

    def __str__(self):
        return f"Площадь: {self.calc_area()}"

    def __len__(self):
        return int(self.calc_area())