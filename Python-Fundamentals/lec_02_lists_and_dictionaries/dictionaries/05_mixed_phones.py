my_dict = {}
while True:
    entrance = input()
    if entrance == 'Over':
        for key, value in sorted(my_dict.items()):
            print(f'{key} -> {value}')
        break
    entrance = entrance.split()
    entrance.remove(':')
    key = ''
    value = ''
    if entrance[0].isnumeric():
        key = entrance[1]
        value = entrance[0]
    else:
        key = entrance[0]
        value = entrance[1]
    my_dict[key] = value
