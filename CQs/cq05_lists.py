"""Mutating functions."""

__author__ = "730566893"


def manual_append(x: list[int], n: int) -> None:
    """Mutate a by adding n to the end of its list."""
    x.append(n)  # add int to end of the list


def double(y: list[int]) -> None:
    """Double all the entries in a list."""
    index: int = 0
    while index < len(y):
        y[index] *= 2  # that entry is changed by being doubled
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
# since list_2 = list_1, they are the same reference and will print the same list

double(list_2)  # will effect list_1 since they refer to the same list

print(list_1)
print(list_2)
