import sys
input = sys.stdin.readline

def clean(current_r, current_c, direction):
    global cnt, end
    flag = True
    for dd in range(4):
        direction = ch_d[direction]
        nr = current_r + dr[direction]
        nc = current_c + dc[direction]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc]==0:
            room[nr][nc] = -1
            cnt += 1
            flag = False
            clean(nr, nc, direction)
            if end:
                return
    if flag:
        br = current_r - dr[direction]
        bc = current_c - dc[direction]
        if 0 <= br < N and 0 <= bc < M and room[br][bc] == 1:
            end = True
            return
        elif 0 <= br < N and 0 <= bc < M:
            clean(br, bc, direction)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]  # 0: 북, 1: 동, 2: 남, 3: 서
dc = [0, 1, 0, -1]
ch_d = [3, 0, 1, 2]
cnt = 1
room[r][c] = -1
end = False
clean(r, c, d)
print(cnt)
