N = int(input())
board = [[0] * N for _ in range(N)]
cnt = 0
dr = [1, 1, 1,  0, 0]
dc = [1, -1, 0, -1, 1]

def queen(n, m, t_cnt, temp_c):
    global cnt
    if n == m:
        if t_cnt == n:
            cnt += 1
            return
        else:
            return
    else:
        for c in range(N):
            if board[n][c] == 0:
                t_cnt += 1
                board[n][c] = t_cnt
                temp_c = c
                for d in range(5):
                    for k in range(1, N - n):
                        nr = n + dr[d] * k
                        nc = c + dc[d] * k
                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                            board[nr][nc] = t_cnt
                queen(n + 1, m, t_cnt, temp_c)
                if board[n][temp_c] == t_cnt:
                    board[n][temp_c] = 0
                    for d in range(5):
                        for k in range(1, N - n):
                            nr = n + dr[d] * k
                            nc = temp_c + dc[d] * k
                            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == t_cnt:
                                board[nr][nc] = 0
                t_cnt -= 1
        else:
            return

queen(0, N, 0, 0)
print(cnt)