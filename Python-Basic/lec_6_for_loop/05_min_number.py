input_count = int(input())
min_number = 0
for i in range(0, input_count):
    new_number = int(input())
    if i == 0:
        min_number = new_number
    if new_number < min_number:
        min_number = new_number
print(min_number)
