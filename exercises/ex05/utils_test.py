"""Practice with List Units Tests for EX05!"""

__author__ = "730566893"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_edge_case() -> None:
    """Assert only_evens function returns empty list for edge case."""
    a: list[int] = []
    assert only_evens(a) == []  # bool should be true; want an empty list


def test_only_evens_use_case1() -> None:
    """Assert only_evens function returns a list."""
    a: list[int] = [1, 2, 3, 4, 5]
    assert type(only_evens(a)) == list  # want the return type to be a list


def test_only_evens_use_case2() -> None:
    """Assert only_evens function returns an only even list given."""
    a: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(a) == [2, 4]  # only want even entries from a


def test_sub_edge_case() -> None:
    """assert sub function returns sub-list with out-of-bounds indices."""
    a: list[int] = [1, 2, 3]
    assert sub(a, -2, 5) == [1, 2, 3]  # does this count as a separate edge case?
    # is it too similar to example usage?


def test_sub_use_case1() -> None:
    """Assert that sub function does not mutate input function."""
    a: list[int] = [1, 2, 3]
    sub(a, 0, 1)
    assert a == [1, 2, 3]  # want a to be unchanged


def test_sub_use_case2() -> None:
    """ "Assert sub function returns subset list within proper range."""
    b: list[int] = [34, 56, 78, 1, 2, 3, 4]
    assert sub(b, 3, 6) == [1, 2, 3]  # want adjusted index range to be 3 to 6


def test_add_at_index_edge_case() -> None:
    """Check that add_at_index function returns errors for out-of-bounds index."""
    a: list[int] = [4, 5, 6]
    with pytest.raises(IndexError):
        add_at_index(a, 7, 4)  # want to get an index error message


def test_add_at_index_use_case1() -> None:
    """Check that add_at_index function returns proper list or error."""
    a: list[int] = [4, 5, 6]
    assert add_at_index(a, 2, 1) is None  # syntax "is None" was given with my error


def test_add_at_index_use_case2() -> None:
    """Check that add_at_index function mutates list properly."""
    a: list[int] = [5]
    add_at_index(a, 4, 0)
    assert a == [4, 5]  # even though its a 1 elem list, add 4 bf 5
