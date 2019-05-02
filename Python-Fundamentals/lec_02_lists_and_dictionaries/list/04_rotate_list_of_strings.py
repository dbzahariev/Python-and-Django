list_string = list(input().split(' '))

list_string_rotate = []
for i in range(0, len(list_string)):
    list_string_rotate.append(list_string[i - 1])

print(' '.join(list(list_string_rotate)))
