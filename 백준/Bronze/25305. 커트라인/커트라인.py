import sys
N, k = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))

for i in range(N - 1, N - k - 1, -1):
    max = i
    for j in range(i):
        if score[max] < score[j]:
            max = j
    score[max], score[i] = score[i], score[max]

print(score[N - k])