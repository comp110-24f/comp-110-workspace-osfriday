"""Review for QZ02!"""

x: list[int] = [9, -1, 8, 5]
y: list[str] = ["cat", "dog", "turtle", "elephant", "fish"]
z: list[str] = ["z"]

a: dict[int, int] = {1: 2, 2: 3}
b: dict[str, int] = {"a": 1, "b": 2}

nest: dict[str, int] = {f"{a}": 1, f"{b}": 2}

print(nest)
idx: int = 0

while idx < len(x):
    print(idx)
    print(x[idx])
    idx += 1

for elem in y:
    print(elem)

for idx in range(0, len(z)):
    print(idx)
    print(z[idx])

# for..range() is like using while loops with idx but skips the
# step of assigning a variable; for...in loops are different and only does elements

# not able to print indices with for...in loops because only deals with elems

# Dictionary Question Review
# Q10
my_dictionary: dict[str, float] = {}

# Q11
msg: dict[str, int] = {"Hello": 1, "Yall": 2}
msg["Yall"]

# Q12
msg["Yall"] += 3

# Q13
ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}
ids.pop(100)

# Q14
len(ids)

# Q15
inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}
inventory["makers"] = 15

# Q16
prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}
prices["milk"] = 2.50

# Q17
scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
for keys in scores:
    print(keys)


# Q19
fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}
for fruit in fruit_count:
    print(f"{fruit}: {fruit_count[fruit]}")

# Q20
first_dict: dict[str, int] = {"a": 1, "b": 2}
second_dict: dict[str, int] = {"c": 3, "d": 4}
combo_dict: dict[str, int] = {}

for keys in first_dict:
    combo_dict[keys] = first_dict[keys]
for keys in second_dict:
    combo_dict[keys] = second_dict[keys]


# For loops Review

# Q1
stats: list[int] = [7, 8, 9]
total: int = 100

for elem in stats:
    total -= elem
for i in range(0, len(stats)):
    total -= stats[i]

for elem in stats:  # doesn't work
    stats.pop(elem)

# generally, you cannot iterate through a list while also mutating
# or removing elements from list; distrupts iteration process
