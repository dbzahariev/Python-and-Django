with open('input.txt', 'r') as file:
    lines = file.readlines()

    new_lines = []
    for index in range(len(lines)):
        new_lines.append((lambda x, y: f'{y + 1} {x}')(lines[index], index))
    with open('output.txt', 'w') as file_write:
        file_write.writelines(new_lines)
