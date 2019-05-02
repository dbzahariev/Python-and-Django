def is_uniq(this_list):
    for el in this_list:
        if this_list.count(el) != 1:
            return False
    return True


def add_even_2(this_list):
    for i in range(len(this_list)):
        if this_list[i] % 2 == 0:
            this_list[i] = this_list[i] + 2
    this_list.sort()
    return this_list


def add_odd_3(this_list):
    for i in range(len(this_list)):
        if this_list[i] % 2 == 1:
            this_list[i] = this_list[i] + 3
    this_list.sort()
    return this_list


while True:
    date = input()
    if date == 'stop playing':
        break
    date = date.split()
    date = list(map(int, date))
    if is_uniq(date):
        date = add_even_2(date)
        print(f'Unique list: {",".join(map(str, date))}')
        print(f'Output: {(sum(date) / len(date)):.2f}')
    else:
        date = add_odd_3(date)
        print(f'Non-unique list: {":".join(map(str, date))}')
        print(f'Output: {(sum(date) / len(date)):.2f}')
