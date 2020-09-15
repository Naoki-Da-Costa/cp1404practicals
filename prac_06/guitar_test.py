"""
CP1404/CP5632 Practical
Tests for Guitar class
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922)
another_guitar = Guitar("Another Guitar", 2013)
print("{} get_age() - Expected {}. Got {}".format(gibson.name, 98, gibson.get_age()))
print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 7, another_guitar.get_age()))
print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, True, gibson.is_vintage()))
print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))
