def make_lists(all_words):
    low_w = []
    upper_w = []
    mixed_w = []
    for word in all_words:
        low_case = False
        upper_case = False
        mixed_case = False
        for letter in word:
            if ord(letter) in range(97, 123):
                low_case = True
            elif ord(letter) in range(65, 91):
                upper_case = True
            else:
                mixed_case = True
        if low_case and not upper_case and not mixed_case:
            low_w.append(word)
        elif upper_case and not low_case and not mixed_case:
            upper_w.append(word)
        else:
            mixed_w.append(word)
    return low_w, upper_w, mixed_w


def print_lists(lower, upper, mixed):
    low_str = str.join(', ', lower)
    upper_str = str.join(', ', upper)
    mixed_str = str.join(', ', mixed)

    print(f'Lower-case: {low_str}')
    print(f'Mixed-case: {mixed_str}')
    print(f'Upper-case: {upper_str}')


txt = input()
replacements = ",;:.!()\"\'\\/[] "
clear_chars = []
for i in range(0, len(txt)):
    if txt[i] in replacements:
        clear_chars.append(' ')
    else:
        clear_chars.append(txt[i])
words_str = ''.join(clear_chars)
words = words_str.split()
low_words, upper_words, mixed_words = make_lists(words)
print_lists(low_words, upper_words, mixed_words)
