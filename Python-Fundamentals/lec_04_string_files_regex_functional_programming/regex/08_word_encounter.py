import re

data = input()
pattern = re.compile(rf"{'(?:[A-z]*)' + (f'(?:' + data[0] + '{1})(?:[A-z]*)') * int(data[1])}")

all_word = []
while True:
    text = input()
    if text == 'end':
        break
    if ord(text[0]) not in range(ord('A'), ord('Z')):  # check input if start with uppercase letter
        continue
    if ord(text[-1]) not in [ord('!'), ord('.'), ord('?')]:  # check input if end with one of '.' or '!' or '?'
        continue

    matches = re.finditer(pattern, text)
    for match in matches:
        new_word = match.group()
        if new_word != '':  # check if empty string
            all_word.append(f"{match.group()}")
print(*all_word, sep=', ')
