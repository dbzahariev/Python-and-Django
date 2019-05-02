key = int(input())

count_solution = 0
for a in range(1, min(31, int(key / 2))):
    for b in range(1, min(31, int(key / 2))):
        for c in range(1, min(31, int(key / 2))):
            if a < b < c and a + b + c == key:
                print(f'{a} + {b} + {c} = {key}')
                count_solution += 1
            if a > b > c and a * b * c == key:
                print(f'{a} * {b} * {c} = {key}')
                count_solution += 1
if count_solution == 0:
    print('No!')
