K = int(input())
L = int(input())
M = int(input())
N = int(input())

count_change = 0
for i_1 in range(K, 8 + 1):
    if count_change >= 6:
        break
    for i_2 in range(9, L - 1, -1):
        if count_change >= 6:
            break
        for i_3 in range(M, 8 + 1 + 1):
            if count_change >= 6:
                break
            for i_4 in range(9, N - 1, -1):
                if count_change >= 6:
                    break
                if i_1 % 2 == 0 and i_3 % 2 == 0 and i_2 % 2 == 1 and i_4 % 2 == 1:
                    if i_1 == i_3 and i_2 == i_4:
                        print(f'Cannot change the same player.')
                    else:
                        print(f'{i_1}{i_2} - {i_3}{i_4}')
                        count_change += 1
                    if count_change >= 6:
                        break
