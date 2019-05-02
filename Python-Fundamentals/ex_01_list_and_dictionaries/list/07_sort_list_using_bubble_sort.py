my_list = list(map(int, input().split(' ')))

swapped = True
while swapped:
    swapped = False
    for i in range(1, len(my_list)):
        if my_list[i - 1] > my_list[i]:
            temp = my_list[i - 1]
            my_list[i - 1] = my_list[i]
            my_list[i] = temp
            swapped = True
print(' '.join(map(str, my_list)))
