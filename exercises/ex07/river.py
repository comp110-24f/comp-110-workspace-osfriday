"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730566893"


class River:
    """Defining Attributes in River Class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of fish and bear populations."""
        fit_fish: list[Fish] = []
        fit_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:  # only want fish 3 old or younger
                fit_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:  # only want bears 5 old or younger
                fit_bears.append(bear)

        self.fish = fit_fish  # reassign to copy list with removed items
        self.bears = fit_bears  # reassign to copy list with removed items
        return None

    def bears_eating(self):
        """Accounting for how many fish each Bear can eat."""
        for idx in range(0, len(self.bears)):
            if len(self.fish) >= 5:
                self.bears[idx].eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """If bear hunger score is less than 0, remove from self.bear."""
        full_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:  # only want Bears with hunger.scores >= 0
                full_bears.append(bear)

        self.bears = full_bears  # reassign to copy list with removed items
        return None

    def repopulate_fish(self):
        """Reproduction of fish in self.fish."""
        offspring: int = (len(self.fish) // 2) * 4
        for _ in range(0, offspring):  # add new offspring to the pop
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Reproduction of bears in self.bears."""
        offspring: int = len(self.bears) // 2
        for _ in range(0, offspring):  # add new offspring to the pop
            self.bears.append(Bear())
        return None

    def remove_fish(self, amount: int):
        """Removing a certain amount of fish from its population."""
        not_removed_fish: list[Fish] = []
        for idx in range(0, len(self.fish)):
            if idx >= amount:  # idx already includes 0 so it can equal amount
                not_removed_fish.append(self.fish[idx])
        self.fish = not_removed_fish  # reassign to copy list with removed items
        return None

    def view_river(self):
        """Diagnostic of river behavior."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")  # the length of list is fish pop.
        print(f"Bear population: {len(self.bears)}")  # the length of list is bear pop.
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulating a week in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
