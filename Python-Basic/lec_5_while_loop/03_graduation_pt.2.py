name = input()
grades = 1.0
sum_all_grades = 0.0
excluded_in_class = 0
count_not_grade = 0
while grades <= 12:
    grade = float(input())
    if grade >= 4.00:
        sum_all_grades += grade
        grades += 1
    else:
        count_not_grade += 1
        excluded_in_class = grades
    if count_not_grade == 2:
        break

average = sum_all_grades / 12
if count_not_grade == 2:
    print(f"{name} has been excluded at {excluded_in_class:.0f} grade")
else:
    print(f"{name} graduated. Average grade: {average:.2f}")
