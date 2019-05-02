my_dict = {}
while True:
    internal = input()
    if internal.lower() == 'end':
        for key, value in my_dict.items():
            if len(value) > 0:
                print(f"{key} === {', '.join(value)}")
        break
    pair = internal.split(' -> ')
    key = pair[0]
    if key not in my_dict:
        my_dict[key] = []

    values = pair[1].split(', ')
    if len(values) == 0:
        continue
    for value in values:
        if value.isdigit():
            my_dict[key].append(value)
        if value in my_dict:
            my_dict[key].extend(my_dict[value])
