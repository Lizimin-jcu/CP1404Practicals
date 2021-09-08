from random import randint
from prac_08.car import Car

class Unreliablecar(Car):
    def __init__(self,name,fuel,reliability):
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self, distance):
        random= randint(0,100)
        if random > self.reliability:
            distance=0
        distance_drived=super().drive(distance)
        return distance_drived


