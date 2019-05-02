import re


def find_size(this_str):
    for match in re.finditer(regex, this_str, re.MULTILINE):
        return '\d+ ' * int(match.group('size'))


foo = ""
while True:
    date_1 = input()
    if date_1 == 'DEBUG':
        break
    foo += date_1.split('0')

# foo = foo.replace('0 0', '')


date = foo
regex = r"(?P<start>32656 19759 32763) 0 (?P<size>\d+) 0 " + f""
regex += f"(?P<characters>{find_size(date)})0"
for match in re.finditer(regex, date, re.MULTILINE):
    print(''.join(list(map(chr, map(int, match.group('characters').strip().split())))))
    break
