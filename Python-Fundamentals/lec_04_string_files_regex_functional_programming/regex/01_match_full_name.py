import re

text = input()
pattern = re.compile(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b')
matches = re.finditer(pattern, text)

print(*[match.group() for match in matches])
