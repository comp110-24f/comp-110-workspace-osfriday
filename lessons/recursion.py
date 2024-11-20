from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next


two: Node = Node(2, None)
one: Node = Node(1, two)


def sum(head: Node | None) -> int:
    if head is None:
        return 0
    else:
        rest: int = sum(head.next)
        return head.value + rest


def to_str(head: Node | None) -> str:
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))


def factorial(n: int) -> int:
    # Base Case: n is 0 or 1
    if n == 0 or n == 1:
        return 1
    # Recursive Case: n * recursive call with n-1 as argument
    else:
        return n * factorial(n - 1)
