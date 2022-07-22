# demo using built in modules:

# Test if a Python Key Word exists in a list of strings
# Perform by importing function iskeyword from keyword module

from keyword import iskeyword

no_keyword_list = ['hi', 'whats up?', 'goodbye']
all_keyword_list = ['def', 'True', 'False', 'if', 'else']
one_keyword_list = ['yo', 'eren', 'def', 'bye']

print(f"\nThe following lists are:\n")
print(no_keyword_list)
print(all_keyword_list)
print(one_keyword_list)


def contains_keyword(word_list):
    return any(iskeyword(word) for word in word_list)


print(f"Does {no_keyword_list} contain any keywords?: {contains_keyword(no_keyword_list)}\n")
print(f"Does {all_keyword_list} contain any keywords?: {contains_keyword(all_keyword_list)}\n")
print(f"Does {one_keyword_list} contain any keywords?: {contains_keyword(one_keyword_list)}\n")
