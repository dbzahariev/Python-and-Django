list_numbers = list(map(int, input().split(' ')))

count_odd = 0
for num in list_numbers:
    if num % 2 == 1:
        count_odd += 1
print(count_odd)
