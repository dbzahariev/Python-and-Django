input_list = sorted(list(map(int, input().split())), reverse=True)
print(' '.join(map(str, [input_list[index] for index in range(int(input()))])))
