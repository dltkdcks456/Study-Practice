T = int(input())
for test in range(T):
    x, y = map(int, input().split())
    diff = y - x
    i = 1
    while i * (i + 1) <= diff:  # i * (i + 1) <= diff < (i + 1) * (i + 2)
        i += 1
    i = i - 1
    if i * (i + 1) == diff:
        print(2 * i)
    elif diff - i * (i + 1) <= i + 1:
        print(2 * i + 1)
    else:
        print(2 * i + 2)