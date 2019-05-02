nums_list = list(map(int, input().split(' ')))

nums_dict = {}
for num in sorted(nums_list):
    if num not in nums_dict:
        nums_dict[num] = nums_list.count(num)

for key, value in nums_dict.items():
    print(f'{key} -> {value}')
