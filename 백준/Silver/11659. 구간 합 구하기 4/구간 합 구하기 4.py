import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    data[i] += data[i - 1]

for _ in range(M):
    s, e = map(int, input().split())
    print(data[e] - data[s - 1])