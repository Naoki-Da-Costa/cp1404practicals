from prac_08.unreliable_car import UnreliableCar
new_car = UnreliableCar("Mitsubishi 2", 100, 50)
new_car.drive(20)
print(new_car)
print(new_car.current_fare_distance)
new_car.drive(20)
print(new_car)
print(new_car.current_fare_distance)
