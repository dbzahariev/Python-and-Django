max_1 = int(input())
max_2 = int(input())
max_3 = int(input())

for i_1 in range(1, max_1 + 1):
    for i_2 in range(1, max_2 + 1):
        for i_3 in range(1, max_3 + 1):
            if i_1 % 2 == 0:
                if i_3 % 2 == 0:
                    if 2 <= i_2 <= 7:
                        if i_2 == 2 or i_2 == 3 or i_2 == 5 or i_2 == 7:
                            print(i_1, i_2, i_3)
