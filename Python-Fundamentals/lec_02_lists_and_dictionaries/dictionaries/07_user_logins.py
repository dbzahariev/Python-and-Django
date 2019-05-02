my_dict = {}
count_fail = 0
is_login = False


def failed(username, count_fail_in):
    print(f'{username}: login failed')
    return count_fail_in + 1


while True:
    entrance = input()
    if entrance == 'login':
        is_login = True
        continue
    if entrance == 'end':
        print(f'unsuccessful login attempts: {count_fail}')
        break
    entrance = entrance.split()
    entrance.remove('->')
    key = entrance[0]
    value = entrance[1]
    if is_login is False:
        my_dict[key] = value
    else:
        if key in my_dict:
            if value == my_dict[key]:
                print(f'{key}: logged in successfully')
            else:
                count_fail = failed(key, count_fail)
        else:
            count_fail = failed(key, count_fail)
