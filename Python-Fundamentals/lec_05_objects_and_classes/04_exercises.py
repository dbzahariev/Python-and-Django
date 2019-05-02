class Exercisers:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems


data = input()
exercisers_list = []
while not data == 'go go go':
    data = data.split(' -> ')
    new_exercise = Exercisers(data[0], data[1], data[2], data[3].split(', '))
    exercisers_list.append(new_exercise)
    data = input()

for count_exegesis in range(len(exercisers_list)):
    topic = exercisers_list[count_exegesis].topic
    course_name = exercisers_list[count_exegesis].course_name
    judge_contest_link = exercisers_list[count_exegesis].judge_contest_link
    problems = exercisers_list[count_exegesis].problems
    print(f'Exercises: {topic}')
    print(f'Problems for exercises and homework for the "{course_name}" course @ SoftUni.')
    print(f'Check your solutions here: {judge_contest_link}')
    for count_problem in range(len(problems)):
        print(f'{count_problem + 1}. {problems[count_problem]}')
