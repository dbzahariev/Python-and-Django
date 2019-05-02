my_dict = {}
while True:
    data = input()
    if data == 'end':
        break
    for dd in list(map(int, data[2:].split('/'))):
        my_dict[dd] = data[0]

result = ''
for key in sorted(my_dict):
    result += my_dict[key]
print(result)
