"""Challenge Question on While loops!"""

__author__ = "730566893"


def num_instances(phrase: str, search_char: str) -> int:
    """Counting number of instances a character appears in a phrase"""
    index: int = 0  # Indexing from the start of phrase should be 0
    count: int = 0  # Count should start from 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1  # add one to count to show number of instances and rep as needed
        index += 1  # regardless if the character is found, add one to index to check
        #               entire phrase
    return count  # must return an integer
