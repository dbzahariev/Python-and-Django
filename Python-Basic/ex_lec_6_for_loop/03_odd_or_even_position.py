import math
count_numbers = int(input())
odd_sum = 0.0
odd_min = math.inf
odd_max = -math.inf
even_sum = 0.0
even_min = math.inf
even_max = -math.inf
for i in range(1, count_numbers + 1):
    new_number = float(input())
    if i % 2 == 1:
        odd_sum += new_number
        odd_max = max(odd_max, new_number)
        odd_min = min(odd_min, new_number)
    else:
        even_sum += new_number
        even_max = max(even_max, new_number)
        even_min = min(even_min, new_number)
if odd_sum.is_integer():
    print(f'OddSum={odd_sum:.0f},')
else:
    print(f'OddSum={odd_sum},')
if odd_min == math.inf:
    print('OddMin=No')
elif odd_min.is_integer():
    print(f'OddMin={odd_min:.0f},')
else:
    print(f'OddMin={odd_min},')
if odd_max == -math.inf:
    print('OddMax=No')
elif odd_max.is_integer():
    print(f'OddMax={odd_max:.0f},')
else:
    print(f'OddMax={odd_max},')

if even_sum.is_integer():
    print(f'EvenSum={even_sum:.0f},')
else:
    print(f'EvenSum={even_sum},')
if even_min == math.inf:
    print('EvenMin=No')
elif even_min.is_integer():
    print(f'EvenMin={even_min:.0f},')
else:
    print(f'EvenMin={even_min},')
if even_max == -math.inf:
    print('EvenMax=No')
elif even_max.is_integer():
    print(f'EvenMax={even_max:.0f},')
else:
    print(f'EvenMax={even_max},')
