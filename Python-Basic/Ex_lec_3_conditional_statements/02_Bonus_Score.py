number = float(input())
bonus_score = 0.0

if number <= 100:
    bonus_score = 5
else:
    if number > 1000:
        bonus_score = number * 0.10
    else:
        bonus_score = number * 0.20

if number % 2 == 0:
    bonus_score += 1
elif number % 10 == 5:
    bonus_score += 2
print(bonus_score)
print(number + bonus_score)
