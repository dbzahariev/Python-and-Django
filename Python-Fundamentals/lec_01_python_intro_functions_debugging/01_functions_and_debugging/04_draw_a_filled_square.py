n = int(input())


def print_head_footer():
    new_line = ''
    for i in range(0, n * 2):
        new_line += '-'
    print(f'{new_line}')


def print_body():
    for i in range(0, n - 2):
        print(create_line(n))


def create_line(number):
    new_line = '-'
    for i in range(0, number - 1):
        new_line += '\/'
    new_line += '-'
    return new_line


print_head_footer()
print_body()
print_head_footer()
