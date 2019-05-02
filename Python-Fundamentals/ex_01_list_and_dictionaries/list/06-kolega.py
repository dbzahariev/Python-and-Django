a = list(map(int, input().split()))

for item in range(0, (len(a) // 2)):
    a[item], a[(-item - 1)] = a[(-item - 1)], a[item]

print(*a)
