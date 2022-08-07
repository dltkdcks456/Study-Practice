import sys
N, k = map(int, sys.stdin.readline().split())
score = sorted(list(map(int, sys.stdin.readline().split())))
print(score[N - k])