"""Working with Unit Tests for CQ07"""

__author__ = "730566893"

from find_max import find_and_remove_max


def test_find_and_remove_max_use_case_1() -> None:
    """Ensures find_and_remove_max returns expected value."""
    a: list[int] = [3, 7, 5, 6, 7, 4]
    assert find_and_remove_max(a) == 7  # 7 is the largest number in this list


def test_find_and_remove_max_use_case_2() -> None:
    """Test if find_and_remove_max mutates input correctly."""
    a: list[int] = [3, 7, 5, 6, 7, 4]
    find_and_remove_max(a)
    assert a == [3, 5, 6, 4]  # want to see if a is mutated w/0 the "7" entries


def test_find_and_remove_max_edge_case() -> None:
    """Test that find_and_remove_max returns correct max with neg. values."""
    a: list[int] = [2, 2, 2, 2]
    assert find_and_remove_max(a) == 2  # 2 is the max; all inputs are the same
