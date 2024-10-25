"""Practice with Unit Tests for QZ02!"""

from study.qz02.functions_unittests import (
    find_even,
    sum_numbers,
)


def test_find_even_use_case() -> None:
    """Assert find_even function returns proper number."""
    a: list[int] = [1, 2, 3, 4]
    assert find_even(a) == 1


def test_list_sum_use_case() -> None:
    """Assert sum_numbers functions returns proper total."""
    a: list[int] = [1, 2, 3, 4]
    assert sum_numbers(a) == 10
