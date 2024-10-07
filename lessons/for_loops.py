"""Lesson on for loops and range() !!!"""

# Looping through Sequences
#   you can use a loop to iterate over every element in a sequence

# for...in... loops
#   print every element of xs
xs: list[str] = ["w", "x", "y", "z"]
idx: int = 0
while idx < len(xs):  # iterates over indices
    print(xs[idx])
    idx += 1

# with a for...in... loop
# for ____ in _____
#   blank 1: name (variable that rep elements in a list) and blank 2: sequence
#   will look at every element in list and will stop when all elements are looped

for elem in xs:  # iterates over elements in xs
    print(elem)

# Practice

pets: list[str] = ["Louise", "Bo", "Bear"]

for ani in pets:
    print(f"Good boy, {ani}!")  # using f-strings!!!


# When to use a while loop over a for loop?
#   When there is a condition that doesn't involve sequences
#   Better when modifying a list (adding or removing elements to a sequence)
#   Access to the indexes
#

# Range
#   A type of sequence you can loop over
# Includes start point, does NOT include end point, and steps through every point btw
# Constructor:
#   range(start, end, [step = 1])
# start and end refer to the INDEXES

# use with for loops and range
for index in range(0, len(pets)):
    print(pets[index])

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):  # excludes len(names) so the idx will work
    print(f"{idx}: {names[idx]}")
