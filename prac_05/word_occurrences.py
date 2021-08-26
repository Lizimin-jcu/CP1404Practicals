count_words = {}
text = input("Enter the text: ")
print(count_words)
number_of_words = text.split()
print(number_of_words)
for word in number_of_words:
    collection_of_words = count_words.get(word, 0)
    count_words[word] = collection_of_words + 1
words = list(count_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, count_words[word]))