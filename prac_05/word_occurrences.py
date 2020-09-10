"""
CP1404/CP5632 Practical
Print word that are the same and their recurrence
"""

word_to_count = {}
string_for_count = input("Text: ")
words = string_for_count.split()

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

# Print word that are the same and their recurrence in alphabetical order
words = list(word_to_count.keys())
words.sort()

# use the max function to find the longest word
longest_word = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, longest_word, word_to_count[word]))
