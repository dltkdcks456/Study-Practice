import sys

T = int(sys.stdin.readline())

prime_bool = [False] * 2 + [True] * (10000 - 1)
for i in range(2, int(10000 ** 0.5) + 1):
    for j in range(i + i, 10000, i):
        if prime_bool[j]:
            prime_bool[j] = False

for i in range(T):
    n = int(sys.stdin.readline())
    for i in range(int(n // 2), 1, -1):
        if prime_bool[i] and prime_bool[n - i]:
            print(i, n - i)
            break