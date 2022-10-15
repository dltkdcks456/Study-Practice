import sys

for test in range(3):
    N = int(input())
    s = 0
    for _ in range(N):
        s += int(sys.stdin.readline())
    if s > 0:
        print('+')
    elif s == 0:
        print(0)
    else:
        print('-')