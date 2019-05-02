data = input().split(' ')
result = []
for word in data:
    reversed_word = f"{''.join(list(reversed(word)))}"
    if word == reversed_word and word not in result:
        result.append(word)
result = sorted(result, key=str.lower)
print(', '.join(result))
