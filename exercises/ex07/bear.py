"""File to define Bear class."""

__author__ = "730566893"


class Bear:
    """Defining Attributes in Bear Class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """One day as a bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase hunger_score to match number of fish the bear eats."""
        self.hunger_score += num_fish
        return None
