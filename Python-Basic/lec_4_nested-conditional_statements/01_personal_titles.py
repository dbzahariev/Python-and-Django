age = float(input())
gender = input()

mr = ("Master", "Mr.", "Miss", "Ms.")
coefficient = 0
if gender == 'm':
    if age >= 16:
        coefficient += 1
    print(mr[coefficient])
else:
    coefficient = 2
    if age >= 16:
        coefficient += 1
    print(mr[coefficient])
