"""Practice with recursive writing for QZ04!"""

from __future__ import annotations


def factorial(input: int) -> int:
    if input == 0:
        return 1
    return input * factorial(input - 1)


def sum_of_natural_numbers(n: int) -> int:
    if n == 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)


def power(n: int, pwr: int) -> int:
    if pwr == 0:
        return 1
    return n * power(n, pwr - 1)


class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value  # A list of integers
        # Either another Node or None
        if next is None:
            self.next = None
        else:
            self.next = next


def sum_node_values(head: Node | None) -> int:
    if head is None:
        return 0
    current_sum: int = 0
    for val in head.value:
        current_sum += val
    return current_sum + sum_node_values(head.next)


def increment_node_values(head: Node | None) -> None:
    if head is None:
        return None
    copy: list[int] = []
    for val in head.value:
        copy.append(val + 1)
    return increment_node_values(head.next)


def print_nodes(head: Node | None) -> list[int]:
    if head is None:
        return []
    if head.next is None:
        return head.value
    else:
        return print_nodes(head.next)
