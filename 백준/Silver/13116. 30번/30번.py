import sys

def find_par(n):
    li = []
    while n:
        li.append(n)
        n = par[n]
    return li

T = int(sys.stdin.readline())
par = [0] * 1024
for i in range(len(par)):
    par[i] = i // 2
for test in range(T):
    A, B = map(int, sys.stdin.readline().split())
    A_par = set(find_par(A))
    B_par = set(find_par(B))
    print(max(A_par & B_par) * 10)
