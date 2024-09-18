"""Practice creating a Wordle-like game!"""

__author__ = "730566893"


def input_word() -> str:
    """Returning 5-letter input word"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        print(word)
    else:
        print("Error: Word must contain 5 characters.")
        print(word)  # Do I need this line of code (10/13/21/24) or is it redundant?
    return word


def input_letter() -> str:
    """Input of a single character and returning it."""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        print(letter)
    else:
        print("Error: Character must be a single character.")
        print(letter)  # should it be print(str(letter)) or just print(letter) ???
    return letter


def contains_char(word: str, letter: str) -> None:
    """Finding where a letter may exist in a word."""
    print("Searching for " + letter + " in " + word)
    index: int = 0
    while index < len(word):
        if word[index] == letter:  # do I need an else statement???
            print(letter + " found at index " + str(index))
        index += 1


# We want to show where a letter exists in a word, so we must index where the word is.
# If word [index] is equivalent to a letter, print where the letter can be found but if
# not, just add 1 to index number.
