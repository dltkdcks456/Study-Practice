import sys
import heapq
input = sys.stdin.readline

def djikstra(s):
    q = []
    heapq.heappush(q, [0, s])
    distance = [float('inf')] * (N + 1)
    distance[s] = 0
    while q:
        dis, node = heapq.heappop(q)
        for k in adjList[node]:
            next_dist = dis + k[1]
            if distance[k[0]] < next_dist:
                continue
            distance[k[0]] = next_dist
            heapq.heappush(q, [distance[k[0]], k[0]])
    return distance



N, E = map(int, input().split())
adjList = [[] for _ in range(N + 1)]
for _ in range(E):
    v, u, w = map(int, input().split())
    adjList[v].append([u, w])
    adjList[u].append([v, w])
v1, v2 = map(int, input().split())
S = djikstra(1)
V1 = djikstra(v1)
V2 = djikstra(v2)
ans = min(S[v1] + V1[v2] + V2[N], S[v2] + V2[v1] + V1[N])
if ans == float('inf'):
    print(-1)
else:
    print(ans)