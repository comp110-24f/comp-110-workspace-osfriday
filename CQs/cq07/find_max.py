"""Working with Unit Tests for CQ07"""

__author__ = "730566893"


def find_and_remove_max(input: list[int]) -> int:
    """Find the largest number and remove all entries of it in a list."""
    i_1: int = 1  # max is already idx 0 so start at idx 1.
    i_2: int = 0  # separate idx for other while loop
    if input == []:  # want it to return -1 if empty
        return -1
    max: int = input[0]
    while i_1 < len(input):
        if max < input[i_1]:
            max = input[i_1]
        i_1 += 1
    while i_2 < len(input):
        if input[i_2] == max:
            input.pop(i_2)
        else:  # remove entries of the max
            i_2 += 1
    return max
