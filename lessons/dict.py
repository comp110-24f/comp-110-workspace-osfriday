"""Practice with dictionaries in Python."""

# Dictionaries
#   Cannot have duplicate keys but can have duplicate values

"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["vanilla"] += 110

print(ice_cream["vanilla"])
# vanilla = 118
