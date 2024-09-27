"""Practice importing"""

from lessons.scope_practice import remove_chars, word

print(word)
print(remove_chars("happy", "p"))

# lessons is a directory
# importing runs the WHOLE MODULE (scope_practice)
#   if you don't want that to happen, in the module, add the if __name__ == "__main__"
#   before whatever you don't want to transfer
