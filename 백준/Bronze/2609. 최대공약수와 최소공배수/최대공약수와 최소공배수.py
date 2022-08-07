import sys
n, m = map(int, sys.stdin.readline().split())

A = list()

for i in range(1, max(n, m) + 1):
    if n % i == 0 and m % i == 0:
        A.append(i)

print(A[-1])
print(n * m // A[-1])