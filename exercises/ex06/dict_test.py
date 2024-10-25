"""Checking dictionary functions."""

from exercises.ex06.dictionary import favorite_color


def test_favorite_color_edge_case() -> None:
    """Check that dictionary mutates count dict properly."""
    a: dict[str, str] = {
        "Marc": "yellow",
        "Ezri": "blue",
        "Kris": "blue",
        "Olivia": "yellow",
    }
    favorite_color(a)
    assert count == {"yellow": 2, "blue": 2}
