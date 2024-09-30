"""Re-Creating Wordle game!"""

__author__ = "730566893"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    N: int = 1  # Number of terms player has used (start with 1)
    guess: str = input_guess(len(secret))
    GREEN_BOX: str = "\U0001F7E9"
    while N <= 6 and (
        emojified(guess, secret) != N * f" {GREEN_BOX}"
    ):  # still have turns and didn't answer with the secret
        print(f"=== Turn {N}/6 ===")
        emojified(guess, secret)
        if emojified(guess, secret) == N * f" {GREEN_BOX}":
            print(f"You won in {N}/6 turns!")
        N += 1
    if N > 6:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Count the number of chars in word to match secret word length."""
    guess_word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess_word) != secret_word_len:
        guess_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searching for the num of occurences of char_guess in search_word."""
    assert len(char_guess) == 1
    idx: int = 0
    search: bool = False
    while (idx < len(secret_word)) and (not search):
        # want loop to end once either of these conditionals are false bc either idx is
        # finished or search is True
        if secret_word[idx] == char_guess:
            search = True
        else:
            search = False
        idx += 1
    return search


def emojified(guess: str, secret: str) -> str:
    """Compare 2 srings of equ. length and see which chars match and how."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    index: int = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            emoji += f" {GREEN_BOX}"  # Used to create gaps btw emoji's
        elif contains_char(secret_word=secret, char_guess=(guess[index])):
            emoji += f" {YELLOW_BOX}"  # Used to create gaps btw emoji's
        else:
            emoji += f" {WHITE_BOX}"  # Used to create gaps btw emoji's
        index += 1
    return emoji


main("codes")
