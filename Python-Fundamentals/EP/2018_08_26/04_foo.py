import re


def find_size(regex, this_str):
    regex += ')'
    for match in re.finditer(regex, this_str, re.MULTILINE):
        return '\d+ ' * int(match.group('size'))


foo = ""
while True:
    date_1 = input()
    if date_1 == 'DEBUG':
        break
    foo += date_1
date = foo

# date = '32656 19759 32763 0 5 0 80 101 115 104 111 0 0 0 0 0 0 0 0 0 0 0 0 32656 19759 32763 0 7 0 83 111 102 116 117 110 105 0 0 0 0 0 0 0 0'
while True:
    regex = r"(32656 19759 32763 0 (?P<size>\d+) 0 "
    count_digit = find_size(regex, date)
    if count_digit is None:
        break
    regex += f"(?P<characters>{count_digit})(?P<other>.+))"
    for match in re.finditer(regex, date, re.MULTILINE):
        print(''.join(list(map(chr, map(int, match.group('characters').strip().split())))))
        date = match.group('other')
        break
