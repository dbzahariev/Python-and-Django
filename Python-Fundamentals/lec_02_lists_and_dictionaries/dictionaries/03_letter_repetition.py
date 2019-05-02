list_string = []
for letter in input():
    list_string.append(letter)

dict_strings = {}
for i in list_string:
    dict_strings[i] = list_string.count(i)

for key, value in dict_strings.items():
    print(f'{key} -> {value}')
