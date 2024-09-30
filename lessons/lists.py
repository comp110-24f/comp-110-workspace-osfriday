"""Practice with Lists"""

# Lists can only have one type of data (all strs, all floats but not a str and float.)
# Declaring a List
names: list[str]

#   <list name>: list[<object type>]
#   You can also have an EMPTY LIST

# Initializing an Empty List
#   "constructor" list() is a function that returns the literal []
#   Like an empty str --> str() returns ""
#   NOTE: The constructor list() is a function that returns the literal []
#       Literal (what literally returns) vs. constructor (a way to denote what will be
#       returned)

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

print(my_numbers)
my_numbers.append(1.5)  # way to add things to a list
print(my_numbers)

# Initializing An Already Populated List
game_points: list[int] = [102, 86, 94]

# Subscription Notation/Indexing
print(game_points[2])  # should print 94

last_game: int = game_points[2]  # can save value of a list as a variable

# Modify object in list through Indexing
grocery_list: list[str] = ["bananas", "milk", "bread", "bananas"]
grocery_list[1] = "eggs"  # will replace "milk" with "eggs"

#   You cannot do this with variables!!!!
# x: str = "110" then x[0] = "2" DOES NOT WORK

# Getting the length of List
len(game_points)  # returns 3 bc there are 3 items in the list

# Remove items from a list
grocery_list.pop(2)  # 2 equates to the INDEX, not number in list,
#                       therefore it removes "bread", NOT "milk"


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(game_points)
