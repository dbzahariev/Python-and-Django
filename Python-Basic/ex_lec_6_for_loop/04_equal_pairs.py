numbers_count = int(input())

prev_sum = 0
max_diff = 0
for i in range(numbers_count):
    num_1 = int(input())
    num_2 = int(input())
    this_sum = num_1 + num_2
    if i == 0:
        prev_sum = this_sum
    else:
        max_diff = max(max_diff, abs(prev_sum - this_sum))  # current_diff
        prev_sum = this_sum

if max_diff == 0:
    print(f"Yes, value={prev_sum}")
else:
    print(f"No, maxdiff={max_diff}")
