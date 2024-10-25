"""Practice with Lists, Dictionaries, and for Loops in VSC."""

# Q1
my_list: list[int] = list()

my_list.append(8)
my_list.append(0)
my_list.append(3)
my_list.append(-1)

my_list.pop(2)  # pop refers to INDEX not VALUE

# Q2
my_dict: dict[int, str] = {}

my_dict[8] = "eight"
my_dict[0] = "zero"
my_dict[3] = "three"
my_dict[-1] = "negative one"

my_dict.pop(3)

cat = my_dict[0]

print(len(my_dict))  # for both number of keys and values

my_dict[8] = "zero"

# answer: dict[str, int] = {"returned_amount": sum_dict_keys(my_dict)}

# Q3
# a,a,a,a,a,a

# Q4
for x in range(0, len(my_dict)):
    print(x)

# 4a. Since there is not a key "2", it returns a key error
# 4b. a
# 4c. a
# 4d. a
# 4e. a
# 4f. a

# Q5
my_dict: dict[str, str] = {
    "cat": "dog",
    "dog": "cat",
    "bird": "mouse",
    "mouse": "bird",
    "while": "whale",
}

# 5a. a
# 5f. c
