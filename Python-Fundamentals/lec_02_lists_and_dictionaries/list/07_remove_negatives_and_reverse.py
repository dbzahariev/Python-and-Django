list_numbers = list(map(int, input().split(' ')))

list_numbers_rotate = []
for index in range(len(list_numbers) - 1, -1, -1):
    if list_numbers[index] > 0:
        list_numbers_rotate.append(list_numbers[index])

if len(list_numbers_rotate) == 0:
    print('empty')
else:
    print(' '.join(list(map(str, list_numbers_rotate))))
