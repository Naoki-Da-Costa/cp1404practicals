"""
CP1404/CP5632 Practical
Guitar program.
"""
from prac_06.guitar import Guitar


def main():
    """Guitar program."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    if guitars:
        print("\n... snip ...\n")
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {}: {} ({}), worth ${:.2f}{}".format(i, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))
    else:
        print("No guitars")


main()
