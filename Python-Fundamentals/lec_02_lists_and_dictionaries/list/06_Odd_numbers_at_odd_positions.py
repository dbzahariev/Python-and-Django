list_numbers = list(map(int, input().split(' ')))

for index in range(len(list_numbers)):
    if index % 2 == 1:
        if list_numbers[index] % 2 == 1:
            print(f'Index {index} -> {list_numbers[index]}')
