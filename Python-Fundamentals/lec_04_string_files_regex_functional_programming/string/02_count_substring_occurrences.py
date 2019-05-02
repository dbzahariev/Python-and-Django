data_text, data_subtext, count, index = [input().lower(), input().lower(), 0, 0]

while not index >= len(data_text):
    finder_index = data_text.find(data_subtext, index)
    if finder_index > -1:
        index = finder_index + 1
        count += 1
    else:
        break
print(count)
