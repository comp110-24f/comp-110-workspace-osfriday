"""Practice with Global Variables and Scopes."""


def remove_chars(msg: str, char: str) -> str:
    """Return message with all instances of char removed."""
    copy: str = ""  # Set yp empty string and then we can copy vals over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:  # want to copy letters that are not equal to char
            copy += msg[index]
        index += 1

    return copy


word: str = "yoyo"  # Global Variable
if __name__ == "__main__":
    print(remove_chars(word, "o"))
    print(remove_chars(word, "y"))
