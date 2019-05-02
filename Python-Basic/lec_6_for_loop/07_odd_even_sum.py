import math

sum_odd = 0
sum_even = 0

for i in range(0, int(input())):
    if i % 2 == 0:
        sum_odd += int(input())
    else:
        sum_even += int(input())

if sum_odd == sum_even:
    print(f"Yes")
    print(f"Sum = {sum_odd}")
else:
    print(f"No")
    print(f"Diff = {int(math.fabs(sum_odd - sum_even))}")
