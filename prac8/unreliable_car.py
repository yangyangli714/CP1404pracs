from prac8.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a car"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(0,100) > self.reliability:
            distance = 0
            return distance
        else:
            distance = super().drive(distance)
            return distance