numbers = input()


def printing():
    sum_odd = 0
    sum_even = 0
    for later in numbers:
        if later != '-':
            number = int(later)
            if number % 2 == 1:
                sum_odd += number
            else:
                sum_even += number
    print(sum_odd * sum_even)


printing()
