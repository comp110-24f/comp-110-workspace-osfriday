"""Practice with function writing"""


# Lists
def odd_and_even(input: list[int]) -> list[int]:
    """Return a new lsit containing odd elements that have even indices."""
    odd_at_even: list[int] = []
    for i in range(0, len(input)):
        if i % 2 == 0:
            if input[i] % 2 == 1:
                odd_at_even.append(input[i])
    return odd_at_even


def short_words(a: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    short: list[str] = []
    for word in a:
        if len(word) < 5:
            short.append(word)
        else:
            print(f"{word} is too long!")
    return short


def multiples(a: list[int]) -> list[bool]:
    """Is each int value a multiple of the previous value."""
    mult: list[bool] = []
    if a[0] % a[len(a) - 1] == 0:
        mult.append(True)
    else:
        mult.append(False)
    for i in range(0, len(a) - 1):
        if a[i + 1] % a[i] == 0:
            mult.append(True)
        else:
            mult.append(False)
    return mult


def reverse_multiply(a: list[int]) -> list[int]:
    """return a list with values doubled and reversed from a."""
    reverse_double: list[int] = []
    i: int = len(a) - 1
    while i >= 0:
        reverse_double.append(a[i] * 2)
        i -= 1
    return reverse_double


# Dictionaries
def value_exists(input: dict[str, int], val: int) -> bool:
    exists: bool = False
    for key in input:
        if input[key] == val:
            exists = True
            return exists
    return exists


def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    """Checks if each balue in inp is even or odd."""
    for key in inp:
        if inp[key] % 2 == 0:
            inp[key] += n
        else:
            inp[key] -= n


def free_biscuits(x: dict[str, list[int]]) -> dict[str, bool]:
    """Maps each game to whether or not to win free buscuits."""
    biscuit: dict[str, bool] = {}
    total_points: int = 0
    for key in x:
        points: list[int] = x[key]
        total_points = 0
        for num in points:
            total_points += num
        if total_points >= 100:
            biscuit[key] = True
        else:
            biscuit[key] = False
    return biscuit


def merge_lists(a: list[str], b: list[int]) -> dict[str, int]:
    """Merge two lists together."""
    merge: dict[str, int] = {}
    if len(a) != len(b):
        return merge
    i: int = 0
    while i < len(a):
        merge[a[i]] = b[i]
        i += 1
    return merge


# Q6
# Q7
# Q8
# Q9
# Q10
# Q11
# Q12
# Q13
# Q14
# Q15
# Q16
# Q17
# Q18
# Q19
# Q20
# Q21
# Q22
# Q23
# Q24
# Q25
# Q26
# Q27
