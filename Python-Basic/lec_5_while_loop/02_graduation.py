name = input()

grade = float(input())
counter = 1
result = 0
year = 1
while year < 12:
    result += grade
    counter += 1
    if grade > 4:
        year += 1
    grade = float(input())

print(f"{name} graduated. Average grade: {(result / counter):.2f}")


# prieto reshenie:
name = input()
grades = 1.0
sum_all_grades = 0.0
while grades <= 12:
    grade = float(input())
    if grade >= 4.00:
        sum_all_grades += grade
        grades += 1

average = sum_all_grades / 12
print(f"{name} graduated. Average grade: {average:.2f}")
