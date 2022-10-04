import sys

def bfs(n):
    global ans
    q = []
    q.append(n)
    visited[n] = 1
    while q:
        v = q.pop(0)
        if v == b:                      # 도착점 b에 도달할 경우
            ans = visited[v] - 1        # 그때까지의 진행값에서 -1을 뺀값을 ans에 저장
            return
        for w in adjList[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                q.append(w)

n = int(input())
a, b = map(int, input().split())
m = int(input())
adjList = [[] for _ in range(n + 1)]    # 인접 리스트 저장
visited = [0] * (n + 1)                 # 방문 기록
ans = -1
for _ in range(m):                      # 입력값 받기, 무방향 그래프
    x, y = map(int, input().split())
    adjList[x].append(y)
    adjList[y].append(x)
bfs(a)
print(ans)