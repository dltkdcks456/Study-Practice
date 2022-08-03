import sys

n, m = list(map(int, sys.stdin.readline().split()))

A = set()
B = set()

for i in range(1, n + 1):
    if n % i == 0:
        A.add(i)

for j in range(1, m + 1):
    if m % j == 0:
        B.add(j)

ans1 = sorted(list(A & B))[-1]
ans2 = ans1 * (n // ans1) * (m // ans1)

print(ans1)
print(ans2)