"""
CP1404/CP5632 Practical
Guitar class
"""
CURRENT_YEAR = 2020
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of Guitar object."""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of guitar object based on year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if Guitar is vintage."""
        age = Guitar.get_age(self)
        return age >= VINTAGE_AGE
