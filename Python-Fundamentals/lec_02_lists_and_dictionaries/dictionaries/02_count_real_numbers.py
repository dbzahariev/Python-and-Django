list_float = list(map(float, input().split(' ')))

dict_float = {}
for i in list_float:
    dict_float[i] = list_float.count(i)

for key, value in sorted(dict_float.items(), reverse=False):
    print(f'{key} -> {value} times')
