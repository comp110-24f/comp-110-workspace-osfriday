"""File to define Fish class."""

__author__ = "730566893"


class Fish:
    """Defining Attributes in Fish Class."""

    age: int

    def __init__(self):
        """Initializing Fish class."""
        self.age = 0
        return None

    def one_day(self):
        """Modifying attributes for one day as a fish."""
        self.age += 1
        return None
