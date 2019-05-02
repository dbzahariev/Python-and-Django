searched_word, text = [input().split(), input()]

for word in searched_word:
    text = text.replace(word, '*' * len(word))

print(text)
