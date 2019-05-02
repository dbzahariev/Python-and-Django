data = input()
while not data == 'end':
    if data.find('<a') >= 0:
        data = data.replace('<a', '[URL').replace('">', '"]').replace('</a>', '[/URL]')
    print(data)
    data = input()
