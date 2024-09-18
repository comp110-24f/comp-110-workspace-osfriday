"""Practice with while loops in Python"""

# Review
#   Block: sequence of statements (EX: Then vs. Else Blocks)
#       Can be multiple lines of code
# Loops
#   Used to carry out statements in a program repeatedly an arbitrary number of times


def characters(msg: str) -> None:
    index: int = 0
    while index <= len(msg):
        print(msg[index])
        index = index + 1


characters(msg="Howdy")
