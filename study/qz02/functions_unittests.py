"""Functions to practice Unit Tests."""


def find_even(nums: list[int]) -> int:
    idx: int = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            return idx
        idx += 1
    return -1


def sum_numbers(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise Exception("Empty list - no elements to add")

    total: int = numbers[0]
    for i in range(1, len(numbers)):
        total += numbers[i]

    return total


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def add_key_to_dicts(dicts: list[dict], key: str, value: int) -> None:
    for d in dicts:
        d[key] = value


def increment_dict_value(d: dict[str, int], key: str) -> None:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


def max_sum_dict(d: dict[str, list[int]]) -> str:
    keys = []
    for key in d:
        keys.append(key)

    values_list_1 = d[keys[0]]
    values_list_2 = d[keys[1]]

    total_1 = 0
    for value in values_list_1:
        total_1 += value

    total_2 = 0
    for value in values_list_2:
        total_2 += value

    if total_1 > total_2:
        return keys[0]
    else:
        return keys[1]
