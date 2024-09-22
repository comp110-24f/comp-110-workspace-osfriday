"""Practice creating a Wordle-like game!"""

__author__ = "730566893"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """Returning 5-letter input word"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:  # if len(input) is not 5, error bc that is req.
        print("Error: Word must contain 5 characters.")
        exit()  # exit should occur iff error message and after it, not b/f
    return word


def input_letter() -> str:
    """Input of a single character and returning it."""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:  # if the input is not 1, it is not a char t/f error
        print("Error: Character must be a single character.")
        exit()  # exit should occur iff error message and after it, not b/f
    return letter


def contains_char(word: str, letter: str) -> None:
    """Finding where a letter may exist in a word."""
    print("Searching for " + letter + " in " + word)
    index: int = 0
    count: int = 0  # count variable should be an integer
    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count += 1  # only add to the count if the condition is true t/f indent
        index += 1  # add one to the idx regardless of condition value t/f not indented
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


# We want to show where a letter exists in a word, so we must index where the word is.
# If word [index] is equivalent to a letter, print where the letter can be found but if
# not, just add 1 to index number.
