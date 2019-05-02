import re

text = input()
pattern = re.compile(r"(?P<power>[2-9]|10|J|Q|K|A)(?P<suit>[SHDC])")
matches = re.finditer(pattern, text)

for match in matches:
    print(f"{match.group('power')}{match.group('suit')}", end=' ')
