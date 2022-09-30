import sys
input = sys.stdin.readline
N = int(input())
distance = list(map(int, input().split())) + [0]
cost = list(map(int, input().split()))
ans = cost[0] * distance[0]
for i in range(1, N - 1):
    if cost[i - 1] < cost[i]:
        cost [i] = cost[i - 1]
        ans += cost[i] * distance[i]
    else:
        ans += cost[i] * distance[i]
print(ans)