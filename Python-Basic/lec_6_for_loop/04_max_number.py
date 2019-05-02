max_number = 0
for i in range(0, int(input())):
    new_number = int(input())
    if i == 0:
        max_number = new_number
    if max_number < new_number:
        max_number = new_number
print(max_number)
