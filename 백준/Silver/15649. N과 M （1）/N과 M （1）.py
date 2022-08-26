import sys

n, m = map(int, sys.stdin.readline().split())
n_list = list(range(1, n + 1))
stack = [-1] * m

def f(n, m):
    if n == m:
        for i in stack:
            print(i, end = ' ')
        print()
        return
    for i in range(len(n_list)):
        if n_list[i] in stack:
            continue
        stack[n] = n_list[i]
        f(n + 1, m)
        stack[n] = -1
f(0, m)