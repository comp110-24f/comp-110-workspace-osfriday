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


# print(last(one))
print(last(courses))
