"""Working with Unit Tests"""


def get_first(input: list[int]) -> int:
    """Return the first element of the input list."""
    if len(input) == 0:
        return int(-1)
    return input[0]


def remove_first(input: list[int]) -> None:
    """Remove the first element of the input list."""
    input.pop(0)


def remove_and_get_first(input: list[int]) -> int:
    first: int = input[0]
    input.pop(0)
    return first


# easier way to test functions instead of the repl is to use the unit test
# Unit test: writes functions to test ofther functions
# Edge case: testing instances outside "typical" usage (empty list, incorrect inputs)
