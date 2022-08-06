import sys


N, M = map(int,sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

sum_list = list()

Max = 3

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            a = num_list[i] + num_list[j] + num_list[k]
            if a <= M and a >= Max:
                Max = a

print(Max)
