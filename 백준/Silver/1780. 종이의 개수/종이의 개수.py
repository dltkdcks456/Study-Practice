import sys

def cut(r, c, K):
    global cnt_0, cnt_m1, cnt_p1
    shape = paper[r][c]
    flag = True
    for nr in range(r, r + K):
        for nc in range(c, c + K):
            if paper[nr][nc] != shape:
                flag = False
                break
        if not flag:
            break
    if flag:
        if shape == 1:
            cnt_p1 += 1
        elif shape == 0:
            cnt_0 += 1
        else:
            cnt_m1 += 1
    else:
        K //= 3
        for ck_r in range(3):
            for ck_c in range(3):
                cut(r + ck_r * K, c + ck_c * K, K)

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt_0 = cnt_p1 = cnt_m1 = 0
cut(0, 0, N)
print(cnt_m1)
print(cnt_0)
print(cnt_p1)