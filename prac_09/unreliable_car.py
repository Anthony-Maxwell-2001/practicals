from random import randint
from prac_06.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """initialises the class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drives the car only if its reliability is above a random number"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
