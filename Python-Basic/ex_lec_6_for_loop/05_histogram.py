p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0
count_all = int(input())
for number in range(count_all):
    new_number = int(input())
    if new_number < 200:
        p_1 += 1
    elif 200 <= new_number <= 399:
        p_2 += 1
    elif 400 <= new_number <= 599:
        p_3 += 1
    elif 600 <= new_number <= 799:
        p_4 += 1
    elif new_number >= 800:
        p_5 += 1
p_1 = p_1 / count_all * 100
p_2 = p_2 / count_all * 100
p_3 = p_3 / count_all * 100
p_4 = p_4 / count_all * 100
p_5 = p_5 / count_all * 100
print(f"{p_1:.2f}%\n{p_2:.2f}%\n{p_3:.2f}%\n{p_4:.2f}%\n{p_5:.2f}%")
