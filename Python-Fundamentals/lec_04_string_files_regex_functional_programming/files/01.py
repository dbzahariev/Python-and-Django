with open('input.txt', 'r') as file:
    lines = file.readlines()
    odd_lines = []
    for index in range(1, len(lines), 2):
        odd_lines.append(lines[index])
    with open('output.txt', 'w') as file_write:
        file_write.writelines(odd_lines)
