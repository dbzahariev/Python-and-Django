list_numbers = list(filter(None, map(str, input().split('|'))))

list_numbers_rotate = []
for i in range(len(list_numbers) - 1, -1, -1):
    list_numbers_rotate.append(list_numbers[i])
list_numbers = list_numbers_rotate

print(' '.join(list(filter(None, ' '.join(list_numbers).split()))))
