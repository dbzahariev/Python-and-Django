text, sum_type, sum_int_letter = [input(), input().upper(), 0]

for letter in text:
    letter_to_int = ord(letter)
    if (sum_type == 'LOWERCASE' and ord('a') <= letter_to_int <= ord('z')) or (
            sum_type == 'UPPERCASE' and ord('A') <= letter_to_int <= ord('Z')):
        sum_int_letter += letter_to_int
print(f'The total sum is: {sum_int_letter}')
