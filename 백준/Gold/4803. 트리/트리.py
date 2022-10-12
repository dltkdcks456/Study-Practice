import sys

def dfs(n, par):
    global flag
    for w in adjList[n]:                                # 인접 노드로 진행
        if w != par:                                    # 부모 노드와 다른 곳에서만 탐색
            if visited[w] == 0:                         # 방문하지 않은 경우
                visited[w] = 1                          # 방문 처리
                dfs(w, n)
            else:
                flag = False


test = 1                                                # 테스트케이스 출력
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:                               # 0, 0 입력 시 정지
        break

    adjList = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)                             # 방문 기록을 할 저장공간
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adjList[a].append(b)
        adjList[b].append(a)

    result = 0
    for i in range(1, n + 1):
        if visited[i] == 0:                             # 방문하지 않으면 dfs진행
            flag = True                                 # 순환이 있는지 확인할 신호
            visited[i] = 1                              # 탐색 시작점 방문 처리
            dfs(i, -1)
            if flag:                                    # 순환이 없으면 트리 개수 1 증가
                result += 1

    if result == 0:                                     # 출력 부분
        print(f'Case {test}: No trees.')
    elif result == 1:
        print(f'Case {test}: There is one tree.')
    else:
        print(f'Case {test}: A forest of {result} trees.')
    test += 1