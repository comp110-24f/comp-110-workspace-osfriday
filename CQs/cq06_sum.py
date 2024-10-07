"""Summing the elements of a list using different loops!"""

__author__ = "730566893"


def w_sum(vals: list[float]) -> float:
    sum: float = float()  # create an empty float that you use to add indexes
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1  # prevents infinite loop
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = float()  # create an empty float that you use to add indexes
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = float()  # create an empty float that you use to add indexes
    for num in range(0, len(vals)):  # excludes the end point which is perfect for idx
        sum += num
    return sum
