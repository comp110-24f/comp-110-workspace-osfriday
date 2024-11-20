"""Working on Linked Lists and Recursive Structures!"""

from __future__ import annotations


class Node:
    """Node class."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):  # one magic method
        """Initializing Node class."""
        self.value = val
        self.next = next

    def __str__(self) -> str:  # another magic method
        """Represent a Node object as a str."""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Return data of a Node stored at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index == 0:  # Base Case
            return head.value
        else:
            index -= 1  # want to work to index 0
            return value_at(head.next, index)  # Recursive Case


def max(head: Node | None) -> int:
    """Returns max data value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:  # Base Case
        return head.value
    max_val: int = max(head.next)  # assign max val to next value and compare
    if head.value < max_val:
        return max_val
    else:
        return head.value  # Recursive Case


def linkify(items: list[int]) -> Node | None:
    """Return a Linked List of nodes with the same values as the input."""
    if len(items) == 0:  # Base Case
        return None
    return Node(items[0], linkify(items[1:]))  # Recursive Case
    # recall linkify with every val but the first one; new list


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list with value multiplied by some factor."""
    if head is None:  # Base Case
        return None
    return Node(head.value * factor, scale(head.next, factor))  # Recursive Case
    # Want to multiply each value by the factor
