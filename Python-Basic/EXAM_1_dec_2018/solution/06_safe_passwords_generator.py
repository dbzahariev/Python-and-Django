a = int(input())
b = int(input())
max_combination = int(input())
symbol1 = 35
symbol2 = 64
count = 0
result = ''
for i in range(1, a + 1):
    for j in range(1, b + 1):
        result += f"{chr(symbol1)}{chr(symbol2)}{i}{j}{chr(symbol2)}{chr(symbol1)}|"
        count += 1
        symbol1 += 1
        if symbol1 == 56:
            symbol1 = 35
        symbol2 += 1
        if symbol2 == 97:
            symbol2 = 64
        if count >= max_combination:
            break
    if count >= max_combination:
        break
print(result)
