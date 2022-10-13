import sys
import heapq

def djikstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in adjList[now]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(h, (distance[i[0]], i[0]))



V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
adjList = [[] for _ in range(V + 1)]
INF = 200001
distance = [INF] * (V + 1)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adjList[u].append([v, w])
djikstra(K)
for j in range(1, V + 1):
    if distance[j] == INF:
        print('INF')
    else:
        print(distance[j])