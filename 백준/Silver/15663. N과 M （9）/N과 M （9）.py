N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
chosen = [-1] * M # 값을 저장할 곳
visited = [0] * N # 사용된 값 표시할 곳
save = set() # 이미 진행된 수열 저장소

def perm(n, M):
    if n == M:
        if tuple(chosen) not in save:
            save.add(tuple(chosen))
            print(' '.join(map(str, chosen)))
            return
        else:
            return
    for i in range(N):
        if visited[i] == 0:
            chosen[n] = num_list[i]
            visited[i] = 1
            perm(n + 1, M)
            chosen[n] = -1
            visited[i] = 0
perm(0, M)