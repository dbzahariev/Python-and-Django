def insertion_sort(this_list):
    for index in range(1, len(this_list)):

        current_value = this_list[index]
        position = index

        while position > 0 and this_list[position - 1] > current_value:
            this_list[position] = this_list[position - 1]
            position = position - 1

        this_list[position] = current_value


my_list = list(map(int, input().split(' ')))
insertion_sort(my_list)
print(' '.join(map(str, my_list)))
