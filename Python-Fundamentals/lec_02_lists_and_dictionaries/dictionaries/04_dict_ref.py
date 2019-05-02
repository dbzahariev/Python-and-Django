my_dict = {}
while True:
    entrance = input()
    if entrance == 'end':
        for key, value in my_dict.items():
            print(f'{key} === {value}')
        break

    key = entrance.split(' = ')[0]
    value = entrance.split(' = ')[1]
    if value in my_dict:
        my_dict[key] = my_dict[value]
    elif value.isnumeric():
        my_dict[key] = int(value)
