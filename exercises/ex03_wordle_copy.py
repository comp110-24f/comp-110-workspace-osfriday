"""Re-Creating Wordle game!"""

__author__ = "730566893"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    N: int = 1  # Number of turns player has used (start with 1)
    ans: bool = False  # want loop to end once you find the secret or N > 6
    while N <= 6 and (not ans):
        print(f"=== Turn {N}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        # guess reassigned to emo. to check if answer == secret
        if guess == secret:
            # so that we can check for any length of secret
            print(f"You won in {N}/6 turns!")
            ans = True
        N += 1
    if N > 6 and (not ans):  # if you never get the answer, print...
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Count the number of chars in word to match secret word length."""
    guess_word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess_word) != secret_word_len:
        guess_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # Don't forget spaces bf and after length
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
            emoji += f"{GREEN_BOX}"  # use f" notation to call variables inside a str.
        elif contains_char(secret_word=secret, char_guess=(guess[index])):
            emoji += f"{YELLOW_BOX}"
        else:
            emoji += f"{WHITE_BOX}"
        index += 1
    return emoji


if __name__ == "__main__":
    main(secret="codes")
