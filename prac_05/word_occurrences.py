"""
Word Occurrences
Estimate: 15 minutes
Actual: 16 Minutes, 50 seconds
"""

text = input("Text: ")

words_to_count = {}
words = text.split()
for word in words:
    occurrences = words_to_count.get(word, 0)
    words_to_count[word] = occurrences + 1

words = list(words_to_count.keys())
words.sort()

longest_word = max((len(word) for word in words))
for word in words:
    print(f"{word:{longest_word}} : {words_to_count[word]}")
