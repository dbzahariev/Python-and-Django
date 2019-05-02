list_string = input().split(' ')

dict_strings = {}

for i in range(len(list_string)):
    list_string[i] = list_string[i].lower()

for i in range(len(list_string)):
    dict_strings[list_string[i]] = list_string.count(list_string[i])

result = []
for key, value in dict_strings.items():
    if value % 2 == 1:
        result.append(key)

print(', '.join(result))
