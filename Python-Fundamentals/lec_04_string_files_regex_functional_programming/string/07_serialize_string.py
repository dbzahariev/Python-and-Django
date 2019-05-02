data = input()

char_dict = {}
for index in range(len(data)):
    letter = data[index]
    if letter not in char_dict:
        char_dict[letter] = [index]
    else:
        char_dict[letter].append(index)

for letter, indices in char_dict.items():
    print(f"{letter}:{'/'.join(map(str, indices))}")
