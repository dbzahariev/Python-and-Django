count_numbers = int(input())
sum_all = 0
max_number = 0
for i in range(0, count_numbers):
    new_number = int(input())
    if i == 0:
        max_number = new_number
    sum_all += new_number
    if max_number < new_number:
        max_number = new_number
if sum_all - max_number == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {abs(max_number + max_number - sum_all)}')
