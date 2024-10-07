"""Working with Lists for EX04!"""

__author__ = "730566893"


def all(a: list[int], n: int) -> bool:
    """check that each entry in list contains the same value n."""
    i: int = 0
    same: bool = True
    if len(a) == 0:
        same = False
    while i < len(a):
        if a[i] != n:
            same = False  # same is F once one item is not the same
        i += 1  # to prevent infinite loop and check each index
    return same


def max(num: list[int]) -> int:
    """Finds max value in list."""
    if len(num) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 1
    max: int = num[0]
    while idx < len(num):
        if max < num[idx]:
            max = num[idx]  # max is reassigned to the greater value
        idx += 1  # to prevent infinite loop and check each index
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks that two lists contain deep equality."""
    idx: int = 0
    ans: bool = True
    if len(list_1) != len(list_2):
        ans = False
    while (idx < len(list_1)) and (idx < len(list_2)):
        if list_1[idx] != list_2[idx]:
            # only wants ans to change if there is a non-equal idx
            ans = False
        idx += 1  # to prevent infinite loop and check each index
    return ans


def extend(x: list[int], y: list[int]) -> None:
    """Adds entry from one list to the end of the other."""
    idx: int = 0
    while idx < len(y):
        x.append(y[idx])  # Do not have to worry about overlap
        idx += 1  # to prevent infinite loop and check each index in y
