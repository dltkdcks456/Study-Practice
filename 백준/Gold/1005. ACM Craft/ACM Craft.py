import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    global end
    q =deque([n])
    time[n] = D[n]
    while q:
        v = q.popleft()
        if adjList[v]:
            for w in adjList[v]:
                if time[w] < time[v] + D[w]:
                    time[w] = time[v] + D[w]
                    q.append(w)
        else:
            end.append(v)


T = int(input())
for test in range(T):                   # 진행할 테스트 케이스 수
    N, K = map(int, input().split())    #건물의 개수, 건설순서의 규칙
    D = [0] + list(map(int, input().split())) # 각 건물당 건설 시간(1~)
    adjList = [[] for _ in range(N + 1)]    #인접 리스트
    time = [0] * (N + 1)                    # 건물 짓는데 걸리는 시간을 기록할 공간
    for _ in range(K):
        a, b = map(int, input().split())
        adjList[b].append(a)            # 역방향에 대해서만 진행
    W = int(input())                    # 시작점
    end = []                             # 도착할 노드
    bfs(W)
    # print(time)
    # print(end)
    maxV = 0
    for i in end:
        if time[i] > maxV:
            maxV = time[i]
    print(maxV)