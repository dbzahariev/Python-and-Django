text = input()
vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
sum_vowels = 0
for i in range(0, text.__len__()):
    if vowels.__contains__(text[i]):
        sum_vowels += vowels[text[i]]
print(sum_vowels)
