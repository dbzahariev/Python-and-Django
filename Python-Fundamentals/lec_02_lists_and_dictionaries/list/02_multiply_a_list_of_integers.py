list_numbers = list(map(int, input().split(' ')))
multiply = int(input())


def multiplier(a):
    return f'{a * multiply}'


list_numbers = list(map(multiplier, list_numbers))
print(" ".join(list_numbers))
