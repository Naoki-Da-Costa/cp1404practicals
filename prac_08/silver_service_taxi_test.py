from prac_08.silver_service_taxi import SilverServiceTaxi
test_car = SilverServiceTaxi("Ferrari", 100, 2)
test_car.drive(18)
print(test_car)
print("${:.2f}".format(test_car.get_fare()))
