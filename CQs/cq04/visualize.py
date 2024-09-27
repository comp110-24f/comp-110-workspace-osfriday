"""Visualize the 2 functions for CQ04"""

__author__ = "730566893"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords  # imports must be at beginning of file

x: str = "123"
y: str = "abc"

print(concat(x, y))

get_coords(x, y)
