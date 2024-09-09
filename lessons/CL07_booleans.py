def check_first_letter(word: str, letter:str) -> str:
    if (word [0] == letter):
        print("match!")
    else:
        print("no match!")

check_first_letter(word="happy", letter="h")
check_first_letter(word="happy", letter="s")
