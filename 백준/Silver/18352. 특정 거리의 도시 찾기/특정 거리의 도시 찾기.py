import sys
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        v = q.popleft()                     # 인접한 정점들을 하나씩 너비 우선으로 방문
        for w in adjList[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1 # 이전 방문 횟수에서 1을 더한 값을 저장
                if visited[w] == K + 1:         # 거리가 K인 경우 result에 해당 도시를 저장하고 건너 뛰어 append 방지
                    result.append(w)
                    continue
                q.append(w)                 # 다시 옮겨간 너비에서 탐색 진행


N, M, K, X = map(int, input().split())      # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호 입력
adjList = [[] for _ in range(N + 1)]        # 인접 리스트
visited = [0] * (N + 1)                     # 방문 기록
for _ in range(M):
    s, e = map(int, input().split())        # 정점끼리의 연결 정보(방향 존재)
    adjList[s].append(e)                    # 인접리스트 저장
result = []                                 # 거리가 K인 도시의 정보 저장할 리스트
bfs(X)
if result:
    print('\n'.join(map(str, sorted(result))))  # join 메소드를 통해 오름차순으로 하나씩 출력
else:
    print(-1)