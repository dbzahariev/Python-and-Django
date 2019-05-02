import re

text = input()
pattern = re.compile(r'\b(?P<day>\d{2})([-./])(?P<mount>[A-z][a-z]{2})\2(?P<year>\d{4})\b')
matches = re.finditer(pattern, text)

for match in matches:
    day = match.group('day')
    mount = match.group('mount')
    year = match.group('year')
    print(f'Day: {day}, Mount: {mount}, Year: {year}')
