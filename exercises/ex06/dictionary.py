"""Practicing with dicts for EX06."""

__author__ = "730566893"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert keys and values in a dict."""
    invert: dict[str, str] = {}
    for key in a:
        if a[key] in invert:  # means a duplicate key exists (raise error)
            raise KeyError("Keys must be unique!")
        invert[a[key]] = key  # inverse the key and value from a
    return invert


def favorite_color(a: dict[str, str]) -> str:
    """Return most said color in a dict."""
    fav: str = ""
    color_count: dict[str, int] = {}  # color and count
    max: int = 0  # keep track of max count
    for name in a:  # will count favorite colors and put in a dict
        if a[name] in color_count:
            color_count[a[name]] += 1
        else:
            color_count[a[name]] = 1
    for color in color_count:
        if color_count[color] > max:  # compares colors singularly
            fav = color  # will only reassign if greater than, not equal to max
            max = color_count[color]
    return fav


def count(a: list[str]) -> dict[str, int]:
    """Creating dict with values and the appearances of said values."""
    val_count: dict[str, int] = {}
    for elem_1 in a:
        if elem_1 in val_count:
            val_count[elem_1] += 1  # add one to add to appearances
        else:
            val_count[elem_1] = 1  # add a row to the dict
    return val_count


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Creating an index for words starting with the same letter."""
    begin_letter: dict[str, list[str]] = {}
    for words in x:
        first_letter: str = words[0].lower()  # make the first letter lowercase
        if first_letter in begin_letter:
            begin_letter[words[0]].append(words)  # add word to list value
        else:
            begin_letter[words[0]] = [words]
    return begin_letter


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Attendance of students stored in a dict."""
    if day in attendance:
        if not (
            student in attendance[day]
        ):  # if student is not already counted in attendance
            attendance[day].append(student)
    else:
        attendance[day] = [student]  # if day is not already in attendance
    return None
