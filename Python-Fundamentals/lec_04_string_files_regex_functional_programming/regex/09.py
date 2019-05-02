import re


def calc_tail(tail):
    tail_type = 'None'
    tail_length = tail.count('>')
    if tail_length > 5:
        tail_type = "Long"
    elif tail_length > 1:
        tail_type = "Medium"
    elif tail_length == 1:
        tail_type = "Short"
    tail_cm = tail_length * 2
    if tail_cm == 0:
        return f'  Tail type: {tail_type}'
    else:
        return f'  Tail type: {tail_type} ({tail_cm} cm)'


def calc_body(body):
    body_type = 'Short'
    body_length = body.count('(')
    if body_length > 10:
        body_type = 'Long'
    if body_length > 5:
        body_type = 'Medium'
    body_cm = body_length * 2
    return f"  Body type: {body_type} ({body_cm} cm)"


def calc_status(statuses):
    status = ""
    if statuses == "'":
        status = 'Awake'
    elif statuses == "-":
        status = 'Asleep'
    elif statuses == "x" or statuses == 'X':
        status = 'Dead'
    return f"  Status: {status}"


text = input()
# noinspection Annotator,Annotator
pattern = re.compile(r"(?P<tail>[>]+|[<]+)(?:[<]*)(?P<body>[(]+)(?P<statuses>['|\-xX])[>]+")
matches = re.finditer(pattern, text)
count = 0
for match in matches:
    count += 1
    print(f"Fish {count}: {match.group()}")
    tail = match.group('tail')
    body = match.group('body')
    statuses = match.group('statuses')
    print(calc_tail(tail))
    print(calc_body(body))
    print(calc_status(statuses))

if count == 0:
    print("No fish found.")
