"""Practicing with dicts for EX06."""

__author__ = "730566893"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert keys and values in a dict."""
    invert: dict[str, str] = {}
    for key in a:
        invert[a[key]] = key  # inverse the key and value from a
    for key_1 in invert:
        for key_2 in invert:
            if key_1 == key_2:
                raise KeyError("Keys must be unique!")
    return invert


def favorite_colors(a: dict[str, str]) -> str:
    """Return most said color in a dict."""
    fav: str = ""
    count: dict[str, int] = {}
    color_count: int = 0
    for names_1 in a:  # will count favorite colors and put in a dict
        color_count: int = 0
        for names_2 in a:
            if a[names_1] == a[names_2]:
                color_count += 1
        count[a[names_1]] = color_count

    for colors_1 in count:  # will compare colors to find one with highest number
        for colors_2 in count:
            if count[colors_1] < count[colors_2]:
                fav = colors_2
            else:
                fav = colors_1
    return fav


def count(a: list[str]) -> dict[str, int]:
    """Creating dict with values and the appearances of said values."""
    val_count: dict[str, int] = {}
    count: int = 0
    for elem_1 in a:
        count = 0
        for elem_2 in a:
            if elem_1 == elem_2:
                count += 1
        val_count[elem_1] = count
    for val_1 in val_count:
        for val_2 in val_count:
            if val_1 == val_2:
                val_count.pop(val_2)  # cannot have this syntax
                # how can I remove duplicate entries in dicts?

    return val_count
