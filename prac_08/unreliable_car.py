from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.reliability = reliability

    def drive(self, distance):  # fix code
        distance_driven = super().drive(distance)
        reliability = float(random.randint(0, 100))
        if self.reliability < reliability:
            print(reliability)
            distance_driven = 0
        else:
            self.current_fare_distance += distance_driven
        return distance_driven
