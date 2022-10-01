import sys
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    move[n] = -1
    while q:
        v = q.popleft()
        if v == K:
            print(visited[v])
            li = []
            while move[v] != -1:
                li.append(v)
                v = move[v]
            li = li + [n]
            print(*li[::-1])
            break
        for w in [v - 1, v + 1, v * 2]:
            if 0 <= w <= 100000 and visited[w] > visited[v] + 1:
                visited[w] = visited[v] + 1
                move[w] = v
                q.append(w)

N, K = map(int, input().split())
visited = [100001] * 200001
visited[N] = 0
move = dict()
bfs(N)