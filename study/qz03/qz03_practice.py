""""Practice with class's for CQ10!"""

import math

__author__ = "730566893"


class Circle:
    radius: float

    def __init__(self, r: float):
        self.radius = r

    def area(self) -> float:
        area: float = math.pi * (self.radius**2)
        return area


class Rectangle:
    width: float
    height: float

    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h

    def area(self):
        area: float = self.width * self.height
        return area
