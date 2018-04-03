

exclusive_words = {}
sentance = input("Text here:")
words = sentance.split()
for word in words:
    frequency = exclusive_words.get(word, 0)
    exclusive_words[word] = frequency + 1

words = list(exclusive_words.keys())
words.sort()
max_length = max((len(word)for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, exclusive_words[word]))
