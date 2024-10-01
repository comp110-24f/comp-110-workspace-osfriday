"""Mutating functions."""

__author__ = "730566893"


def manual_append(x: list[int], n: int) -> None:
    """Mutate a by adding n to the end of its list."""
    x.append(n)


def double(y: list[int]) -> None:
    index: int = 0
    while index < len(y):
        y[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
