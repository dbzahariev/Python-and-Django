key, value, count = [input(), input(), int(input())]

pairs_list_tuple = []
for i in range(count):
    pair = input().split(' => ')
    pairs_list_tuple.append((pair[0], pair[1].split(';')))

for this_key, this_value in pairs_list_tuple:
    if key in this_key:
        print(f'{this_key}:')
        for val in this_value:
            if value in val:
                print(f'-{val}')
