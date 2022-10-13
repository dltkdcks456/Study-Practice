import sys
import heapq

def djikstra(start, li):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        for w in li[now]:
            if distance[w[0]] < dist:
                continue

            temp = dist + w[1]
            if distance[w[0]] > temp:
                distance[w[0]] = temp
                heapq.heappush(q, (temp, w[0]))
    return distance

N, M , X = map(int, sys.stdin.readline().split())
adjList_in = [[] for _ in range(N + 1)]
adjList_out = [[] for _ in range(N + 1)]
INF = 10000000
for _ in range(M):
    S, E, T = map(int, sys.stdin.readline().split())
    adjList_in[S].append([E, T])
    adjList_out[E].append([S, T])
D1 = djikstra(X, adjList_in)
D2 = djikstra(X, adjList_out)
for i in range(1, N + 1):
    D1[i] += D2[i]
print(max(D1[1:]))