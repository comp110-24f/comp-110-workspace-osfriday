"""Concat function for CQ04."""

__author__ = "730566893"


def concat(a: str, b: str) -> str:
    """Return concatenation of 2 inputs."""
    return a + b  # add two strings, a and b


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
