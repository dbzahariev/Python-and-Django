in_type = input()
a = input()
b = input()


def sum_chars_from_strings(x):
    result = 0
    for later in x:
        result += ord(later)
    return result


def return_first_later(x):
    res = 0
    for later in x:
        res = ord(later)
        break

    return res


def broken_variant():
    if in_type == 'char':
        print(chr(max(ord(a), ord(b))))
    elif in_type == 'int':
        print(max(int(a), int(b)))
    else:
        if a.__len__() > b.__len__():
            print(a)
        elif a.__len__() < b.__len__():
            print(b)
        elif return_first_later(a) > return_first_later(b):
            print(a)
        elif return_first_later(a) < return_first_later(b):
            print(b)
        else:
            if sum_chars_from_strings(b) >= sum_chars_from_strings(a):
                print(b)
            else:
                print(a)


def correct_variant():
    if in_type == 'int':
        print(max(int(a), int(b)))
    else:
        print(max(a, b))


correct_variant()
