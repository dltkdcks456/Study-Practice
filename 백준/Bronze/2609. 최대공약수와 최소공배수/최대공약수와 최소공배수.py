import sys

n, m = map(int, sys.stdin.readline().split())

A = set()
B = set()

for i in range(1, max(n, m) + 1):
    if n % i == 0:
        A.add(i)
    if m % i == 0:
        B.add(i)

ans1 = max(list(A & B))
print(ans1)
print(ans1 * (n // ans1) * (m // ans1))