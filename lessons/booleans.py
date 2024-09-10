def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        if word[0] == "h":
            return "super h!"  # You can nest if-else statements inside then block
        else:
            return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="corn", letter="c"))
