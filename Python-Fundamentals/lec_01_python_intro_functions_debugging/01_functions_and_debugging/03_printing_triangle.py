n = int(input())


def create_line(range_line):
    line = ''
    for i in range(1, range_line + 1):
        line += f'{i} '
    return line


def first_part_print():
    for a in range(1, n + 1):
        line = create_line(a)
        print(line)


def second_part_print():
    for a in range(n - 1, 0, -1):
        line = create_line(a)
        print(line)


first_part_print()
second_part_print()
