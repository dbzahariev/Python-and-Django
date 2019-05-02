import re

regex = r"name is (?P<name>[A-Z][a-z]+ [A-Z][a-z]+).* (?P<age>\d\d) years.*on (?P<date>\d\d-\d\d-\d\d\d\d).*\."

date_base = []
while True:
    date = input()
    if date == 'make migrations':
        break
    test_str = date
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for match in matches:
        person = {'name': match.group('name'), 'age': match.group('age'), 'birthday': match.group('date')}
        if int(person['age']) > 9 and int(person['age']) < 100:
            date_base.append(person)
    # print(date)

if len(date_base) == 0:
    print('DB is empty')
else:
    for person in date_base:
        print(f"Name of the person: {person['name']}.")
        print(f"Age of the person: {person['age']}.")
        print(f"Birthdate of the person: {person['birthday']}.")
