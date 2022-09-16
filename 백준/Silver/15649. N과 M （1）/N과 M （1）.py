N, M = map(int, input().split())
li = list(range(1, N + 1))

def perm(n, m):
    if n == m:
        print(*chosen)
        return
    else:
        for i in range(len(li)):
            if visited[i] == 0:
                chosen[n] = li[i]           # chosen의 n번째에 넣을 숫자 선택
                visited[i] = 1              # 방문한 곳은 1로 변경
                perm(n + 1, m)
                visited[i] = 0              # 재귀 복귀 시 방문했던 곳 0으로 원복

chosen = [-1] * M                           # 내가 골라서 담을 리스트
visited = [0] * len(li)                     # 이미 입력한 수를 확인할 리스트
perm(0, M)