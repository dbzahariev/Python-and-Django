p_1 = 0
p_2 = 0
p_3 = 0
count_all = int(input())
for number in range(count_all):
    new_number = int(input())
    if new_number % 2 == 0:
        p_1 += 1
    if new_number % 3 == 0:
        p_2 += 1
    if new_number % 4 == 0:
        p_3 += 1
p_1 = p_1 / count_all * 100
p_2 = p_2 / count_all * 100
p_3 = p_3 / count_all * 100
print(f"{p_1:.2f}%\n{p_2:.2f}%\n{p_3:.2f}%")
