""" CQ00 Functions COMP 110!"""

__author__ = "730566893"


def mimic(message: str) -> str:
    """repeat input string back to you."""
    return message


def main() -> None:
    """print what returns with mimic function."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
