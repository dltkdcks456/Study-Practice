import sys
input = sys.stdin.readline

def dfs(n, par):
    global signal
    if not signal:
        return
    visited[n] = 1
    for m in adjList[n]:
        if m != par and visited[m] == 0:
            dfs(m, n)
        elif m != par and visited[m] == 1:
            signal = False
            return


flag = False
k = 1
while True:                                 # 테스트 케이스의 종료를 위한 while문
    li = []
    while True:                             # 입력에 대한 종료를 선언하기 위한 while문
        data = list(map(int, input().split()))
        if data:                            # 빈 입력이 주어질 때를 대비하여 조건문 작성
            li.extend(data)
            if li[-2] == 0 and li[-1] == 0:     # 0, 0이 들어오면 해당 while문 종료
                break
            elif li[-2] < 0 and li[-1] < 0:     # 둘다 음수일 경우 전체 테스트 케이스 종료
                flag = True
                break
    N = len(li)

    if flag:                                # flag의 신호를 통해 테스트 케이스 종료할지 여부 결정
        break

    maxV = max(li)                          # 가장 큰 노드의 값을 추출해 저장 크기를 결정
    adjList = [[] for _ in range(maxV + 1)] # 인접행렬에 대한 정보 저장
    visited = [0] * (maxV + 1)              # bfs 방문기록 리스트
    visited[0] = 1

    for i in range((N - 2) // 2):           # 부모노드에 대한 정보, 간선의 정보 처리
        p, ch = li[2 * i], li[2 * i + 1]
        adjList[p].append(ch)
        adjList[ch].append(p)

    signal = True
    dfs(maxV, -1)

    if not signal:
        print(f'Case {k} is not a tree.')
    else:
        for l in set(li):
            if visited[l] == 0:
                print(f'Case {k} is not a tree.')
                break
        else:
            print(f'Case {k} is a tree.')

    k += 1                                  # 테스트 케이스 경우의 수 증가