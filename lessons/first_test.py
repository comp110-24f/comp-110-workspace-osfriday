from lessons.unit_test_first import get_first, remove_and_get_first, remove_first


def test_get_first_use_case() -> None:
    """Testing basic behavior for get_first function."""
    a: list[int] = [4, 5, 6, 7]
    assert get_first(a) == 4  # Want this to be last line of code in def


def test_remove_first_use_case() -> None:
    a: list[int] = [4, 5, 6, 7]
    remove_first(a)  # call function first to mutate a
    assert a == [5, 6, 7]


def test_remove_and_get_first_use_case() -> None:
    """Test returning the first element."""
    assert remove_and_get_first([4, 5, 6, 7]) == 4


def test_remove_and_first_mutation_use_case() -> None:
    a: list[int] = [102, 45, 76]
    remove_and_get_first(a)
    assert a == [45, 76]


def test_get_first_edge_case() -> None:
    assert get_first([]) == -1


# another way to run a unit test
