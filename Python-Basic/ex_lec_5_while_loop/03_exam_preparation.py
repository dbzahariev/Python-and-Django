count_problems = int(input())
sum_score = 0.0
average_score = 0.0
count_all_task = 0
count_fails = 0
last_problem = ""
while True:
    name_task = input()
    if name_task == "Enough":
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {count_all_task}")
        print(f"Last problem: {last_problem}")
        break
    last_problem = name_task
    grade = float(input())
    count_all_task += 1
    sum_score += grade
    average_score = sum_score / count_all_task
    if grade <= 4:
        count_fails += 1
    if count_fails == count_problems:
        print(f"You need a break, {count_fails} poor grades.")
        break

