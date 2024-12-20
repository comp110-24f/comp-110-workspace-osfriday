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


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end."""
    if start > end:
        raise ValueError("invalid arguments")
    if start == end:
        return None
    else:
        # 1. Handle the first value in your new list here!
        first: int = start
        # 2. Let the rest of the list be handled recursively!
        rest: Node | None = recursive_range(start + 1, end)
        # 3. Return a new node which is followed by rest
        return Node(first, rest)


a_list: Node | None = recursive_range(110, 113)
print(a_list)
