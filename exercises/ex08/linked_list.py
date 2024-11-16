"""Working on Linked Lists and Recursive Structures!"""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):  # one magic method
        self.value = val
        self.next = next

    def __str__(self) -> str:  # another magic method
        """Represent a Node object as a str"""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a Linked List."""
    if head.next is None:
        return head.value  # Base case!
    else:
        rest: int = last(head.next)
        return rest  # Recursive case!


def value_at(head: Node | None, index: int) -> int:
    """Return data of a Node stored at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index == 0:
            return head.value
        else:
            index -= 1
            return value_at(head.next, index)


def max(head: Node | None) -> int:
    """Returns max data value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    # max: int = 0
    # i: int = 0
    # if max is less than the value_at(subsequent Node) then reassign max
    # how can I sequence through linked lists w/o loops?
