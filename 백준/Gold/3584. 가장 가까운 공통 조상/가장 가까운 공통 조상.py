import sys

def find_par(n):
    Li = []
    while n:
        Li.append(n)
        n = par[n]
    return Li


T = int(sys.stdin.readline())
for test in range(T):
    N = int(sys.stdin.readline())
    par = [0] * (N + 1)
    for _ in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())
        par[B] = A
    x, y = map(int, sys.stdin.readline().split())
    X = find_par(x)
    Y = find_par(y)
    for i in X:
        if i in Y:
            print(i)
            break