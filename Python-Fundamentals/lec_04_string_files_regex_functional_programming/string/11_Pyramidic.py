count_row_input = int(input())

my_dict = {}
for i in range(count_row_input):
    data = input()
    for letter in data:
        if letter in my_dict:
            my_dict[letter] = data.count(letter)
        else:
            my_dict[letter] = 1

max_char = None
max_char_count = -1
for key, value in my_dict.items():
    if value > max_char_count:
        max_char = key
        max_char_count = value

for i in range(1, max_char_count + 1, 2):
    print(max_char * i)
