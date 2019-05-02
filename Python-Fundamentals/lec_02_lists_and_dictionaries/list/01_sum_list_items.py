count = int(input())
list_numbers = []

sum_numbers = 0

for i in range(count):
    list_numbers.append(int(input()))
for num in list_numbers:
    sum_numbers += num

print(sum_numbers)
