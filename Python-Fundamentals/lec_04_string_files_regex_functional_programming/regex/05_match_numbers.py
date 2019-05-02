import re

text = input()
pattern = re.compile(r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))')
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), end=' ')
