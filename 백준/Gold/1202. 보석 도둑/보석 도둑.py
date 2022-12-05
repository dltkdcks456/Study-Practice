import sys
import heapq
input = sys.stdin.readline


N, K = map(int, input().split())
crystal = []

for _ in range(N):
    M, V = map(int, input().split())
    crystal.append([M, V])

bags = []
for _ in range(K):
    bags.append(int(input()))

crystal.sort(reverse=True)
bags.sort()


temp_crystal = []
ans = 0
for bag in bags:
    while crystal and crystal[-1][0] <= bag:
        heapq.heappush(temp_crystal, -crystal[-1][1])
        crystal.pop()
    if temp_crystal:
        ans -= heapq.heappop(temp_crystal)
    elif not crystal:
        break
print(ans)