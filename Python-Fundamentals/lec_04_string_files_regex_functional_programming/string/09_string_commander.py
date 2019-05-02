string_list = list(input())


def shift_right(lst):
    try:
        return [lst[-1]] + lst[:-1]
    except IndexError:
        return lst


def shift_left(lst):
    temp = lst[0]
    for index in range(len(lst) - 1):
        lst[index] = lst[index + 1]
        lst[index + 1] = temp
    return lst


while True:
    whole_command = input().split()
    command = whole_command[0]
    if command == 'end':
        print(''.join(string_list))
        break
    if command == 'Delete':
        for index in range(int(whole_command[2]), int(whole_command[1]) - 1, -1):
            del string_list[index]
    if command == 'Insert':
        start_index = int(whole_command[1])
        for c_index in range(0, len(whole_command[2])):
            string_list.insert(start_index, whole_command[2][c_index])
            start_index += 1
    if command == 'Right':
        for i in range(int(whole_command[1])):
            string_list = shift_right(string_list)
    if command == 'Left':
        for i in range(int(whole_command[1])):
            string_list = shift_left(string_list)
