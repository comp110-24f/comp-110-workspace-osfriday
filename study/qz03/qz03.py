"""Study for QZ03"""


class Course:
    """Models the idea of a UNC course."""

    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        """Check if prereq is included in course name."""
        for level in self.level:
            if self.level >= 400 and prereq in self.prerequisites:
                return True
            else:
                return False


class Car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = 0
        self.color = ""
        self.mileage = 0.0

    def update_mileage(self, miles: float):
        self.mileage += miles

    def display_info(self):
        print(f"Make: {self.make}")  # repeat for others


def calculation_depreciation(car: Car, depreciation_rate: float) -> float:
    return car.mileage * depreciation_rate


# Instantiation Practice
