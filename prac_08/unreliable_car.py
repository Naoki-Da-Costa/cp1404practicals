from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.reliability = reliability

    def drive(self, distance):
        reliability = float(random.randint(0, 3))
        if self.reliability < reliability:
            print("don't drive", reliability)
            distance = 0
        self.current_fare_distance += distance
        distance_driven = super().drive(distance)
        return distance_driven

        # reliability = float(random.randint(0, 3))
        # if reliability < self.reliability:
        #     print("drive", reliability)
        #     self.current_fare_distance += distance
        # else:
        #     print("don't drive", reliability)
        #     distance = 0
        # distance_driven = super().drive(distance)
        # return distance_driven
