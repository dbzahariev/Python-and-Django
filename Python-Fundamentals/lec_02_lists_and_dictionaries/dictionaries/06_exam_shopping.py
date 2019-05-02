my_dict = {}
while True:
    entrance = input()
    if entrance == 'shopping time':
        continue
    if entrance == 'exam time':
        for key, value in my_dict.items():
            if value > 0:
                print(f'{key} -> {value}')
        break
    entrance = entrance.split()
    action = entrance[0]
    key = entrance[1]
    value = int(entrance[2])
    if action == 'stock':
        if key in my_dict:
            my_dict[key] = my_dict[key] + value
        else:
            my_dict[key] = value
    elif action == 'buy':
        if key in my_dict and my_dict[key] <= 0:
            print(f'{key} out of stock')
        if key in my_dict:
            my_dict[key] = my_dict[key] - value
        else:
            print(f"{key} doesn't exist")
