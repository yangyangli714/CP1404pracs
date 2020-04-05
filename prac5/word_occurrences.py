"""
CP1404 Practical
Count word occurrences in a string
"""

word_occurred = {}
text = input("Text: ")
words = text.split()

for word in words:
    frequency = word_occurred.get(word, 0)
    word_occurred[word] = frequency + 1

words = list(word_occurred.keys())
words.sort()


max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_occurred[word]))

