import re

text = input()
pattern = re.compile(r'(?:0x)?[0-9A-F]+\b')
matches = re.finditer(pattern, text)

print(*[match.group() for match in matches])
