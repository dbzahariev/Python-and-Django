def filtered_word():
    this_text = input().replace(',', ' ').replace(';', ' ').replace(':', ' ').replace('.', ' ') \
        .replace('!', ' ').replace('(', ' ').replace(')', ' ') \
        .replace('"', ' ').replace("'", ' ').replace("\\", ' ') \
        .replace("\/", ' ').replace("\[", ' ').replace("\[", ' ')
    new_words = []
    for this_word in this_text.split():
        if this_word == '':
            continue
        if this_word not in new_words:
            new_words.append(this_word)
    return new_words


def check_word(this_word):
    count_low = 0
    count_up = 0
    count_mix = 0
    for letter in this_word:
        if 97 <= ord(letter) <= 122:
            count_low += 1
        elif 65 <= ord(letter) <= 90:
            count_up += 1
        else:
            count_mix += 1

    if len(this_word) == count_low:
        return 'Lower'
    elif len(this_word) == count_up:
        return 'Upper'
    else:
        return 'Mixed'


words = filtered_word()

lo_case = []
mixed_case = []
up_case = []

for word in words:
    if check_word(word) == 'Lower':
        lo_case.append(word)
    elif check_word(word) == 'Upper':
        up_case.append(word)
    elif check_word(word) == 'Mixed':
        mixed_case.append(word)

print(f"Lower-case: {', '.join(lo_case)}")
print(f"Mixed-case: {', '.join(mixed_case)}")
print(f"Upper-case: {', '.join(up_case)}")
