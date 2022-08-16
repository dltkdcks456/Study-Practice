import sys
for test in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    diff = y - x
    i = int(diff ** 0.5)
    while i * (i + 1) <= diff:
        i += 1
    if i * (i - 1) == diff:
        print(2 * (i - 1))
    elif diff - i * (i - 1) <= i:
        print(2 * (i - 1) + 1)
    else:
        print(2 * (i - 1) + 2)