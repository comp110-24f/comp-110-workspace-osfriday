"""Comparing method types in OOP for CQ09."""

from __future__ import annotations

__author__ = "730566893"


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Update x and y by multiplying by some factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Return a new point by multiplying x and y by some factor."""
        x_init: float = self.x * factor
        y_init: float = self.y * factor
        return Point(x_init, y_init)
