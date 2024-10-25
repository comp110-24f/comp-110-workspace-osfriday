"""Function Writing Practice for QX03!"""


def odd_and_even(input: list[int]) -> list[int]:
    """return a list of elements of input that are odd with an even index."""
    x: list[int] = []
    idx: int = 0
    while idx < len(input):
        if (idx % 2 == 0) and (input[idx] % 2 == 1):
            x.append(input[idx])
        idx += 1
    return x


def short_words(list1: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    list2: list[str] = []
    i: int = 0
    while i < len(list1):
        if len(list1[i]) < 5:
            list2 += f"{list1[i]}"
        else:
            print(f"{list1[i]} is too long!")
        i += 1
    return list2


weather: list[str] = ["sun", "cloud", "sky"]

short_words(weather)
