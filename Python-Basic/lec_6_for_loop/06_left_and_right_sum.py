import math

input_count = int(input())
diff = 0
left_sum = 0
right_sum = 0

# calc left sum
for i in range(0, input_count):
    left_sum += int(input())

# calc right sum
for i in range(0, input_count):
    right_sum += int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = math.fabs(left_sum - right_sum)
    print(f"No, diff = {diff}")
