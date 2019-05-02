line_one = input()

while line_one != "collapse":
    line_two = input()

    while len(line_two) > 0:
        if line_one.__contains__(line_two):
            line_one = line_one.replace(line_two, '')
        else:
            line_two = line_two[1:]
            if len(line_two) > 0:
                line_two = line_two[:-1]

    if len(line_one) > 0:
        print(line_one.strip())
    else:
        print("(void)")

    line_one = input()
