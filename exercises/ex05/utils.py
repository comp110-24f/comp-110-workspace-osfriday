"""Practice with List Units for EX05!"""

__author__ = "730566893"


def only_evens(input: list[int]) -> list[int]:
    """Given a list returns a list with only the even elements."""
    a: list[int] = []
    for elem in input:
        if elem % 2 == 0:
            a.append(elem)
    return a


def sub(input: list[int], s_idx: int, e_idx: int) -> list[int]:
    """Creating a subset of input over a range of indexes."""
    sub: list[int] = []
    if len(input) == 0:
        return sub
    if s_idx < 0:  # want idx to start with 0 with neg entries
        s_idx = 0
    if e_idx > len(input):  # e_idx cannot be greater than length of input
        e_idx = len(input)
    while e_idx - s_idx - 1 >= 0:  # want loop to end after s_idx = e_idx - 1
        sub.append(input[s_idx])
        s_idx += 1
    return sub


def add_at_index(input: list[int], elem: int, idx: int) -> None:
    """Modifying input to place element at a given index."""
    input.append(0)  # add empty integer at the end of list
    if idx < 0 or idx > (len(input) - 1):  # raise AFTER appending input
        raise IndexError("Index is out of bounds for the input list")
    index: int = len(input) - 2  # want to shift every element AFTER idx given
    while index >= idx:  # start from the right side of list to prevent errors
        input[index + 1] = input[index]  # reassign elements after idx to left element
        index -= 1
    input[idx] = elem
