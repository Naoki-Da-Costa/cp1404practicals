from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ")
    total_fare = 0
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            print_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(total_fare))
        elif menu_choice == "d":
            current_taxi.start_fare()
            drive_distance = float(input("Drive how far? "))
            current_taxi.drive(drive_distance)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            total_fare += current_taxi.get_fare()
            print("Bill to date: ${:.2f}".format(total_fare))
        else:
            print("Invalid choice")
        print(MENU)
        menu_choice = input(">>> ")
    print("Total trip cost: ${:.2f}".format(total_fare))
    print("Taxis are now:")
    print_taxis(taxis)


def print_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
