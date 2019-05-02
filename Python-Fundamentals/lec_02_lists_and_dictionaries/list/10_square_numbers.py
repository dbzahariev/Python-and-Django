def my_sqrt(num):
    n = (num / 2) + 1
    n1 = (n + num / n) / 2
    while n1 < n:
        n = n1
        n1 = (n + (num / n)) / 2
    return n


list_numbers = list(map(str, input().split(' ')))
list_numbers = filter(None, list_numbers)
list_numbers = list(map(int, list_numbers))
list_numbers.sort(reverse=True)
list_sqrt = []
for i in range(len(list_numbers)):
    if my_sqrt(list_numbers[i]).is_integer():
        list_sqrt.append(str(list_numbers[i]))
print(' '.join(list_sqrt))
